# /user/bin/env python          #(1) ��ʼ��  ���ýű�ʱ ���õ��ý����� ֱ������ű���������

"this is a test module"         #(2)ģ���ĵ� �ĵ��ַ���

import sys
import os                       #(3) ģ�鵼��

debug =True                     #(4)(ȫ�ֱ���) ��������


class FooClass(object):         #(5) �ඨ�壨���У�
    "Foo class"
    pass

def text():                     #(6)�������壨���У�
    "test function"
    foo = Fooclass()

    if debug:
        print "ran text()"


if __name__ == '__main__':      #(7)������
    test()
