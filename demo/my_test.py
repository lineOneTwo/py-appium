from sympy.logic.utilities import load_file

from common.app_common.element_action import *

# 用户信息
user_1=read_ini(ini_file_path=load_file('parameter'),name='用户',value='user_1')
password=read_ini(ini_file_path=load_file('parameter'),name='用户',value='password')
#app信息
app_name_JSC=read_ini(ini_file_path=load_file('app_conf'),name='领导驾驶舱',value='appName')

#元素类型
id_type='id_type'
class_name_ini='class_name_ini'
location_type='location_type'
xpath_type='xpath_type'
