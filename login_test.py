from selenium import webdriver
from selenium.webdriver.common.by import By
import time

LOGIN_URL = "https://academy.powerlearnprojectafrica.org/login"
VALID_USERNAME = "oyugidenis82@gmail.com"
VALID_PASSWORD = "Fpzds@2025"
INVALID_USERNAME = "fakeuser@example.com"
INVALID_PASSWORD = "wrongpass"

def run_test(username, password, label):
    driver = webdriver.Chrome()
    driver.get(LOGIN_URL)
    
    try:
        # Adjust selectors if needed (verify in browser)
        driver.find_element(By.NAME, "email").send_keys(username)
        driver.find_element(By.NAME, "password").send_keys(password)
        driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
        
        time.sleep(3)

        current_url = driver.current_url
        page_src = driver.page_source.lower()
        
        if label == "Valid":
            if "/login" not in current_url:
                print(f"[PASS] Valid login success: {username}")
            else:
                print(f"[FAIL] Valid login failed: {username}")
        else:  # Invalid test
            if "invalid" in page_src or current_url.endswith("/login"):
                print(f"[PASS] Invalid login correctly blocked: {username}")
            else:
                print(f"[FAIL] Invalid login unexpectedly succeeded: {username}")

        screenshot = f"{label}_login_{'pass' if 'PASS' in locals() else 'fail'}.png"
        driver.save_screenshot(screenshot)
        print(f"Screenshot saved: {screenshot}")
    except Exception as e:
        print(f"[ERROR in {label} Test] {e}")
    finally:
        driver.quit()

# Run tests
print("=== Valid Login Test ===")
run_test(VALID_USERNAME, VALID_PASSWORD, "Valid")

print("\n=== Invalid Login Test ===")
run_test(INVALID_USERNAME, INVALID_PASSWORD, "Invalid")
