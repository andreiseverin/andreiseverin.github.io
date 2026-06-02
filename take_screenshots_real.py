import time
import sys
import uuid
from playwright.sync_api import sync_playwright

# Support UTF-8 console output for Windows shell
sys.stdout.reconfigure(encoding='utf-8')

def capture_all():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        # Use a standard high-definition viewport
        page = browser.new_page(viewport={"width": 1920, "height": 1080})
        
        # 1. Capture Login Screen
        print("1. Capturing login screen...")
        page.goto('http://localhost:3000/')
        page.wait_for_load_state('networkidle')
        time.sleep(2)
        page.screenshot(path='f:/andreiseverin.github.io/images/projects/login-screen.png')
        print("Captured login-screen.png")
        
        # Register a unique user
        print("Registering new user...")
        page.click('text=Register New User')
        time.sleep(1)
        
        username = f"user_{uuid.uuid4().hex[:8]}"
        print(f"Username: {username}")
        page.fill('#login-username', username)
        page.fill('#login-password', 'password123')
        page.click('button:has-text("REGISTER")')
        
        page.wait_for_url('**/dashboard', timeout=10000)
        page.wait_for_load_state('networkidle')
        time.sleep(4)
        
        # 2. Capture Exercise Panel
        print("2. Capturing exercise panel...")
        # Click Mainframe Foundations track
        page.click('.lesson-track-tab:has-text("Mainframe Foundations")')
        time.sleep(1.5)
        # Click module
        page.click('text="01. TSO & ISPF Introduction"')
        time.sleep(1.5)
        # Click TSO Login Procedure lesson
        page.click('text="TSO Login Procedure"')
        time.sleep(2.5)
        # Take screenshot of the page showing the lesson instructions on the right
        page.screenshot(path='f:/andreiseverin.github.io/images/projects/exercise-panel.png')
        print("Captured exercise-panel.png")
        
        # 3. Capture ISPF Primary Option Menu
        print("3. Logging in to TSO to capture ISPF Primary Menu...")
        # Click inside the terminal panel area to focus it
        page.click('.panel')
        time.sleep(1)
        
        # The userid field defaults to USER01. We can press Tab to move to password, then type PASSWORD and press Enter.
        page.keyboard.press('Tab')
        time.sleep(0.5)
        page.keyboard.type('PASSWORD')
        time.sleep(0.5)
        page.keyboard.press('Enter')
        time.sleep(3)
        
        # Dismiss the completion modal if it pops up, so we can see the terminal behind it
        try:
            print("Looking for completion modal...")
            # Wait up to 3 seconds for the return/close button to become visible, then click it
            modal_btn = page.locator('.completion-modal .btn-secondary')
            if modal_btn.is_visible():
                modal_btn.click()
                print("Modal closed.")
                time.sleep(1)
        except Exception as e:
            print("Modal close skipped/failed, moving on:", e)
            
        page.screenshot(path='f:/andreiseverin.github.io/images/projects/ispf-primary.png')
        print("Captured ispf-primary.png")
        
        # 4. Capture COBOL Editor
        print("4. Capturing COBOL editor...")
        page.click('button:has-text("Free Dev")')
        time.sleep(1.5)
        
        page.click('text="HELLO.cbl"')
        time.sleep(2.5)
        page.screenshot(path='f:/andreiseverin.github.io/images/projects/cobol-editor.png')
        print("Captured cobol-editor.png")
        
        # 5. Capture JES Spool Viewer
        print("5. Submitting JCL to capture JES Spool...")
        page.click('text="RUNHELLO.jcl"')
        time.sleep(1.5)
        
        # Submit the JCL using keyboard shortcut Control+Enter
        page.keyboard.press('Control+Enter')
        print("Submitted JCL...")
        time.sleep(6) # Wait for job completion logs to load in spool
        
        page.screenshot(path='f:/andreiseverin.github.io/images/projects/jes-spool.png')
        print("Captured jes-spool.png")
        
        # 6. Capture CICS Terminal
        print("6. Capturing CICS terminal...")
        page.click('button:has-text("Lesson Mode")')
        time.sleep(1.5)
        
        page.click('.lesson-track-tab:has-text("CICS")')
        time.sleep(1.5)
        
        page.click('text="12. CICS Fundamentals"')
        time.sleep(1.5)
        
        page.click('text="Introduction to CICS"')
        time.sleep(2.5)
        
        page.screenshot(path='f:/andreiseverin.github.io/images/projects/cics-terminal.png')
        print("Captured cics-terminal.png")
        
        browser.close()

if __name__ == '__main__':
    capture_all()
