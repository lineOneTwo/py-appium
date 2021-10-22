from  time import sleep
from appium import webdriver


class testLogin():
    def setup(self):
        self.desire_cap={
            "platformName": "Android",
            "platformVersion": "7.1.2",
            "deviceName": "emulator-5554",
            "appPackage": "uni.UNI25A295E",
            "appActivity": "io.dcloud.PandoraEntryActivity"
        }
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", self.desire_cap)
        self.driver.implicitly_wait(5)
        print("23")

    def test_login(self):
        """
        输入账号密码后登录
        :return:
        """
        pass



if __name__ == '__main__':
    testLogin()