from playwright.sync_api import sync_playwright
import os

with sync_playwright() as p:
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    user_data_dir = os.path.join(base_dir, 'zalo_user_data_session')
    browser = p.chromium.launch_persistent_context(user_data_dir=user_data_dir, headless=True, no_viewport=True)
    page = browser.pages[0]
    page.goto('https://chat.zalo.me/')
    
    page.wait_for_selector('#contact-search-input', timeout=60000)
    page.wait_for_timeout(3000)
    
    # Dump the container of the left panel conversations
    html = page.evaluate('() => { var n = document.querySelector("#conversationListId"); return n ? n.innerHTML : document.body.innerHTML; }')
    with open("zalo_left_panel.html", "w", encoding="utf-8") as f:
        f.write(html)
    
    print("Left panel DOM saved.")
    browser.close()
