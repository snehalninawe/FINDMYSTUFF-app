from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def testLogin():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(10)

    driver.get('https://findmystuff-web.vercel.app/')

    time.sleep(2)

    # click report item 
    driver.find_element(By.XPATH, "//a[text()='Report Item']").click()

    driver.find_element(By.NAME, "name").send_keys("water bottle")
    driver.find_element(By.NAME, "description").send_keys(
        "a blue colour water bottle missing from canteen."
    )

    driver.find_element(By.NAME, "category").click()
    time.sleep(1)
    driver.find_element(By.XPATH, "//option[text()='Others']").click()
    print("Others selected")

    driver.find_element(By.NAME, "location").send_keys("Canteen")

    # ================= DATE PICKER =================
    # wait + scroll
    date_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "date"))
    )

    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", date_field)

    # set date directly
    date_field.clear()
    date_field.send_keys("2026-06-15")

    # ================= FILE UPLOAD =================
    file_input = driver.find_element(By.XPATH, "//input[@type='file']")
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", file_input)

    file_input.send_keys(
        "C:\\Users\\Snehal Ninawe\\OneDrive\\Desktop\\bottle.jpg"
    )
    
    # submit button
    submit_btn = driver.find_element(By.XPATH, "//button[@type='submit']")
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", submit_btn)
    driver.execute_script("arguments[0].click();", submit_btn)

    time.sleep(3)

    # verification
    assert "success" in driver.page_source.lower()

    print("Report item working ✔")

    time.sleep(2)

    driver.quit()