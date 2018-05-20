class HeaderLocators(object):

    banner = '//*[@id="header"]/div[1]/div/div/a/img'
    phone_number = '//span[@class="shop-phone"]/strong'
    contact_us = '//div[@id="contact-link"]'
    sign_in = '//a[@class="login"]'
    logo = '//div[@id="header_logo"]/a/img[@class="logo img-responsive"]'
    search_input = '//input[@id="search_query_top"]'
    search_lup = '//button[@name="submit_search"]'
    cart = '//*[@title="View my shopping cart"]'

    category_women = '//*[@id="block_top_menu"]/ul/li[1]'
    category_women_tops = '//*[@id="block_top_menu"]/ul/li[1]/ul/li[1]/a'
    category_women_tshirts = '//*[@id="block_top_menu"]/ul/li[1]/ul/li[1]/ul/li[1]/a'
    category_women_blouses = '//*[@id="block_top_menu"]/ul/li[1]/ul/li[1]/ul/li[2]/a'
    category_women_dresses = '//*[@id="block_top_menu"]/ul/li[1]/ul/li[2]/a'
    category_women_casual_dresses = '//*[@id="block_top_menu"]/ul/li[1]/ul/li[2]/ul/li[1]/a'
    category_women_evening_dresses = '//*[@id="block_top_menu"]/ul/li[1]/ul/li[2]/ul/li[2]/a'
    category_women_summer_dresses = '//*[@id="block_top_menu"]/ul/li[1]/ul/li[2]/ul/li[3]/a'

    category_dresses = '//*[@id="block_top_menu"]/ul/li[2]'
    category_dresses_casual_dresses = '//*[@id="block_top_menu"]/ul/li[2]/ul/li[1]/a'
    category_dresses_evening_dresses = '//*[@id="block_top_menu"]/ul/li[2]/ul/li[2]/a'
    category_dresses_summer_dresses = '//*[@id="block_top_menu"]/ul/li[2]/ul/li[3]/a'

    category_tshirts = '//*[@id="block_top_menu"]/ul/li[3]'
