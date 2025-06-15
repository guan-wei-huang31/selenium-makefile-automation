import pytest
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from dotenv import load_dotenv

load_dotenv()
TEST_WEBSITE = os.getenv("test_website")

@pytest.fixture(scope="module")
def my_driver():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    yield driver   # yield: return driver to the test function and pause execution until the test finishes
    driver.quit()

def test_experience_click(my_driver):
    my_driver.get(TEST_WEBSITE)
    wait = WebDriverWait(my_driver, 10)   # create an explicit wait object with a maximum wait time of 10 seconds

    exp_button = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Experiences")))   # # repeatedly check until an <a> element with text "Experiences" is clickable
    exp_button.click()

    wait.until(EC.url_contains("experiences"))   # repeatedly check until the current URL contains "experiences"

    assert "experiences" in my_driver.current_url   # verify that the URL contains "experiences"
    print(f"[Experience button click] Success. Current URL: {my_driver.current_url}")

def test_skill_click(my_driver):
    my_driver.get("https://guan-wei.vercel.app/")
    wait = WebDriverWait(my_driver, 10)   

    exp_button = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Skills")))  
    exp_button.click()

    wait.until(EC.url_contains("skills"))  

    assert "skills" in my_driver.current_url 
    print(f"[Skills button click] Success. Current URL: {my_driver.current_url}")
