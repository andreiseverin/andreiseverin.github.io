import time
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page(viewport={"width": 1920, "height": 1080})
    
    print("Navigating to http://localhost:3000/...")
    page.goto('http://localhost:3000/')
    page.wait_for_load_state('networkidle')
    
    # Register a new user
    page.click('text=Register New User')
    time.sleep(1)
    
    import uuid
    username = f"user_{uuid.uuid4().hex[:8]}"
    print(f"Registering user: {username}")
    page.fill('#login-username', username)
    page.fill('#login-password', 'password123')
    page.click('button:has-text("REGISTER")')
    
    page.wait_for_url('**/dashboard', timeout=10000)
    page.wait_for_load_state('networkidle')
    time.sleep(5)
    
    # Print list of buttons and text contents
    print("PAGE TITLE:", page.title())
    
    # Let's inspect the active elements in the center panel
    # E.g. what is open in the main container?
    html_content = page.content()
    with open('dashboard_elements.txt', 'w', encoding='utf-8') as f:
        f.write(html_content)
        
    print("Saved DOM to dashboard_elements.txt")
    
    browser.close()
