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


    bot.sleep_browser()