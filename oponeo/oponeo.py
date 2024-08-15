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
            if option.get_attribute("value")==ratio:
                select_ratio.select_by_value(ratio)
                select_ratio_flag=1
                break
        if select_ratio_flag!=1:
            print("Ratio not avaliable")
            return
        time.sleep(2)
        diameter_tag = self.find_element(By.NAME,"_carTires_ctTS_ddlDimDiameter")
        select_diameter = Select(diameter_tag)
        select_diameter_flag=0
        for option in select_diameter.options:
            if option.get_attribute("value")==diameter:
                select_diameter.select_by_value(diameter)
                select_diameter_flag=1
                break
        if select_diameter_flag!=1:
            print("Diameter not avaliable")
        time.sleep(2)

    def click_choose_class(self):
        choose = self.find_element(By.CSS_SELECTOR,"#forSize > div:nth-child(2) > div.chooseBox.producer > div")
        choose.click()
        time.sleep(2)

    def select_premium(self):
        checkbox_premium = self.find_element(By.CSS_SELECTOR,"#forSize > div:nth-child(2) > div.chooseBox.producer.visible > div > div.options > div > div.producersGroup > div.groupItem.groupPremium > div.groupTitle > label > span > span")
        checkbox_premium.click()

    def select_middle(self):
        checkbox_middle = self.find_element(By.CSS_SELECTOR,"#forSize > div:nth-child(2) > div.chooseBox.producer.visible > div > div.options > div > div.producersGroup > div.groupItem.groupMedium > div.groupTitle > label > span > span")
        checkbox_middle.click()

    def select_economic(self):
        checkbox_economic = self.find_element(By.CSS_SELECTOR,"#forSize > div:nth-child(2) > div.chooseBox.producer.visible > div > div.options > div > div.producersGroup > div.groupItem.groupCheap > div.groupTitle > label > span > span")
        checkbox_economic.click()
    
    
    def sleep_browser(self):
        time.sleep(10)