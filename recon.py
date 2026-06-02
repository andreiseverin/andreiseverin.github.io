import time
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page(viewport={"width": 1920, "height": 1080})
    
    print("Navigating to http://localhost:3000/...")
    page.goto('http://localhost:3000/')
    page.wait_for_load_state('networkidle')
    time.sleep(2)
    
    # Save landing page screenshot
    page.screenshot(path='login_screen_temp.png')
    print("Saved login_screen_temp.png")
    
    # Register a new user
    print("Switching to register...")
    page.click('text=Register New User')
    time.sleep(1)
    
    # Generate a unique username to avoid collisions
    import uuid
    username = f"user_{uuid.uuid4().hex[:8]}"
    print(f"Registering username: {username}")
    
    page.fill('#login-username', username)
    page.fill('#login-password', 'password123')
    page.click('button:has-text("REGISTER")')
    
    # Wait for navigation to dashboard
    print("Waiting for dashboard...")
    page.wait_for_url('**/dashboard', timeout=10000)
    page.wait_for_load_state('networkidle')
    time.sleep(5)
    
    # Save dashboard screenshot
    page.screenshot(path='dashboard_temp.png')
    print("Saved dashboard_temp.png")
    
    # Let's inspect the DOM elements or print text content
    print("Page Title:", page.title())
    
    browser.close()
