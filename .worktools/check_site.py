from pathlib import Path
from urllib.parse import unquote,urlsplit
from html.parser import HTMLParser
from playwright.sync_api import sync_playwright
import json
ROOT=Path(__file__).resolve().parent.parent
class Parse(HTMLParser):
    def __init__(self):super().__init__();self.ids=[];self.refs=[];self.h1=0
    def handle_starttag(self,tag,attrs):
        d=dict(attrs)
        if 'id' in d:self.ids.append(d['id'])
        if tag=='h1':self.h1+=1
        for k in ['href','src']:
            if k in d:self.refs.append(d[k])
pages=[ROOT/'index.html']+list(ROOT.glob('report-*.html'))
for path in pages:
    p=Parse();p.feed(path.read_text(encoding='utf-8'))
    assert p.h1==1,(path.name,'h1',p.h1)
    assert len(p.ids)==len(set(p.ids)),(path.name,'duplicate ids')
    for ref in p.refs:
        u=urlsplit(ref)
        if u.scheme:continue
        if not u.path:
            assert u.fragment in p.ids,(path.name,ref)
        else:assert (path.parent/unquote(u.path)).exists(),(path.name,ref)
print('HTML references and structure: OK')
with sync_playwright() as pw:
    try: browser=pw.chromium.launch(headless=True)
    except Exception: browser=pw.chromium.launch(channel='msedge',headless=True)
    page=browser.new_page()
    errors=[];page.on('pageerror',lambda e:errors.append(str(e)))
    for path in pages:
        for width in [360,390,768,1440]:
            page.set_viewport_size({'width':width,'height':1000})
            page.goto(path.as_uri())
            page.wait_for_timeout(1000)
            page.evaluate('document.fonts.ready')
            assert not page.evaluate('document.documentElement.scrollWidth>innerWidth+1'),(path.name,width,'overflow')
            if path.name!='index.html':
                count=page.locator('canvas').count()
                assert page.evaluate('Object.keys(Chart.instances).length')==count,(path.name,'charts missing')
                assert page.locator('.oe-figure__chart:visible').count()==count,(path.name,'charts hidden')
            else:
                assert page.locator('.oe-hero__media img').evaluate('(e)=>e.complete && e.naturalWidth>0'),'cover missing'
            if width in [390,1440]:
                page.screenshot(path=str(ROOT/'.worktools'/f'{path.stem}-{width}.png'),full_page=True)
        if path.name!='index.html':
            page.set_viewport_size({'width':390,'height':900})
            page.reload();page.locator('.nav__toggle').click()
            assert page.locator('.nav__toggle').get_attribute('aria-expanded')=='true'
            page.keyboard.press('Escape')
            assert page.locator('.nav__toggle').get_attribute('aria-expanded')=='false'
            page.locator('details').first.click() if page.locator('details').count() else None
        print(path.name+': responsive, charts, navigation OK')
    assert not errors,errors
    browser.close()
print('Browser page errors: 0')

