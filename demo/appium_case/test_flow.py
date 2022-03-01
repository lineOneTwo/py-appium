import unittest

from demo.my_test import *
from demo.appium_case.basepage import *
from utx import skip, tag, Tag


class TestAboutAddEvent(unittest.TestCase):
    """
    用户登录
    添加事件
    """

    @classmethod
    def setUpClass(cls):  # setUpClass所有用例开始前执行一遍，但是必须使用类函数装饰器
        cls.driver = driver_begin(app_name)
        log.debug("初始化APP，测试数据初始化")

    @skip
    @tag(Tag.UI_F1)
    def test_skip_shuffling(self):
        """跳过轮播图"""
        time.sleep(1)
        BasePage(driver=self.driver).skip_shuffling()

    @skip
    @tag(Tag.UI_F1)
    def test_skip_agreement(self):
        """同意协议"""
        time.sleep(1)
        BasePage(driver=self.driver).skip_agreement()
        time.sleep(10)

    # @skip
    @tag(Tag.UI_F1)
    def test_login(self):
        """登录"""
        BasePage(driver=self.driver).login_base(user_number=user,password=password)
    # <appium.webdriver.webdriver.WebDriver (session="60010865-521c-4169-922c-51be57a3bfbe")>

    @tag(Tag.UI_F1)
    def test_add_event(self):
        """添加事件"""
        BasePage(driver=self.driver).add_event()

    @skip
    @tag(Tag.UI_F1)
    def test_registry(self):
        """点击注册按钮"""
        BasePage(driver=self.driver).registry()

    @skip
    @tag(Tag.UI_F1)
    def test_skip_limits(self):
        """第一次进入APP的权限弹窗"""
        time.sleep(1)
        BasePage(driver=self.driver).skip_limits()

    @skip
    @tag(Tag.UI_F1)
    def test_reset_password(self):
        """找回密码"""
        time.sleep(1)
        BasePage(driver=self.driver).reset_password()

    @skip
    @tag(Tag.UI_F1)
    def test_send_massage(self):
        """发送消息给好友"""
        log.debug("进入通讯录")
        clicking(driver=self.driver, type=id_type, section_name='导航', name='通讯录')
        log.debug("找到李飞")
        clicking(driver=self.driver, type=xpath_type, section_name='通讯录', name='李飞')
        log.info("准备发送100条消息")
        clicking(driver=self.driver, type=id_type, section_name='好友', name='发送消息')
        for i in range(100):
            inputting(driver=self.driver, type=id_type, section_name='好友', name='消息输入框', txt='你好')
            clicking(driver=self.driver, type=id_type, section_name='好友', name='发送按钮')
            log.info("发送第" + str(i + 1) + "成功，发送消息内容“你好”")



if __name__ == '__main__':
    unittest.main()