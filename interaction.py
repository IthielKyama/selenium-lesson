from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://secure-retreat-92358.herokuapp.com/")

# article_count = driver.find_element(By.XPATH, '//*[@id="articlecount"]/a[1]')
# # article_count.click()
#
# all_portals = driver.find_element(By.LINK_TEXT, "Content portals")
# # all_portals.click()

# search_icon = driver.find_element(By.XPATH, '//*[@id="p-search"]/a/span[1]')
# search_icon.click()
# search = driver.find_element(By.NAME, "search")
# search.send_keys("Python", Keys.ENTER)

first_name = driver.find_element(By.NAME, "fName")
first_name.send_keys("Ithiel")
last_name = driver.find_element(By.NAME, "lName")
last_name.send_keys("Ithiel")
email = driver.find_element(By.NAME, "email")
email.send_keys("kyamanyaga@email.com")
submit = driver.find_element(By.XPATH, '/html/body/form/button')
submit.click()


















