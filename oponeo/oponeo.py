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

    def choose_size(self, width, ratio, diameter):
        width_tag = self.find_element(By.ID,"_carTires_ctTS_ddlDimWidth")
        select_width = Select(width_tag)
        select_width_flag=0
        for option in select_width.options:
            if option.get_attribute("value")==width:
                select_width.select_by_value(width) 
                select_width_flag=1
                break
        if select_width_flag!=1:
            print("Width not avaliable")
            return
        time.sleep(1)
        ratio_tag = self.find_element(By.ID,"_carTires_ctTS_ddlDimRatio")
        select_ratio = Select(ratio_tag)
        select_ratio_flag = 0
        for option in select_ratio.options:
            print(option.get_attribute("value"))
            if option.get_attribute("value")==ratio:
                select_ratio.select_by_value(ratio)
                select_ratio_flag=1
                break
        if select_ratio_flag!=1:
            print("Profile not avaliable")
            return
        diameter_tag = self.find_element(By.ID,"_carTires_ctTS_ddlDimDiameter")

    
    
    def sleep_browser(self):
        time.sleep(20)