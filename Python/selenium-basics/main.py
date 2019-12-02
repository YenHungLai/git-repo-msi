from selenium.webdriver import Chrome

driver = Chrome('C:/Users/Jacob/Downloads/chromedriver.exe')

driver.get("https://www.youtube.com/")

driver.find_element_by_css_selector('a[id="click-target"]').click()