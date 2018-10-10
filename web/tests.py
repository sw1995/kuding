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

#
# import socket
# host_name = socket.gethostname()
# # print(" Host name: %s" %host_name)
# print(" IP address: %s" %socket.gethostbyname(host_name))
# print(socket.gethostbyname(host_name))

# if (/ ^ (13[0-9] | 15[012356789] | 17[678] | 18[0-9] | 14[57])[0 - 9]{8}$ /.test(forget_account)) {
# else {
#             alert(1230);
#             $("[name='forget_account']").next("span").html("手机号码有误，请重新确认！");
#             setTimeout(function () {
#                 $("[name='forget_account']").next("span").html("");
#             }, 3000);
#         }
#     });
# $('.t_info_detail').parent().prevAll().each(function()
# {
#     var
# v = $(this).html();
# console.log(v);
# var
# n = $(this).attr('sxy');
# console.log(n);
#
#
#
# $("#s_t_info input[name='" + n + "']").val(v)
# })


# < !-- 遮罩层 -->
# < div
#
#
# class ="s_shadow" > < / div >

#
# $('.t_info_detail').on('click', function()
# {
# $(".s_t_info").css("display", "block");
# var
# t_account = $("[sxy='t_account']").text();
# console.log(t_account);
# $.ajax({
#     url: '/t_info_detail/',
#     type: "post",
#     data: {
#         t_account: t_account,
#         csrfmiddlewaretoken: $("[name='csrfmiddlewaretoken']").val()
# },
# success: function(data)
# {
#     console.log(data)
# }
# })
#
# });

# <li {% if request.path == "/man/" %}class="action"{% endif %}>
#                      <a href="">
#                          <p><svg class="icon" style="font-size: 35px" aria-hidden="true">
#                                   <use xlink:href="#icon-shoucang"></use>
#                             </svg>
#                          </p>
#                          <p style="color: black;">试题管理</p>
#                      </a>
#                  </li>


# {% for s_l_state in s_l_state_obj %}
#                             {% if l_state.s_state == "0" or s_l_state == "1" %}
#                                 <i class="fa fa-circle" aria-hidden="true" style="color: red;"></i>
#                             {% endif %}
#                          {% endfor %}
