##  多个装饰器，从上往下执行，最后执行函数本身，但是装饰过程是从下往上的
## 即，先执行createUI后执行createLi，但是，先执行li() 后执行ui
def createUl(func):
    print('create ui')
    def ui():
        return '<ui>' + func() + '</ui>'
    return ui

def createLi(func):
    print('create li')
    def li():
        return '<li>' + func() + '</li>'
    return li

@createUl
@createLi
def body():
    return 'aspire'

print(body())