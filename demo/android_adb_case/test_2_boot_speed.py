from typing import re

from common.app_common.read_config import read_package_name, read_activity_name
from common.app_common.shell_boot_adb import get_cold_boot_time, get_hot_boot_time
from demo.my_test import *
import unittest

from utx import tag, Tag, log


class TestBootSpeed(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.boot_times = 2
        cls.app = '牛老幺'

    @tag(Tag.UI_F2)
    def test_run_boot(self):
        """冷启动和热启动的平均速度"""

        cold_time = []
        hot_time = []
        # 读取设备 id
        read_device_id = list(os.popen('adb devices').readlines())

        # 正则表达式匹配出 id 信息
        device_id = re.findall(r'^\w*\b', read_device_id[1])[0]
        package = read_package_name(self.app)
        activity = read_activity_name(self.app)

        for i in range(self.boot_times):
            cold_time.append(get_cold_boot_time(package, activity))
            hot_time.append(get_hot_boot_time(package, activity, device_id))
        res_cold_time = 0
        res_hot_time = 0
        print("冷启动时间 = " + str(cold_time))
        print("热启动时间 = " + str(hot_time))
        for i in cold_time:
            res_cold_time = res_cold_time + i
        log.info('平均冷启动时间: ' + str(res_hot_time / self.boot_times) + ' ms')
        for i in hot_time:
            res_hot_time = res_hot_time + i
        log.info('平均热启动时间: ' + str(res_hot_time / self.boot_times) + ' ms')


if __name__ == '__main__':
    unittest.main()
