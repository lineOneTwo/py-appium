from appium.webdriver.common.touch_action import TouchAction

from common.app_common.element_action import *
from common.app_common.shell_boot_adb import *
from common.app_common.session import *


class BasePage():
    def __init__(self, driver):
        self.driver = driver

    def login_base(self, user_number, password):
        time.sleep(1)
        log.info("开始执行登录操作")
        log.info("----" * 15)
        # clicking(driver=self.driver, type='id_type', section_name='登录', name='手机号')
        inputting(driver=self.driver, type='id_type', section_name='登录', name='手机号', txt=user_number)
        log.info("输入账号")
        # clicking(driver=self.driver, type='id_type', section_name='登录', name='密码')
        inputting(driver=self.driver, type='id_type', section_name='登录', name='密码' , txt=password)
        log.info("输入密码")
        clicking(driver=self.driver, type='id_type', section_name='登录', name='登录按钮')
        log.info("点击登录")
        # time.sleep(10)
        # TouchAction(driver=self.driver).tap(x=98,y=409).perform()
        # #clicking(driver=self.driver, type='location_type', section_name='选择岗位', name='岗位')
        # clicking(driver=self.driver, type='id_type', section_name='选择岗位', name='确定')

    def registry(self):
        clicking(driver=self.driver,type='id_type',section_name='注册',name='注册')

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

    def reset_password(self):
        time.sleep(3)
        log.info("找回密码")
        clicking(driver=self.driver,type='id_type',section_name='找回密码',name='找回')