import time
import unittest
import warnings

from common.app_common.element_action import *
from utx import *
from common.app_common.read_config import *
from common.app_common.shell_install_adb import *
from common.app_common.shell_boot_adb import *
from common.app_common.session import *
from common.app_common.shell_monkey_adb import *


class BasePage():
    def __init__(self, driver):
        self.driver = driver

    def login_base(self, user_number, password):
        time.sleep(1)
        log.info("开始执行登录操作")
        log.info("----" * 15)
        inputting(driver=self.driver, type='id_type', section_name='登录', name='账号', txt=user_number)
        log.info("输入账号")
        inputting(driver=self.driver, type='id_type', section_name='登录', name='密码' , txt=password)
        log.info("输入密码")
        clicking(driver=self.driver, type='id_type', section_name='登录', name='登录按钮')
        log.info("点击登录")

    def skip_shuffling(self):
        log.info("跳过轮播图")
        clicking(driver=self.driver, type='id_type', section_name='轮播图', name='跳过')

    def skip_agreement(self):
        log.info("同意隐私协议")
        clicking(driver=self.driver, type='id_type', section_name='协议', name='同意')

    def skip_limits(self):
        time.sleep(3)
        log.info("操作权限弹窗二次")
        for i in range(5):
            clicking(driver=self.driver, type='id_type', section_name='权限', name='允许')
            time.sleep(1.5)
