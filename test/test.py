from component.selenium import Selenium

my_selenium = Selenium(browser_type='firefox')
driver = my_selenium.driver
driver.get("http://www.baidu.com")
driver.close()
