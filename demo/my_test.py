from sympy.logic.utilities import load_file

from common.app_common.element_action import *

# 用户信息
user=read_ini(ini_file_path=load_file('parameter'),name='用户',value='user_2')
password=read_ini(ini_file_path=load_file('parameter'),name='用户',value='password_2')
#app信息
app_name=read_ini(ini_file_path=load_file('app_conf'),name='掌上平城',value='appName')

#元素类型
id_type='id_type'
class_name_ini='class_name_ini'
location_type='location_type'
xpath_type='xpath_type'
