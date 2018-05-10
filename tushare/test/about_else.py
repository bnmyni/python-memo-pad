# -*- coding: utf-8 -*-
## else 配合
def else_while(a):
    total = 0
    i = 1
    while a > i:
        total += a
        i += 1
    else:
        print('total:', total)

def else_except():
    try:
        print('hello')
    except:
        print('sorry')
    else:
        print('good')

else_except()