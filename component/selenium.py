import os

from selenium import webdriver

from component import path


class Selenium(object):
    def __init__(self, browser_type='ie'):
        if 'ie' == browser_type:
            selenium_driver_name = 'IEDriverServer.exe'
            self.driver = webdriver.Ie(
                os.path.join(path.find_third_party_path(), 'web_driver', browser_type, selenium_driver_name))
        elif 'chrome' == browser_type:
            selenium_driver_name = 'chromedriver.exe'
            self.driver = webdriver.Chrome(
                os.path.join(path.find_third_party_path(), 'web_driver', browser_type, selenium_driver_name))
        elif 'firefox' == browser_type:
            selenium_driver_name = 'geckodriver.exe'
            self.driver = webdriver.Firefox(
                os.path.join(path.find_third_party_path(), 'web_driver', browser_type, selenium_driver_name))
        else:
            raise Exception('the target browser type(%s) was not support' % browser_type)
