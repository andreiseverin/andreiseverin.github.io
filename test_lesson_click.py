import time
import sys
import uuid
from playwright.sync_api import sync_playwright

# Set stdout to UTF-8 for Windows console support
sys.stdout.reconfigure(encoding='utf-8')

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page(viewport={"width": 1920, "height": 1080})
    
    page.goto('http://localhost:3000/')
    page.click('text=Register New User')
    time.sleep(1)
    
    username = f"user_{uuid.uuid4().hex[:8]}"
    page.fill('#login-username', username)
    page.fill('#login-password', 'password123')
    page.click('button:has-text("REGISTER")')
    page.wait_for_url('**/dashboard')
    page.wait_for_load_state('networkidle')
    time.sleep(4)
    
    # Click track
    page.click('.lesson-track-tab:has-text("Mainframe Foundations")')
    time.sleep(1.5)
    
    # Print what modules are visible
    print("VISIBLE TEXTS AFTER TRACK CLICK:")
    print(page.locator('.lesson-module').all_text_contents())
    
    # Click module
    page.click('text="01. TSO & ISPF Introduction"')
    time.sleep(1.5)
    
    # Print lessons visible
    print("VISIBLE LESSONS AFTER MODULE CLICK:")
    print(page.locator('.lesson-item').all_text_contents())
    
    # Click lesson
    page.click('text="TSO Login Procedure"')
    time.sleep(3)
    
    # Save a screenshot of the state
    page.screenshot(path='lesson_clicked_state.png')
    print("Saved lesson_clicked_state.png")
    
    # Check if panel is visible
    print("Is panel visible:", page.locator('.panel').is_visible())
    print("Is terminal visible:", page.locator('text="VTAM / TSO TERMINAL - SESSION A@T601"').is_visible())
    
    # Print page content around panel
    with open('lesson_dom.txt', 'w', encoding='utf-8') as f:
        f.write(page.content())
        
    browser.close()
