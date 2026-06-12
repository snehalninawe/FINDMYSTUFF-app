from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

def test_login():

    driver = webdriver.Chrome()
    driver.maximize_window()

    driver.get("https://findmystuff-web.vercel.app/")

    time.sleep(2)

    # click explore items
    driver.find_element(By.XPATH, "//a[text()='Browse Items']").click()

    time.sleep(1)
    

    
    search_box=driver.find_element(By.XPATH, "//input").send_keys(
        "Bottle"
    )

    time.sleep(1)
    driver.find_element(By.XPATH, "//select[contains(.,'All Types')]").click()
    time.sleep(1)
    driver.find_element(By.XPATH, "//option[text()='Lost']").click()
    print("Lost option selected")
    
    driver.find_element(By.XPATH, "//select[contains(.,'All Categories')]").click()
    time.sleep(1)
    driver.find_element(By.XPATH, "//option[text()='Others']").click()
    print("Others selected")
    
    time.sleep(1)

    search_box.send_keys(Keys.ENTER)

    time.sleep(3)

    # ✅ verification
    assert "books" in driver.page_source.lower()

    print("Search working ✔")

    driver.quit()

