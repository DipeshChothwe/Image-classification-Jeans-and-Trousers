from selenium import webdriver
#from selenium.common.exceptions import StaleSeleniumReferenceException
from definations import scrap_image_url,save_images,make_directory

print("hi")

DRIVER_PATH = 'G:\FliproboAssgn\chromedriver_win32\Chromedriver.exe'
browser = webdriver.Chrome(executable_path = DRIVER_PATH)



current_page_url = browser.get('https://www.flipkart.com/search?q=trouser&sid=clo%2Cvua%2Cmle%2Clhk&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_1_4_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_1_4_na_na_na&as-pos=1&as-type=RECENT&suggestionId=trouser%7CMen%27s+Trousers&requestId=7b2f2b33-baad-4618-b002-fe9e7336d193&as-searchtext=trou&page=1')

data_use = 'Train'
DIRNAME = 'Trouser'
make_directory(data_use,DIRNAME)

start_page = 1
last_page = 3

for page in range(start_page, last_page+1):
  
    product_details = scrap_image_url(driver = browser, page=page)
    page_number = browser.find_elements_by_xpath("//a[@class = '2Xp0TH fyt9Eu']")
    print("Scraped page", page_number)

    save_images(data = product_details, data_use= data_use, dirname = DIRNAME, page = page)
    print("saving images from page", page_number)


    
    print("Moving to next page")
    #getElement(By.xpath(Next)).click()
    print(browser.find_elements_by_xpath("//a[@class='_3fVaIS']//span"))
    button_selection = browser.find_elements_by_xpath("//div[@class='_2zg3yZ']//a[@class='_3fVaIS']//span").get_attribute('innerHTML')
    #button_selection = browser.find_elements_by_xpath("//a[@class='_3fVaIS']//span").text
    print(button_selection)
    print(browser.find_elements_by_xpath("//a[@class = '_3fVaIS']"))
    if button_selection == Next:
        browser.find_elements_by_xpath("//a[@class = '_3fVaIS']").click()
    else:
        browser.find_elements_by_xpath("//a[@class = '_3fVaIS'][2]").click()

    new_page = browser.find_elements_by_xpath("//a[@class = '2Xp0TH fyt9Eu']")
    print("Moving on to page number ", new_page)
    
