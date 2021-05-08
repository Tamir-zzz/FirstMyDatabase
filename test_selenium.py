# coding = utf-8
from time import sleep
from selenium import webdriver
import pytest
# def test_o():
#     # 驱动文件路径
#     driverfile_path = r'D:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe'
#     # 启动浏览器
#     driver = webdriver.Chrome(executable_path=driverfile_path)
#     # 打开百度首页
#     driver.get(r'https://www.baidu.com/')
#     # 通过id定位搜索框，并输入selenium
#     driver.find_element_by_id('kw').send_keys('selenium')
#     driver.find_element_by_id('su').click()
#     #assert driver.find_element_by_id('kw').send_keys('selenium')
#     #assert driver.find_element_by_id('su').click()
#     # 等待5秒
#     sleep(5)
#     # 退出
#     driver.quit()
#     print("zhix")

driverfile_path = r'D:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe'
driver = webdriver.Chrome(executable_path=driverfile_path)
class TestCase():
    def setup_method(self):
        # 驱动文件路径
        # 启动浏览器
        # 打开百度首页
        driver.get(r'https://www.baidu.com/')
    def test_one(self):
        assert driver.find_element_by_id('kw').send_keys('selenium')
    def test_two(self):
        driver.find_element_by_id('kw').send_keys('selenium')
        assert driver.find_element_by_id('su').click()
    def test_three(self):
        assert driver.find_element_by_id('su').click()
    # def test_four(self):
    #     assert driver.find_element_by_name("title-content-title").click()
    # def test_five(self):
    #     return null
    # def test_six(self):
    #     return null
    
    def teardown_class(self):
        sleep(3)
        driver.quit()
