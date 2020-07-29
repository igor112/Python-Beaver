from beaver import RBCBank

bank = beaver.RBCBank()

transactions = bank.screen_scrape_transactions(
    '01234567890123', '123456', '', 'web.mobile@com'
)