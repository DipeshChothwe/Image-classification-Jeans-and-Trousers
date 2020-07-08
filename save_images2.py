from selenium import webdriver
#from selenium.common.exceptions import StaleSeleniumReferenceException
from definations import scrap_image_url,save_images,make_directory,scrap_image_url_test

print("hi")

DRIVER_PATH = 'G:\FliproboAssgn\chromedriver_win32\Chromedriver.exe'
browser = webdriver.Chrome(executable_path = DRIVER_PATH)

data_use = 'Train'
DIRNAME = 'Trouser'
make_directory(data_use, DIRNAME)

#current_page_url = browser.get('https://www.flipkart.com/search?q=trouser&sid=clo%2Cvua%2Cmle%2Clhk&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_1_4_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_1_4_na_na_na&as-pos=1&as-type=RECENT&suggestionId=trouser%7CMen%27s+Trousers&requestId=7b2f2b33-baad-4618-b002-fe9e7336d193&as-searchtext=trou&page=1')
for page in range(1,4):
    url = "https://www.flipkart.com/search?q=trouser&sid=clo%2Cvua%2Cmle%2Clhk&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_1_4_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_1_4_na_na_na&as-pos=1&as-type=RECENT&suggestionId=trouser%7CMen%27s+Trousers&requestId=7b2f2b33-baad-4618-b002-fe9e7336d193&as-searchtext=trou&page={}". format(page)
    print(type(url))
    current_page_url = browser.get(url)
    product_details = scrap_image_url(driver = browser, page = page)
    page_number = browser.find_elements_by_xpath("//a[@class = '2Xp0TH fyt9Eu']")
    print("Scraped page", page_number)

    save_images(data = product_details, data_use = data_use, dirname = DIRNAME, page = page)
    print("saving images from page", page_number)

data_use = 'Train'
DIRNAME = 'Jeans'
make_directory(data_use, DIRNAME)

#current_page_url = browser.get('https://www.flipkart.com/search?q=trouser&sid=clo%2Cvua%2Cmle%2Clhk&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_1_4_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_1_4_na_na_na&as-pos=1&as-type=RECENT&suggestionId=trouser%7CMen%27s+Trousers&requestId=7b2f2b33-baad-4618-b002-fe9e7336d193&as-searchtext=trou&page=1')
for page in range(1,4):
    url = "https://www.flipkart.com/search?q=jeans&sid=clo%2Cvua%2Ck58%2Ci51&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_2_5_na_na_ps&otracker1=AS_QueryStore_OrganicAutoSuggest_2_5_na_na_ps&as-pos=2&as-type=RECENT&suggestionId=jeans%7CMen%27s+Jeans&requestId=13ea052c-796a-4e1f-9add-48e243689c50&as-searchtext=jeans&page={}". format(page)
    print(type(url))
    current_page_url = browser.get(url)
    product_details = scrap_image_url(driver = browser, page = page)
    page_number = browser.find_elements_by_xpath("//a[@class = '2Xp0TH fyt9Eu']")
    print("Scraped page", page_number)

    save_images(data = product_details, data_use = data_use, dirname = DIRNAME, page = page)
    print("saving images from page", page_number)


#For test dataset

data_use = 'Test'
DIRNAME = 'Trouser'
make_directory(data_use, DIRNAME)

#current_page_url = browser.get('https://www.flipkart.com/search?q=trouser&sid=clo%2Cvua%2Cmle%2Clhk&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_1_4_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_1_4_na_na_na&as-pos=1&as-type=RECENT&suggestionId=trouser%7CMen%27s+Trousers&requestId=7b2f2b33-baad-4618-b002-fe9e7336d193&as-searchtext=trou&page=1')
for page in range(5,6):
    url = "https://www.flipkart.com/search?q=trouser&sid=clo%2Cvua%2Cmle%2Clhk&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_1_4_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_1_4_na_na_na&as-pos=1&as-type=RECENT&suggestionId=trouser%7CMen%27s+Trousers&requestId=7b2f2b33-baad-4618-b002-fe9e7336d193&as-searchtext=trou&page={}". format(page)
    print(type(url))
    current_page_url = browser.get(url)
    product_details = scrap_image_url_test(driver = browser, page = page)
    page_number = browser.find_elements_by_xpath("//a[@class = '2Xp0TH fyt9Eu']")
    print("Scraped page", page_number)

    save_images(data = product_details, data_use = data_use, dirname = DIRNAME, page = page)
    print("saving images from page", page_number)

data_use = 'Test'
DIRNAME = 'Jeans'
make_directory(data_use, DIRNAME)

#current_page_url = browser.get('https://www.flipkart.com/search?q=trouser&sid=clo%2Cvua%2Cmle%2Clhk&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_1_4_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_1_4_na_na_na&as-pos=1&as-type=RECENT&suggestionId=trouser%7CMen%27s+Trousers&requestId=7b2f2b33-baad-4618-b002-fe9e7336d193&as-searchtext=trou&page=1')
for page in range(5,6):
    url = "https://www.flipkart.com/search?q=jeans&sid=clo%2Cvua%2Ck58%2Ci51&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_2_5_na_na_ps&otracker1=AS_QueryStore_OrganicAutoSuggest_2_5_na_na_ps&as-pos=2&as-type=RECENT&suggestionId=jeans%7CMen%27s+Jeans&requestId=13ea052c-796a-4e1f-9add-48e243689c50&as-searchtext=jeans&page={}". format(page)
    print(type(url))
    current_page_url = browser.get(url)
    product_details = scrap_image_url_test(driver = browser, page = page)
    page_number = browser.find_elements_by_xpath("//a[@class = '2Xp0TH fyt9Eu']")
    print("Scraped page", page_number)

    save_images(data = product_details, data_use = data_use, dirname = DIRNAME, page = page)
    print("saving images from page", page_number)
