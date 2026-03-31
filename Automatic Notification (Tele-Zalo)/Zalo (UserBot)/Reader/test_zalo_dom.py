from playwright.sync_api import sync_playwright
import os

with sync_playwright() as p:
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    user_data_dir = os.path.join(base_dir, 'zalo_user_data_session')
    browser = p.chromium.launch_persistent_context(user_data_dir=user_data_dir, headless=True, no_viewport=True)
    page = browser.pages[0]
    page.goto('https://chat.zalo.me/')
    
    print("Waiting for login...")
    page.wait_for_selector('#contact-search-input', timeout=60000)
    
    print("Searching for Mom...")
    search_input = page.locator('#contact-search-input')
    search_input.click()
    page.keyboard.press("Control+A")
    page.keyboard.press("Backspace")
    search_input.fill("0976022488")
    page.wait_for_timeout(2000)
    page.keyboard.press("Enter")
    page.wait_for_timeout(3000)
    
    html = page.evaluate('() => document.querySelector("#messageViewContainer")?.outerHTML || document.body.innerHTML')
    with open("zalo_dom.html", "w", encoding="utf-8") as f:
        f.write(html)
    
    print("DOM saved to zalo_dom.html")
    browser.close()
