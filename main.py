from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://python.org")

TIME_XPATH = '//*[@id="content"]/div/section/div[2]/div[2]/div/ul/'
NAME_XPATH = '//*[@id="content"]/div/section/div[2]/div[2]/div/ul/'

upcoming_events = {}

for item in range(5):
    upcoming_events[item] = {
        'time': driver.find_element(By.XPATH, f'{TIME_XPATH}li[{item + 1}]/time').text,
        'name': driver.find_element(By.XPATH, f'{NAME_XPATH}li[{item + 1}]/a').text
    }

print(upcoming_events)

driver.quit()
# price_dollar = driver.find_element(By.CLASS_NAME, "a-price-whole")
# price_cents = driver.find_element(By.CLASS_NAME, "a-price-fraction")
# print(f"The price is {price_dollar.text}.{price_cents.text}")

# search_bar = driver.find_element(By.NAME, value="q")
# print(search_bar.get_attribute("placeholder"))
# button = driver.find_element(By.ID, value="submit")
# print(button.size)
# documentation_link = driver.find_element(By.CSS_SELECTOR, value=".documentation-widget a")
# print(documentation_link.text)

# bug_link = driver.find_element(By.TIME_XPATH, value='//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
# print(bug_link.text)




