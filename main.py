from oponeo.oponeo import Oponeo

with Oponeo() as bot:
    bot.load_page()
    bot.decline_cookies()
    bot.choose_size('215','55','17')
    bot.click_choose_class()
    bot.select_premium()
    bot.agree_select_tire_class()
    bot.click_choose_type()
    bot.select_winter_type()
    bot.agree_select_tire_type()
    bot.search_tires()
    # bot.tire_price("300","800")
    # bot.select_speed("210")
    # bot.sort_by_popularity()
    # bot.sort_by_price_desc()
    # bot.sort_by_price_asc()
    # bot.sort_by_evaluation()
    bot.get_products()


    bot.sleep_browser()

