### This is front-end tester for Wicked-Adventure APP

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.utils import ChromeType
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

total_errors=0
chrome_service = Service(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install())
chrome_options = Options()
options = [
    "--headless",
    "--disable-gpu",
    "--window-size=1920,1200",
    "--ignore-certificate-errors",
    "--disable-extensions",
    "--no-sandbox",
    "--disable-dev-shm-usage"
]
for option in options:
    chrome_options.add_argument(option)

driver = webdriver.Chrome(service=chrome_service, options=chrome_options)
driver.get('http://0.0.0.0:8000/')
print(driver.title)

def check_login():
    '''
        This function checks if the user can login.
        If it successful, then script tries to click on Add profile button
        as it apears only when the user is logged in.
    '''
    home_button = driver.find_element(By.CSS_SELECTOR, ".material-icons-outlined")
    home_button.click()
    time.sleep(1)
    login_button = driver.find_element(By.NAME, "base_login_btn")
    login_button.click()
    time.sleep(1)
    login_field = driver.find_element(By.NAME, "username")
    login_field.send_keys("seleniumtester")
    time.sleep(1)
    pass_field = driver.find_element(By.NAME, "password")
    pass_field.send_keys("1a2s3d4f5g6h7j")
    time.sleep(1)
    enter_login = driver.find_element(By.CSS_SELECTOR, '.btn-primary')
    enter_login.click()
    time.sleep(5)
    add_profile = driver.find_element(By.NAME, "base_add_prof_btn")
    add_profile.click()

    '.nav-item:nth-child(1) .btn'
    time.sleep(2)
    print("Loging function has passed!!!")

def check_search():
    '''
        This function checks if search filed presents and works
    '''
    home_button = driver.find_element(By.CSS_SELECTOR, ".material-icons-outlined")
    home_button.click()
    time.sleep(1)
    search_field = driver.find_element(By.NAME, "search_field")
    search_field.send_keys("selenium_tester")
    time.sleep(1)
    search_button = driver.find_element(By.NAME, "search_button")
    search_button.click()
    print("Search field has passed!!!")

def check_register():
    '''
        This function checks if the user can get registered.
        If it successful, then function 'check_login()' uses
        same credentials to check if the user can get logged in.
    '''
    home_button = driver.find_element(By.CSS_SELECTOR, ".material-icons-outlined")
    home_button.click()
    time.sleep(1)

    register_button = driver.find_element(By.NAME, "base_register_btn")
    register_button.click()
    time.sleep(1)

    username_filed = driver.find_element(By.ID, "username")
    username_filed.send_keys("seleniumtester")
    time.sleep(1)

    email_field = driver.find_element(By.ID, "email")
    email_field.send_keys("seleniumtester@qwerty.com")
    time.sleep(1)

    first_name_field = driver.find_element(By.ID, "first_name")
    first_name_field.send_keys("seleniumtester")
    time.sleep(1)

    last_name_field = driver.find_element(By.ID, "last_name")
    last_name_field.send_keys("seleniumtester")
    time.sleep(1)

    password_filed = driver.find_element(By.ID, "password1")
    password_filed.send_keys("1a2s3d4f5g6h7j")
    time.sleep(1)

    password2_filed = driver.find_element(By.ID, "password2")
    password2_filed.send_keys("1a2s3d4f5g6h7j")
    time.sleep(1)

    submit_button = driver.find_element(By.CSS_SELECTOR, ".btn-primary")
    submit_button.click()
    time.sleep(5)
    print("Register pages has passed!!!")

if __name__ == "__main__":
    check_search()
    check_register()
    check_login()
    driver.close() #close the web page.
    print('Front-end test SUCCESSFULY passed')
