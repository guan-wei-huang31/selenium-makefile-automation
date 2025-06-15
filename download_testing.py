import pytest
import time
import os
import shutil
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
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
    download_dir = os.path.abspath("downloads") 
    if os.path.exists(download_dir):
        shutil.rmtree(download_dir) 
    os.makedirs(download_dir, exist_ok=True)    

    chrome_options = Options()
    chrome_options.add_experimental_option("prefs", {
        "download.default_directory": download_dir,  # setting download directory
        "download.prompt_for_download": False,   # don't show download request
    })

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    driver.download_dir = download_dir
    yield driver
    driver.quit()


def test_resume_click(my_driver):
    my_driver.get(TEST_WEBSITE)
    wait = WebDriverWait(my_driver, 10)  

    exp_button = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Resume")))  
    exp_button.click()

    time.sleep(5)
    downloaded_files = os.listdir(my_driver.download_dir)
    pdf_files = [f for f in downloaded_files if f.endswith(".pdf")]

    assert len(pdf_files) > 0, "PDF was not downloaded!"
    print(f"[Download button click] Success. Downloaded files: {pdf_files}")
