from selenium.webdriver.support.wait import WebDriverWait
from common.app_common.read_config import read_ini
from config.load_file import *


def exist(driver, ini_file_path, name, value):  # 判断是否存在此元素
    """ini_name:配置文件的路径"""
    ele = read_ini(ini_file_path=ini_file_path, name=name, value=value)
    source = driver.section_name_source
    if ele in source:
        return True
    else:
        return False


def looking_for_element(driver, type, section_name, name):  # 根据元素类型进行不同的元素定位
    """elements_name:元素类型"""
    try:
        if type == 'class_name_type':  # class_name
            the_name = read_ini(ini_file_path=load_file('class_name_ini'), name=section_name, value=name)
            print(the_name)
            return WebDriverWait(driver, 30).until(lambda x: x.find_element_by_class_name(the_name))
        if type == 'id_type':  # id
            the_name1 = read_ini(ini_file_path=load_file('id_ini'), name=section_name, value=name)
            return WebDriverWait(driver, 30).until(lambda x: x.find_element_by_id(the_name1))
        if type == 'location_type':  # tap
            the_name2 = read_ini(ini_file_path=load_file('location_ini'), name=section_name, value=name)
            return WebDriverWait(driver, 30).until(lambda x: x.tap(list(the_name2), 1000))
        if type == 'xpath_type':  # xpath
            the_name4 = read_ini(ini_file_path=load_file('xpath_ini'), name=section_name, value=name)
            print(the_name4)
            return WebDriverWait(driver, 25).until(lambda x: x.find_element_by_xpath(the_name4))
        if type == 'text_type':  # text
            the_name5 = read_ini(ini_file_path=load_file('text_ini'), name=section_name, value=name)
            return WebDriverWait(driver, 25).until(lambda x: x.find_element_by_link_text(the_name5))
    except TypeError:
        print("抱歉，找不到元素")
    except TimeoutError:
        print("超时，请检查代码")


def clicking(driver, type, section_name, name):  # 点击
    looking_for_element(driver=driver, type=type, section_name=section_name, name=name).click()


def inputting(driver, type, section_name, name, txt):  # 输入内容
    looking_for_element(driver=driver, type=type, section_name=section_name, name=name).send_keys(txt)
    print("输入")

def taping(driver, type, section_name, name):  # 点击
    looking_for_element(driver=driver, type=type, section_name=section_name, name=name)
