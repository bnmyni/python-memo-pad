
import hashlib

m = hashlib.md5()
## r'aaa'
## byte('aaaa', 'utf-8')
## 'aaaa'.encode('utf-8')
m.update('fffff'.encode())
rst = m.hexdigest()
print(rst)