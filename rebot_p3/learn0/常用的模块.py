
# builtins 内建默认函数
# os
# sys
# functools
# json
#logging
#multiprocessing
#threading
#copy
#time
#datatime
#calendar
#hashlib
#random
#re
#socket
#shuitl
#glob

import hashlib

m = hashlib.md5()
print(m)
m.update(b'abcd')
print(m.hexdigest())