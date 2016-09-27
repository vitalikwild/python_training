# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.common.action_chains import ActionChains
import time, unittest

def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False

class test_add_community(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)
    
    def test_(self):
        success = True
        wd = self.wd
        wd.get("http://cms.oneday.com/Account/Login?returnUrl=%2F")
        wd.find_element_by_id("Email").click()
        wd.find_element_by_id("Email").send_keys("\\undefined")
        wd.find_element_by_id("Password").click()
        wd.find_element_by_id("Password").send_keys("\\undefined")
        wd.find_element_by_id("Email").click()
        wd.find_element_by_id("Email").click()
        wd.find_element_by_id("Email").clear()
        wd.find_element_by_id("Email").send_keys("jdineshk@gmail.com")
        wd.find_element_by_id("Password").click()
        wd.find_element_by_id("Password").click()
        wd.find_element_by_id("Password").clear()
        wd.find_element_by_id("Password").send_keys()
        wd.find_element_by_id("Password").click()
        wd.find_element_by_id("Password").clear()
        wd.find_element_by_id("Password").send_keys("brookdale2016")
        wd.find_element_by_xpath("//div[@id='wrapper']//button[.='Log In']").click()
        wd.find_element_by_link_text("Santa Clara University").click()
        wd.find_element_by_xpath("//div[@id='body']/section/section/div[4]/div[1]/div[2]/button").click()
        wd.find_element_by_xpath("//div[@id='body']/section/section/div[3]/div[2]/div[1]/div[1]/input[1]").click()
        wd.find_element_by_xpath("//div[@id='body']/section/section/div[3]/div[2]/div[1]/div[1]/input[1]").clear()
        wd.find_element_by_xpath("//div[@id='body']/section/section/div[3]/div[2]/div[1]/div[1]/input[1]").send_keys("Test 1")
        wd.find_element_by_xpath("//div[@id='body']/section/section/div[3]/div[2]/div[1]/div[1]/input[2]").click()
        wd.find_element_by_xpath("//div[@id='body']/section/section/div[3]/div[2]/div[1]/div[1]/input[2]").clear()
        wd.find_element_by_xpath("//div[@id='body']/section/section/div[3]/div[2]/div[1]/div[1]/input[2]").send_keys("google.com")
        wd.find_element_by_xpath("//div[@id='body']/section/section/div[3]/div[2]/div[1]/div[1]/input[3]").click()
        wd.find_element_by_xpath("//div[@id='body']/section/section/div[3]/div[2]/div[1]/div[1]/input[3]").clear()
        wd.find_element_by_xpath("//div[@id='body']/section/section/div[3]/div[2]/div[1]/div[1]/input[3]").send_keys("adress")
        wd.find_element_by_xpath("//div[@id='body']/section/section/div[3]/div[2]/div[1]/div[1]/input[4]").click()
        wd.find_element_by_xpath("//div[@id='body']/section/section/div[3]/div[2]/div[1]/div[1]/input[4]").clear()
        wd.find_element_by_xpath("//div[@id='body']/section/section/div[3]/div[2]/div[1]/div[1]/input[4]").send_keys("123444")
        wd.find_element_by_xpath("//div[@id='body']/section/section/div[3]/div[2]/div[3]/div[1]/div[3]/i").click()
        wd.find_element_by_xpath("//div[@id='body']/section/section/div[3]/div[2]/div[3]/div[1]/div[3]/i/input").click()
        wd.find_element_by_xpath("//div[@id='body']/section/section/div[3]/div[2]").click()
        wd.find_element_by_xpath("//div[@id='body']/section/section/div[3]/div[1]/div[2]/button[2]").click()
        wd.find_element_by_link_text("Test 1").click()
        wd.find_element_by_link_text("Sign Out").click()
        self.assertTrue(success)
    
    def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()
