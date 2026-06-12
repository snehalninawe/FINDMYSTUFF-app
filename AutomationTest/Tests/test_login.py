from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def testLogin():
    driver = webdriver.Chrome()
    driver.maximize_window()
    
    driver.implicitly_wait(10)
    
    driver.get('https://findmystuff-web.vercel.app/')
    
    time.sleep(2)
    
    #click login btn
    loginBtn = driver.find_element(By.XPATH,"//a[contains(.,'User Login')]")
    loginBtn.click()
    
    #locate username field
    username = driver.find_element(By.NAME,"emailcont")
    username.send_keys("ninawesnehal3108@gmail.com")
    
    #locate password field
    password = driver.find_element(By.NAME,"password")
    password.send_keys("snehal123")
    
    #locate login button
    login_button = driver.find_element(By.TAG_NAME,"button")
    login_button.click()
    
    print("CURRENT URL:", driver.current_url)

    # ✅ better check (safe)
    assert "login" not in driver.current_url.lower()

    
    driver.quit()
    
    