from oponeo.oponeo import Oponeo

with Oponeo() as bot:
    bot.load_page()
    bot.decline_cookies()
    bot.choose_size('235','55','17')

    bot.sleep_browser()