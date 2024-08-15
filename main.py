from oponeo.oponeo import Oponeo
import unittest

# with Oponeo() as bot:
#     bot.load_page()
#     bot.decline_cookies()
#     bot.choose_size('215','55','17')
#     bot.click_choose_class()
#     bot.select_premium()
#     bot.agree_select_tire_class()
#     bot.click_choose_type()
#     bot.select_winter_type()
#     bot.agree_select_tire_type()
#     bot.search_tires()
    # bot.tire_price("300","800")
    # bot.select_speed("210")
    # bot.sort_by_popularity()
    # bot.sort_by_price_desc()
    # bot.sort_by_price_asc()
    # bot.sort_by_evaluation()
    # data = bot.get_products()
    # for i in data:
    #         print("Name: " + i['name'])
    #         print("Model: " + i['model'])
    #         print("Note: " + i['note'])
    #         print("Price: " + i['price']+"zł/szt")
    #         print()
    # data = bot.get_products_with_higher_note(4.7)
    # for i in data:
    #         print("Name: " + i['name'])
    #         print("Model: " + i['model'])
    #         print("Note: " + i['note'])
    #         print("Price: " + i['price']+"zł/szt")
    #         print()
    # data = bot.get_products_by_name("Nokian Tyres")
    # for i in data:
    #         print("Name: " + i['name'])
    #         print("Model: " + i['model'])
    #         print("Note: " + i['note'])
    #         print("Price: " + i['price']+"zł/szt")
    #         print()
    # data = bot.get_products_by_model("Blizzak LM005")
    # for i in data:
    #         print("Name: " + i['name'])
    #         print("Model: " + i['model'])
    #         print("Note: " + i['note'])
    #         print("Price: " + i['price']+"zł/szt")
    #         print()


class TestDodawania(unittest.TestCase):
    def setUp(self):
        self.oponeo = Oponeo()
        self.oponeo.load_page()
        self.oponeo.decline_cookies()
        self.oponeo.choose_size('215','55','17')
        self.oponeo.click_choose_class()
        self.oponeo.select_premium()
        self.oponeo.agree_select_tire_class()
        self.oponeo.click_choose_type()
        self.oponeo.select_winter_type()
        self.oponeo.agree_select_tire_type()
        self.oponeo.search_tires()

    def test_dodaj_liczby(self):
        data = self.oponeo.get_products_by_name("Nokian Tyres")
        self.assertGreater(len(data),0)

    def test_dodaj_bledny_typ(self):
        data = self.oponeo.get_products_by_name("Nexen")
        self.assertGreater(len(data),0)
        

if __name__ == '__main__':
    unittest.main()