#!/usr/bin/env python
# _*_ encoding:utf-8 _*_
# 作者：王凯
# Date:2020/12/31:11:37

import unittest,time
from HTMLTestRunnerCN import HTMLTestRunner
# 定义测试用例的目录
test_dir='..\\UI_Automated_Test\\TestCase\\cg'
discover=unittest.defaultTestLoader.discover(test_dir,pattern='test*.py')
if __name__=='__main__':
    # 获取当前系统时间
    # now = time.strftime("%Y-%m-%d %H-%M-%S")
    # #定义报告文件格式
    # filename='./TestReport/' + now + '_web自动化测试报告.html'
    # #已写入模式打开报告文件
    # fb=open(filename,'wb')
    # #初始化一个HTMLTestRunner实例对象，用来生成报告
    # runner=HTMLTestRunner(stream=fb,title="游隼业务管理平台自动化测试报告",description="自动化测试用例执行情况：",verbosity=2)
    # 运行测试
    runner=unittest.TextTestRunner()
    runner.run(discover)
    # 关闭报告文件
    # fb.close()
