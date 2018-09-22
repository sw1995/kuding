# # # from django.test import TestCase
# # #
# # # # Create your tests here.
# # #
# import time
#
# t = time.localtime(1536570822)
#
# print(time.strftime("%Y-%m-%d %H:%M:%S", t))
#
# t1 = time.time()
# print(t1)


# #
# #
# # # student_list = [("123456789123",'1321','1231')]
# # #
# # # for i in student_list:
# # #     print(i)
# # #     for x in i:
# # #         print(x)
# #
# #
# import urllib, json, urllib.request
# import random


# def get_data(self,mobile,tpl_value):
#     l = []
#     for i in range(6):
#         l.append(random.randint(0, 9))
#     mobile = "".join([str(l[i]) + str(l[i + 1]) for i in range(0, len(l), 2)])
#     self.mobile = mobile
#     self.tpl_value = tpl_value

# get_data()


#
#
# def main():
#     l = []
#     for i in range(6):
#         l.append(random.randint(0, 9))
#     code = "".join([str(l[i]) + str(l[i + 1]) for i in range(0, len(l), 2)])
#     appkey = '337b85164bdc1bfd18b111a17b5a3478'  # 您申请的短信服务appkey
#     mobile = '{}'.format(account)  # 短信接受者的手机号码
#     tpl_id = '102599'  # 申请的短信模板ID,根据实际情况修改
#     tpl_value = '#code#={}&#company#=麒麟信息'.format(code)  # 短信模板变量,根据实际情况修改
#
#     sendsms(appkey, mobile, tpl_id, tpl_value)  # 请求发送短信
#
#
# def sendsms(appkey, mobile, tpl_id, tpl_value):
#     sendurl = 'http://v.juhe.cn/sms/send'  # 短信发送的URL,无需修改
#
#     params = 'key=%s&mobile=%s&tpl_id=%s&tpl_value=%s' % \
#              (appkey, mobile, tpl_id, 	urllib.parse.quote(tpl_value))  # 组合参数
#
#     wp = urllib.request.urlopen(sendurl + "?" + params)
#     content = wp.read()  # 获取接口返回内容
#
#     result = json.loads(content)
#
#     if result:
#         error_code = result['error_code']
#         if error_code == 0:
#             # 发送成功
#             smsid = result['result']['sid']
#             print("sendsms success,smsid: %s" % (smsid))
#         else:
#             # 发送失败
#             print("sendsms error :(%s) %s" % (error_code, result['reason']))
#     else:
#         # 请求失败
#         print("request sendsms error")
#
# if __name__ == '__main__':
#     main()


# import uuid
# s_uuid = str(uuid.uuid1())
# l_uuid=s_uuid.split('-')
# s_id=''.join(l_uuid)
# print(s_uuid)

# import time
#
# print(int(time.time()))
