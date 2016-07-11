# /user/bin/env python          #(1) 起始行  调用脚本时 不用调用解释器 直接输入脚本名来运行

"this is a test module"         #(2)模块文档 文档字符串

import sys
import os                       #(3) 模块导入

debug =True                     #(4)(全局变量) 变量定义


class FooClass(object):         #(5) 类定义（若有）
    "Foo class"
    pass

def text():                     #(6)函数定义（若有）
    "test function"
    foo = Fooclass()

    if debug:
        print "ran text()"


if __name__ == '__main__':      #(7)主程序
    test()
