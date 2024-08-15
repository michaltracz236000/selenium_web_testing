from oponeo.oponeo import Oponeo

with Oponeo() as bot:
    bot.load_page()
    bot.decline_cookies()
    bot.choose_size('215','55','17')
    bot.click_choose_class()
    bot.select_economic()
    bot.select_middle()
    bot.select_premium()

    bot.sleep_browser()