# encoding : utf-8
# Author   : aka阿飞
# Datetime : 2021/8/8 19:33
# User     : AKA阿飞
# Product  : PyCharm
# Project  : pycharm
# File     : auto_add.py
# automatically add a file on the desktop
import os


def add_file(path):
    """
    检验 path 是否有存在
    有则返回字符串path
    反之创建并返回字符串path
    """
    if not os.path.exists(path):
        os.mkdir(path)
    return path
    
    
    
