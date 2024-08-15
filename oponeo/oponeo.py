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
        time.sleep(1)
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
        time.sleep(1)

    def click_choose_class(self):
        choose = self.find_element(By.CSS_SELECTOR,"#forSize > div:nth-child(2) > div.chooseBox.producer > div")
        choose.click()
        time.sleep(1)

    def select_premium(self):
        checkbox_premium = self.find_element(By.CSS_SELECTOR,"#forSize > div:nth-child(2) > div.chooseBox.producer.visible > div > div.options > div > div.producersGroup > div.groupItem.groupPremium > div.groupTitle > label > span > span")
        checkbox_premium.click()
        time.sleep(1)

    def select_middle(self):
        checkbox_middle = self.find_element(By.CSS_SELECTOR,"#forSize > div:nth-child(2) > div.chooseBox.producer.visible > div > div.options > div > div.producersGroup > div.groupItem.groupMedium > div.groupTitle > label > span > span")
        checkbox_middle.click()
        time.sleep(1)

    def select_economic(self):
        checkbox_economic = self.find_element(By.CSS_SELECTOR,"#forSize > div:nth-child(2) > div.chooseBox.producer.visible > div > div.options > div > div.producersGroup > div.groupItem.groupCheap > div.groupTitle > label > span > span")
        checkbox_economic.click()
        time.sleep(1)
    
    def agree_select_tire_class(self):
        agree_btn = self.find_element(By.ID,"_carTires_ctTS_olProducers_lbAck0")
        agree_btn.click()
        time.sleep(1)

    def click_choose_type(self):
        choose = self.find_element(By.CSS_SELECTOR,"#forSize > div:nth-child(2) > div.chooseBox.season > div")
        choose.click()
        time.sleep(1)
        summer_btn = self.find_element(By.CSS_SELECTOR,"#_carTires_ctTS_olSeasons_rix_0 > label > span")
        summer_btn.click()
        time.sleep(1)

    def select_summer_type(self):
        summer_btn = self.find_element(By.CSS_SELECTOR,"#_carTires_ctTS_olSeasons_rix_0 > label > span")
        summer_btn.click()
        time.sleep(1)

    def select_winter_type(self):
        winter_btn = self.find_element(By.CSS_SELECTOR,"#_carTires_ctTS_olSeasons_rix_1 > label > span > span")
        winter_btn.click()
        time.sleep(1)
    
    def select_all_season_type(self):
        all_season_btn = self.find_element(By.CSS_SELECTOR,"#_carTires_ctTS_olSeasons_rix_2 > label > span > span")
        all_season_btn.click()
        time.sleep(1)
        
    def agree_select_tire_type(self):
        agree_btn = self.find_element(By.ID,"_carTires_ctTS_olSeasons_lbAck0")
        agree_btn.click()
        time.sleep(1)

    def search_tires(self):
        agree_btn = self.find_element(By.ID,"_carTires_ctTS_lbSubmit0")
        agree_btn.click()
        time.sleep(1)

    def tire_price(self, min, max):
        min_price_input = self.find_element(By.ID, "_ctTS_inpPF")
        min_price_input.click()
        time.sleep(2)
        for i in range (0,5):
            min_price_input.send_keys(Keys.ARROW_RIGHT)
        for i in range (0,5):
            min_price_input.send_keys(Keys.BACKSPACE)
        min_price_input.send_keys(min)
        time.sleep(2)
        max_price_input = self.find_element(By.ID, "_ctTS_inpPT")
        max_price_input.click()
        time.sleep(2)
        for i in range (0,5):
            max_price_input.send_keys(Keys.ARROW_RIGHT)
        for i in range (0,5):
            max_price_input.send_keys(Keys.BACKSPACE)
        max_price_input.send_keys(max)
        time.sleep(2)
    
    def select_speed(self,speed):
        speed_input = self.find_element(By.CSS_SELECTOR,"#forSize > div.advanced > div:nth-child(1) > div.chooseBox.speedIndex > div")
        speed_input.click()
        time.sleep(2)
        if speed=="190":
            if self.find_element(By.ID,"_ctTS_olSpeedIx_rix_1").get_attribute("class")=='disabled':
                print("Predkosc niedostępna")
            else:
                self.find_element(By.CSS_SELECTOR,"#_ctTS_olSpeedIx_rix_1 > label > span > span").click()
        elif speed=="210":
            if self.find_element(By.ID,"_ctTS_olSpeedIx_rix_2").get_attribute("class")=='disabled':
                print("Predkosc niedostępna")
            else:
                self.find_element(By.CSS_SELECTOR,"#_ctTS_olSpeedIx_rix_2 > label > span > span").click()
        elif speed=="240":
            if self.find_element(By.ID,"_ctTS_olSpeedIx_rix_5").get_attribute("class")=='disabled':
                print("Predkosc niedostępna")
            else:
                self.find_element(By.CSS_SELECTOR,"#_ctTS_olSpeedIx_rix_5 > label > span > span").click()
        elif speed=="270":
            if self.find_element(By.ID,"_ctTS_olSpeedIx_rix_6").get_attribute("class")=='disabled':
                print("Predkosc niedostępna")
            else:
                self.find_element(By.CSS_SELECTOR,"#_ctTS_olSpeedIx_rix_6 > label > span > span").click()
        elif speed=="300":
            if self.find_element(By.ID,"_ctTS_olSpeedIx_rix_9").get_attribute("class")=='disabled':
                print("Predkosc niedostępna")
            else:
                self.find_element(By.CSS_SELECTOR,"#_ctTS_olSpeedIx_rix_9 > label > span > span").click()
        else:
            print("Predkosc niedostępna")
        agree_speed = self.find_element(By.ID,"_ctTS_olSpeedIx_lbAck0")
        agree_speed.click()
        time.sleep(2)

    def sort_by_popularity(self):
        sort_input = self.find_element(By.CSS_SELECTOR,"#_upTireLstSrt > div > div.sortOptions > div")
        sort_input.click()
        time.sleep(2)
        popularity_btn = self.find_element(By.ID,"_ctLstSrt_ctLstSrt_p0_ctLabelDesc")
        popularity_btn.click()
        time.sleep(2)

    def sort_by_price_desc(self):
        sort_input = self.find_element(By.CSS_SELECTOR,"#_upTireLstSrt > div > div.sortOptions > div")
        sort_input.click()
        time.sleep(2)
        price_btn = self.find_element(By.ID,"_ctLstSrt_ctLstSrt_p1_ctLabelDesc")
        price_btn.click()
        time.sleep(2)

    def sort_by_price_asc(self):
        sort_input = self.find_element(By.CSS_SELECTOR,"#_upTireLstSrt > div > div.sortOptions > div")
        sort_input.click()
        time.sleep(2)
        price_btn = self.find_element(By.ID,"_ctLstSrt_ctLstSrt_p1_ctLabelAsc")
        price_btn.click()
        time.sleep(2)

    def sort_by_evaluation(self):
        sort_input = self.find_element(By.CSS_SELECTOR,"#_upTireLstSrt > div > div.sortOptions > div")
        sort_input.click()
        time.sleep(2)
        evaluation_btn = self.find_element(By.ID,"_ctLstSrt_ctLstSrt_p2_ctLabelDesc")
        evaluation_btn.click()
        time.sleep(2)

    def get_products(self):
        tires_div = self.find_element(By.CSS_SELECTOR,"#_upTL > div > div")
        tires = tires_div.find_elements(By.CLASS_NAME, "product")
        data = []
        for tire in tires:
            name = tire.find_element(By.CLASS_NAME,"producerName").get_attribute("innerHTML")
            model = tire.find_element(By.CLASS_NAME,"modelName").get_attribute("innerHTML")
            note="0,0"
            if len(tire.find_elements(By.CLASS_NAME,"note"))>0:
                note = tire.find_element(By.CLASS_NAME,"note").get_attribute("innerHTML")
            price = tire.find_element(By.CLASS_NAME,"priceValue").get_attribute("innerHTML")
            data.append(
                {
                    'name': name,
                    'model': model,
                    "note" : note,
                    'price': price
                }
            )
        return data

    def get_products_with_higher_note(self,note:float):
        tires_div = self.find_element(By.CSS_SELECTOR,"#_upTL > div > div")
        tires = tires_div.find_elements(By.CLASS_NAME, "product")
        data = []
        for tire in tires:
            if len(tire.find_elements(By.CLASS_NAME,"note"))>0 and float(tire.find_element(By.CLASS_NAME,"note").get_attribute("innerHTML").replace(',','.'))>=note:
                name = tire.find_element(By.CLASS_NAME,"producerName").get_attribute("innerHTML")
                model = tire.find_element(By.CLASS_NAME,"modelName").get_attribute("innerHTML")
                noteInData = tire.find_element(By.CLASS_NAME,"note").get_attribute("innerHTML")
                price = tire.find_element(By.CLASS_NAME,"priceValue").get_attribute("innerHTML")
                data.append(
                    {
                        'name': name,
                        'model': model,
                        "note" : noteInData,
                        'price': price
                    }
                )
        return data
    
    def get_products_by_name(self,name_to_find):
        tires_div = self.find_element(By.CSS_SELECTOR,"#_upTL > div > div")
        tires = tires_div.find_elements(By.CLASS_NAME, "product")
        data = []
        for tire in tires:
            name = tire.find_element(By.CLASS_NAME,"producerName").get_attribute("innerHTML")
            model = tire.find_element(By.CLASS_NAME,"modelName").get_attribute("innerHTML")
            note="0,0"
            if len(tire.find_elements(By.CLASS_NAME,"note"))>0:
                note = tire.find_element(By.CLASS_NAME,"note").get_attribute("innerHTML")
            price = tire.find_element(By.CLASS_NAME,"priceValue").get_attribute("innerHTML")
            if name == name_to_find:
                data.append(
                    {
                        'name': name,
                        'model': model,
                        "note" : note,
                        'price': price
                    }
                )
        return data
    
    def get_products_by_model(self,model_to_find):
        tires_div = self.find_element(By.CSS_SELECTOR,"#_upTL > div > div")
        tires = tires_div.find_elements(By.CLASS_NAME, "product")
        data = []
        for tire in tires:
            name = tire.find_element(By.CLASS_NAME,"producerName").get_attribute("innerHTML")
            model = tire.find_element(By.CLASS_NAME,"modelName").get_attribute("innerHTML")
            note="0,0"
            if len(tire.find_elements(By.CLASS_NAME,"note"))>0:
                note = tire.find_element(By.CLASS_NAME,"note").get_attribute("innerHTML")
            price = tire.find_element(By.CLASS_NAME,"priceValue").get_attribute("innerHTML")
            if model == model_to_find:
                data.append(
                    {
                        'name': name,
                        'model': model,
                        "note" : note,
                        'price': price
                    }
                )
        return data
    
    def sleep_browser(self):
        time.sleep(10)