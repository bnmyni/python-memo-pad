# -*- coding: utf-8 -*-
## __main__使用及模块路径搜索和修改

import  sys
## 输出path的搜索路径
print(sys.path)

## 修改模块搜索路径
# sys.path.append('aaa')

# 分包管理模块
# 1.编码模块代码，新建一个文件夹
# 2.在文件夹中创建一个空的__init__,py文件
# 3.将相关的模块放入到文件夹中
# 调用方式  import 包名.模块名