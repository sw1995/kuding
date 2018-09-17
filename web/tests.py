from django.test import TestCase

# Create your tests here.

import time

t = time.localtime(1536570882456/1000)

print(time.strftime("%Y-%m-%d %H:%M:%S", t))

t1 = time.time()
print(t1)


# student_list = [("123456789123",'1321','1231')]
#
# for i in student_list:
#     print(i)
#     for x in i:
#         print(x)