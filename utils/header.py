#!/usr/bin/python3
# coding: utf-8
import random
from . import user_agents    #. 代表使用相对路径导入，即从当前项目中寻找需要导入的包或函数
def get_ua():
    #随机提取一个useragent
    return random.choice(user_agents)