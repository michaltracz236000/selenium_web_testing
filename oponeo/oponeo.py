import oponeo.constants as con
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

import time

class Oponeo(webdriver.Chrome):
    def __init__(self):
        chrome_options = Options()
        chrome_options.add_argument("--disable-search-engine-choice-screen")
        service = Service(executable_path="chromedriver.exe")
        super().__init__(chrome_options,service)
        self.implicitly_wait(15)
        self.maximize_window()

    def __exit__(self, exc_type, exc, traceback):
        self.quit()

    def load_page(self):
        self.get(con.BASE_URL)

    def decline_cookies(self):
        decline_btn=self.find_element(By.CSS_SELECTOR,"#consentsBar > div > div > span.reject.button.primary.md.solid")
        decline_btn.click()

    def choose_size(self, width, profile, diameter):
        width_tag = self.find_element(By.ID,"_carTires_ctTS_ddlDimWidth")
        select_width = Select(width_tag)
        select_width.select_by_value(width)
    
    
    def sleep_browser(self):
        time.sleep(10)