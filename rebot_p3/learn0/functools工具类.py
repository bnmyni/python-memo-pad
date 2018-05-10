import  functools

def note(func):
    '''note function'''
    @functools.wraps(func)
    def test():
        '''test function'''
        return func()
    return test

@note
def use():
    '''use function'''
    print('-'* 5)

## 注意，如果在上面的代码中不加上  @functools.wraps(func) 那么看到的内容就是test的注释了
print(help(use))