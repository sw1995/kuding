from django.shortcuts import render, HttpResponse, redirect, HttpResponseRedirect
from django.http import JsonResponse
from web.form.student import Student_to_teacher
from web.form.reg import RegForm
# from web.form import reg
from article.models import TArticles
from web.models import WebTeacher, WebStudent, WebGrant, WebDetail, WebCourse, WebEvaluate, WebLogsheet, WebClasses, \
    WebRelation
from web.form.login_form import LoginForm


# 获取ip
def get_ip():
    import socket
    host_name = socket.gethostname()
    # print(" Host name: %s" %host_name)
    # print(" IP address: %s" % socket.gethostbyname(host_name))
    ip_address = socket.gethostbyname(host_name)
    return ip_address


# 生成uuid
def create_uuid():
    import uuid
    s_uuid = str(uuid.uuid1())
    l_uuid = s_uuid.split('-')
    uid = ''.join(l_uuid)
    return uid


# 首页
def index(request):

    article_list = TArticles.objects.using("articles").all().order_by("-t_createtime")
    article_list2 = []

    if len(article_list) > 3:
        article_list2.append(article_list[0])
        article_list2.append(article_list[1])
        article_list2.append(article_list[2])
    else:
        article_list2 = article_list

    loginForm = LoginForm()
    reg = RegForm()

    tea_list2 = []
    tea_list = WebTeacher.objects.all().order_by("-t_create_time")
    if len(tea_list) > 3:
        tea_list2.append(tea_list[0])
        tea_list2.append(tea_list[1])
        tea_list2.append(tea_list[2])
    else:
        tea_list2 = tea_list

    account = request.session.get("account")
    role = request.session.get("role")
    if account:
        if role == "student":
            stu_obj = WebStudent.objects.filter(s_account=account).first()
        else:
            tea_obj = WebTeacher.objects.filter(t_account=account).first()
    return render(request, 'index.html', locals())


def stu_show(request):
    loginForm = LoginForm()
    reg = RegForm()
    account = request.session.get("account")
    role = request.session.get("role")
    if account:
        if role == "student":
            stu_obj = WebStudent.objects.filter(s_account=account).first()
        else:
            tea_obj = WebTeacher.objects.filter(t_account=account).first()
    return render(request, 'stu_show.html', locals())


def Teachers_lineup(request):
    loginForm = LoginForm()
    reg = RegForm()
    account = request.session.get("account")
    role = request.session.get("role")
    if account:
        if role == "student":
            stu_obj = WebStudent.objects.filter(s_account=account).first()
        else:
            tea_obj = WebTeacher.objects.filter(t_account=account).first()

    tea_list = WebTeacher.objects.all()
    tea_list2 = []
    # print(len(tea_list))
    if len(tea_list) > 3:
        tea_list2.append(tea_list[0])
        tea_list2.append(tea_list[1])
        tea_list2.append(tea_list[2])
    else:
        tea_list2 = tea_list
    return render(request, 'Teachers_lineup.html', locals())


def contact(request):
    loginForm = LoginForm()
    reg = RegForm()
    account = request.session.get("account")
    role = request.session.get("role")
    if account:
        if role == "student":
            stu_obj = WebStudent.objects.filter(s_account=account).first()
        else:
            tea_obj = WebTeacher.objects.filter(t_account=account).first()
    return render(request, 'contact.html', locals())


def news(request):
    loginForm = LoginForm()
    reg = RegForm()
    account = request.session.get("account")
    role = request.session.get("role")
    if account:
        if role == "student":
            stu_obj = WebStudent.objects.filter(s_account=account).first()
        else:
            tea_obj = WebTeacher.objects.filter(t_account=account).first()
    return render(request, 'news.html', locals())


def class_type(request):
    loginForm = LoginForm()
    reg = RegForm()
    account = request.session.get("account")
    role = request.session.get("role")
    if account:
        if role == "student":
            stu_obj = WebStudent.objects.filter(s_account=account).first()
        else:
            tea_obj = WebTeacher.objects.filter(t_account=account).first()
    return render(request, 'class_type.html', locals())


# 登陆
# from django.views.decorators.csrf import csrf_exempt
# @csrf_exempt
def login(request):
    ret = {}
    if request.method == "POST":
        form_obj = LoginForm(request.POST)
        if form_obj.is_valid():
            account = request.POST.get("log_account")
            password = request.POST.get("log_password")
            role = request.POST.get("log_role")
            if role == "1":
                stu_obj = WebStudent.objects.filter(s_account=account, s_password=password).first()
                if stu_obj:
                    # 确认学生账号存在
                    if stu_obj.s_state == 1:
                        request.session["account"] = account
                        ret["s_id"] = stu_obj.s_id
                        request.session["role"] = "student"
                        request.session["name"] = stu_obj.s_name
                        request.session["password"] = stu_obj.s_password
                        request.session["head_img"] = stu_obj.s_head_image
                        ret["status"] = 1
                        ret["msg"] = '/home/'
                    else:
                        # 判断学生状态
                        ret["status"] = 3
                        ret["msg"] = "该学生已被注销"
                else:
                    ret["status"] = 4
                    ret["msg"] = "账号或密码不正确，请重新输入！"

            elif role == "2":
                tea_obj = WebTeacher.objects.filter(t_account=account, t_password=password).first()
                if tea_obj:
                    # 确认教师账号存在
                    if tea_obj.t_state == 1:
                        # 判断教师状态
                        ret["status"] = 1
                        request.session["account"] = account
                        request.session["role"] = "teacher"
                        # request.session["name"] = tea_obj.t_name
                        # request.session["password"] = tea_obj.t_password
                        # request.session["head_img"] = tea_obj.t_head_image
                        ret["msg"] = "/home/"

                    else:
                        ret["status"] = 3
                        ret["msg"] = "该教师已被注销"

                else:
                    ret["status"] = 4
                    ret["msg"] = "账号或密码不正确，请重新输入！"
        else:
            ret['status'] = 0
            ret['msg'] = form_obj.errors
        return JsonResponse(ret)
    # 生成一个form对象
    loginForm = LoginForm()
    return render(request, 'index.html', locals())


# 注册
import os
from django.conf import settings
def reg(request):
    if request.method == "POST":
        ret = {}
        form_obj = RegForm(request.POST)

        # 做校验
        if form_obj.is_valid():
            # 校验通过 在数据库中保存信息

            s_id = create_uuid()
            sex = 1
            state = 1
            grade = "一年级"
            create_time = int(time.time())

            s_name = form_obj.cleaned_data["name"]
            s_account = form_obj.cleaned_data["account"]
            s_password = form_obj.cleaned_data["password"]

            avatar_img = request.FILES.get("avatar")
            # print(avatar_img)

            if avatar_img:
                avatar_uid = create_uuid()
                avatar_img_name = avatar_uid + "." + avatar_img.name.split(".")[1]
                path = os.path.join(settings.MEDIA_ROOT, 'avatars', avatar_img_name)

                with open(path, "wb") as f:
                    for line in avatar_img:
                        f.write(line)

                avatar_url = "http://" + request.get_host() + "/media/avatars/" + avatar_img_name


            else:
                avatar_url = "http://" + request.get_host() + "/media/avatars/deflaut.png"


            stu_obj = WebStudent.objects.create(s_id=s_id, s_account=s_account, s_password=s_password, s_name=s_name,
                                                s_sex=sex, s_state=state, s_grade=grade, s_create_time=create_time,
                                                s_head_image=avatar_url)
            l_id = create_uuid()
            ip = get_ip()
            create_time = int(time.time())
            action = "注册用户"
            WebLogsheet.objects.create(l_id=l_id, l_action=action, l_user_id=stu_obj.s_name,
                                       l_create_time=create_time, l_state=0, l_ip=ip)
            ret["status"] = 1
            ret["msg"] = '/index/'
            return JsonResponse(ret)

        else:
            ret['status'] = 0
            ret['msg'] = form_obj.errors
            return JsonResponse(ret)

    # 生成一个form对象
    reg = RegForm()
    return render(request, 'index.html', locals())


# 短信校验
import urllib, json, urllib.request
from urllib import parse
import random
import re


#注册验证码
def verify_code(request):
    # 生成随机验证码
    l = []
    for i in range(6):
        l.append(random.randint(0, 9))
    code = "".join([str(l[i]) + str(l[i + 1]) for i in range(0, len(l), 2)])
    ret = {}
    if request.method == "POST":
        account = request.POST.get("account")

        if account:
            match = re.findall((r'^(13[0-9]|15[012356789]|17[678]|18[0-9]|14[57])[0-9]{8}$'), account)

            if match:
                stu_obj = WebStudent.objects.filter(s_account=account)
                if stu_obj:
                    ret["status"] = 0
                    ret["error"] = "手机号码已注册！"
                    return JsonResponse(ret)

                else:

                    appkey = '337b85164bdc1bfd18b111a17b5a3478'  # 您申请的短信服务appkey
                    mobile = '{}'.format(account)  # 短信接受者的手机号码
                    tpl_id = '108018'  # 申请的短信模板ID,根据实际情况修改
                    tpl_value = '#code#={}&#company#=酷丁编程'.format(code)  # 短信模板变量,根据实际情况修改
                    sendsms(appkey, mobile, tpl_id, tpl_value)  # 请求发送短信

                    ret["status"] = 1
                    ret["account"] = account
                    ret["code"] = code
                    print(code)

            else:
                ret["status"] = 0
                ret["error"] = "请输入正确的号码！"
        else:
            ret["status"] = 0
            ret["error"] = "手机号码不能为空！"


        return JsonResponse(ret)


# 忘记密码验证码
def get_code(request):
    # 生成随机验证码
    l = []
    for i in range(6):
        l.append(random.randint(0, 9))
    code = "".join([str(l[i]) + str(l[i + 1]) for i in range(0, len(l), 2)])
    ret = {}
    if request.method == "POST":
        account = request.POST.get("account")

        if account:
            match = re.findall((r'^(13[0-9]|15[012356789]|17[678]|18[0-9]|14[57])[0-9]{8}$'), account)

            if match:
                stu_obj = WebStudent.objects.filter(s_account=account)
                if stu_obj:

                    appkey = '337b85164bdc1bfd18b111a17b5a3478'  # 您申请的短信服务appkey
                    mobile = '{}'.format(account)  # 短信接受者的手机号码
                    tpl_id = '108018'  # 申请的短信模板ID,根据实际情况修改
                    tpl_value = '#code#={}&#company#=酷丁编程'.format(code)  # 短信模板变量,根据实际情况修改
                    sendsms(appkey, mobile, tpl_id, tpl_value)  # 请求发送短信

                    ret["status"] = 0
                    ret["account"] = account
                    ret["code"] = code
                    print(code)

                else:
                    ret["status"] = 1
                    ret["error"] = "该号码未注册！"
            else:
                ret["status"] = 0
                ret["error"] = "请输入正确的号码！"
        else:
            ret["status"] = 0
            ret["error"] = "手机号码不能为空！"


        return JsonResponse(ret)


def sendsms(appkey, mobile, tpl_id, tpl_value):
    sendurl = 'http://v.juhe.cn/sms/send'  # 短信发送的URL,无需修改

    params = 'key=%s&mobile=%s&tpl_id=%s&tpl_value=%s' % \
             (appkey, mobile, tpl_id, urllib.parse.quote(tpl_value))  # 组合参数

    wp = urllib.request.urlopen(sendurl + "?" + params)
    content = wp.read()  # 获取接口返回内容

    result = json.loads(content)

    if result:
        error_code = result['error_code']
        if error_code == 0:
            # 发送成功
            smsid = result['result']['sid']
            print("sendsms success,smsid: %s" % (smsid))
            return "sendsms success,smsid: %s" % (smsid)
        else:
            # 发送失败
            print("sendsms error :(%s) %s" % (error_code, result['reason']))
            return "sendsms error :(%s) %s" % (error_code, result['reason'])
    else:
        # 请求失败
        print("request sendsms error")


#注销(退出登陆)
def logout(request):
    account = request.session.get("account")
    role = request.session.get("role")
    if account:
        del request.session["account"]
    return redirect('/index/')


#个人主页
#孙新洋
def home(request):
    # if request.method == "GET":
    #取当前登陆人的账号和身份
    account = request.session.get("account", None)
    role = request.session.get("role",None)


    #判断身份
    if account:
        if role == "student":
            # 学生
            stu_obj = WebStudent.objects.filter(s_account=account).first()
            stu_info = WebLogsheet.objects.filter(l_user_id=stu_obj.pk).values("l_create_time").order_by(
                "l_create_time").first()




            # 查找班主任
            teachers = WebGrant.objects.filter(g_sid=stu_obj.pk).first()

            if teachers:
                t_info_obj = WebTeacher.objects.filter(t_id=teachers.g_tid_id).all().values()

                # 查询课程
                course_id_list = WebGrant.objects.filter(g_sid=stu_obj.pk).values_list("g_did_id").distinct()
                # print(course_id_list)
                course_list = []
                for course_ids in course_id_list:
                    for course_id in course_ids:
                        # print(course_id)
                        course = WebDetail.objects.filter(d_id=course_id).first()
                        cid = WebDetail.objects.filter(d_id=course_id).values("d_cid_id").distinct()
                        course_table = WebCourse.objects.filter(c_id=cid).first()
                        # print(course_table)
                        if course_table not in course_list:
                            course_list.append(course_table)
                # print(course_list)

                if course_list:
                    course_list.sort(key=lambda course_list: course_list.c_create_time, reverse=True)

                # course_list.sort(WebDetail.d_create_time)
                # print(course_list)

            return render(request, 'home.html', locals())

        elif role == "teacher":
            # 教师
            tea_obj = WebTeacher.objects.filter(t_account=account).first()
            # print(tea_obj)

            # 通知
            # l_state_obj = WebLogsheet.objects.filter(l_tid=tea_obj.pk).first()
            # s_l_state = l_state_obj.l_state

            # 查找学生
            student_list = WebGrant.objects.filter(g_tid_id=tea_obj.pk).values_list("g_sid_id").distinct()
            # print(student_list)
            s_info_list = []
            # student_list = [("123456789123",'1321','1231')]
            for students in student_list:
                for student in students:
                    s_info = WebStudent.objects.filter(s_id=student).first()
                    # print(s_info)
                    s_info_list.append(s_info)
            # print(s_info_list)

            # 查询课程
            course_id_list = WebGrant.objects.filter(g_tid=tea_obj.pk).values_list("g_did_id").distinct()
            # print(course_id_list)
            course_list = []
            for course_ids in course_id_list:
                for course_id in course_ids:
                    # print(course_id)
                    course = WebDetail.objects.filter(d_id=course_id).first()
                    cid = WebDetail.objects.filter(d_id=course_id).values("d_cid_id").distinct()
                    course_table = WebCourse.objects.filter(c_id=cid).first()
                    # print(course_table)
                    if course_table not in course_list:
                        course_list.append(course_table)
                # print(course_list)

                if course_list:
                    course_list.sort(key=lambda course_list: course_list.c_create_time, reverse=True)
                    # course_list.append(course)
            tea_info = WebLogsheet.objects.filter(l_user_id=tea_obj.pk).values("l_create_time").order_by(
                "l_create_time").first()

            return render(request, 'home.html', locals())

    return redirect('/login/')


#个人中心
#孙新洋
def center(request):
    #取当前登陆人的账号和身份
    account = request.session.get("account", None)
    role = request.session.get("role", None)

    book_list = []
    course_list = []
    if role == "student":

        stu_obj = WebStudent.objects.filter(s_account=account).first()
        grant_obj = WebGrant.objects.filter(g_sid=stu_obj.pk).values_list()
        for i in grant_obj:
            book_info = WebDetail.objects.filter(d_id=i[5]).first()
            if book_info not in book_list:
                book_list.append(book_info)
                for book in book_list:
                    # print(book.d_cid_id)
                    course_id = book.d_cid_id
                    if course_id not in course_list:
                        course_list.append(course_id)

        course_obj_list = []
        for c_id in course_list:
            course_obj = WebCourse.objects.filter(c_id=c_id)
            course_obj_list.append(course_obj)

    if role == "teacher":
        tea_obj = WebTeacher.objects.filter(t_account=account).first()
        # print(tea_obj)
        grant_obj = WebGrant.objects.filter(g_tid=tea_obj.pk).values_list()

        for i in grant_obj:
            book_info = WebDetail.objects.filter(d_id=i[5]).first()
            if book_info not in book_list:
                book_list.append(book_info)
                for book in book_list:
                    # print(book.d_cid_id)
                    course_id = book.d_cid_id
                    if course_id not in course_list:
                        course_list.append(course_id)

        course_obj_list = []
        for c_id in course_list:
            course_obj = WebCourse.objects.filter(c_id=c_id)
            course_obj_list.append(course_obj)

    return render(request, 'center.html', locals())


#更改个人信息
#孙新洋
import time
def confirm_center(request):
    if request.method == "POST":
        role = request.session.get("role", None)
        account = request.session.get("account", None)
        ret = {}
        username = request.POST.get("username")
        sex = request.POST.get("sex")
        grade = request.POST.get("grade")
        age = request.POST.get("age")
        email = request.POST.get("email")
        remark = request.POST.get("remark")

        avatar_img = request.FILES.get("avatar")
        # print("avatar_img", type(avatar_img), avatar_img)
        # form_obj.cleaned_data.pop("re_password")
        # avatar_img = request.FILES.get("avatar")
        if avatar_img:
            avatar_uid = create_uuid()
            avatar_img_name = avatar_uid + "." + avatar_img.name.split(".")[1]
            path = os.path.join(settings.MEDIA_ROOT, 'avatars', avatar_img_name)

            with open(path, "wb") as f:
                for line in avatar_img:
                    f.write(line)

            avatar_url = "http://" + request.get_host() + "/media/avatars/" + avatar_img_name
        else:
            if role == "student":
                avatar_url = WebStudent.objects.filter(s_account=account).values("s_head_image")
            else:
                avatar_url = WebTeacher.objects.filter(t_account=account).values("t_head_image")

        if role == "student":
            WebStudent.objects.filter(s_account=account).update(s_name=username, s_email=email, s_sex=sex,
                                                                s_grade=grade, s_remark=remark, s_head_image=avatar_url)

        else:
            WebTeacher.objects.filter(t_account=account).update(t_sex=sex, t_age=age, t_name=username, t_remark=remark,
                                                                t_head_image=avatar_url)

        ret["status"] = 1
        ret["msg"] = "保存成功"
    return JsonResponse(ret)


#个人密码修改
#孙新洋
def confirm_pwd(request):
    if request.method == "POST":
        role = request.session.get("role", None)
        account = request.session.get("account", None)
        ret = {}
        pwd = request.POST.get("pwd")
        new_pwd = request.POST.get("new_pwd")
        conf_pwd = request.POST.get("conf_pwd")



        if role == "student":
            stu_obj = WebStudent.objects.filter(s_password=pwd).first()
            if stu_obj:
                if new_pwd == conf_pwd:
                    WebStudent.objects.filter(s_account=account).update(s_password=new_pwd)
                    l_id = create_uuid()
                    ip = get_ip()
                    create_time = int(time.time())
                    action = "学生修改个人信息"
                    WebLogsheet.objects.create(l_id=l_id, l_action=action, l_user_id=stu_obj.s_name,
                                               l_create_time=create_time, l_state=0, l_ip=ip)
                    ret["status"] = 1
                    ret["msg"] = "保存成功"
                else:
                    ret["status"] = 0
                    ret["msg"] = "两次输入的密码不正确，请重新输入！"
            else:
                ret["status"] = 0
                ret["msg"] = "旧密码不正确，请重新输入！"
        else:
            tea_obj = WebTeacher.objects.filter(t_password=pwd)
            if tea_obj and new_pwd == conf_pwd:
                if new_pwd == conf_pwd:
                    WebTeacher.objects.filter(t_account=account).update(t_password=new_pwd)

                    l_id = create_uuid()
                    ip = get_ip()
                    create_time = int(time.time())
                    action = "教师修改个人信息"
                    WebLogsheet.objects.create(l_id=l_id, l_action=action, l_user_id=tea_obj.t_name,
                                               l_create_time=create_time, l_state=0, l_ip=ip)
                    ret["status"] = 1
                    ret["msg"] = "保存成功"
                else:
                    ret["status"] = 0
                    ret["msg"] = "两次输入的密码不正确，请重新输入！"
            else:
                ret["status"] = 0
                ret["msg"] = "旧密码不正确，请重新输入！"
    return JsonResponse(ret)


def points(request):
    # 取当前登陆人的账号和身份
    account = request.session.get("account", None)
    role = request.session.get("role", None)
    stu_obj = WebStudent.objects.filter(s_account=account).first()
    tea_obj = WebTeacher.objects.filter(t_account=account).first()

    return render(request, 'points.html', locals())


def m_student(request):
    """
    author:，孟浩
    学生端详情
    """
    if request.method == 'GET':
        times = time.ctime()
        # 将格式字符串转换为时间戳
        times = time.mktime(time.strptime(times, "%a %b %d %H:%M:%S %Y"))
        location_time = (times + 300.0)
        # location_time = 1537856766.0
        account = request.session["account"]
        role = request.session.get("role", None)
        sid = WebStudent.objects.filter(s_account=account).values("s_id").first()
        stu_obj = WebStudent.objects.filter(s_account=account).first()
        sid_id = sid['s_id']
        detail_list = WebDetail.objects.filter(webgrant__g_sid=sid_id).values().distinct()
        detail_evaluate = WebDetail.objects.filter(webgrant__g_sid=sid_id, webgrant__g_record='1').values()
        course_list = WebCourse.objects.filter(webdetail__webgrant__g_sid_id=sid_id).values().distinct()
        evaluate_list = WebEvaluate.objects.filter(e_gid__g_sid_id=sid_id).values().distinct()
        teacher_list = WebTeacher.objects.filter(webgrant__g_sid=sid_id).values().distinct()
        grent_list = WebGrant.objects.filter(g_sid=sid_id).values().distinct()
        # grent_url = WebGrant.objects.filter(g_sid=sid_id).values_list('g_url')[0][0]

        # 评价
        informations = []
        for detail in detail_list:
            infor = {}
            d_id = detail['d_id']
            d_name = detail['d_name']
            infor['d_id'] = d_id
            infor['d_name'] = d_name
            infor['s_id'] = sid_id
            teacher_id = WebTeacher.objects.filter(webgrant__g_sid=sid_id, webgrant__g_did=d_id).values().distinct()
            for teacher in teacher_id:
                t_id = teacher['t_id']
                t_name = teacher['t_name']
                infor['t_id'] = t_id
                infor['t_name'] = t_name
            # grent_id = WebGrant.objects.filter(g_sid_id=sid_id,g_did_id=d_id).values().distinct()
            # for grent in grent_id:
            #     g_time = grent['g_time']
            #     g_record = grent['g_record']
            #     infor['g_time'] = g_time
            #     infor['g_record'] = g_record

            informations.append(infor)

        # 我的课程计划
        course_infor = []
        for grent_urls in grent_list:
            gr = {}
            grent_ur = grent_urls['g_url']
            grent_time = grent_urls['g_time']
            grent_sid = grent_urls['g_sid_id']
            grent_did = grent_urls['g_did_id']
            grent_tid = grent_urls['g_tid_id']
            grent_record = grent_urls['g_record']
            gr['url'] = grent_ur
            gr['grent_sid'] = grent_sid
            gr['grent_time'] = grent_time
            gr['grent_record'] = grent_record
            teacher_lists = WebTeacher.objects.filter(webgrant__g_sid=sid_id,
                                                      webgrant__g_tid=grent_tid).values().distinct()
            for teacher in teacher_lists:
                t_id = teacher['t_id']
                t_name = teacher['t_name']
                gr['t_id'] = t_id
                gr['t_name'] = t_name
            detail_lists = WebDetail.objects.filter(webgrant__g_sid=sid_id,
                                                    webgrant__g_did=grent_did).values().distinct()
            for detail in detail_lists:
                d_id = detail['d_id']
                d_name = detail['d_name']
                gr['d_id'] = d_id
                gr['d_name'] = d_name

            course_infor.append(gr)

        grent_join_url = []
        for i in course_infor:
            join_url = {}

            grent_time = i['grent_time']
            grent_sid = i['grent_sid']
            grent_record = i['grent_record']
            grent_t_name = i['t_name']
            grent_d_name = i['d_name']

            join_url['grent_time'] = grent_time
            join_url['grent_sid'] = grent_sid
            join_url['grent_record'] = grent_record
            join_url['grent_d_name'] = grent_d_name
            join_url['grent_t_name'] = grent_t_name

            if i['url'] == None:
                join_url['grent_j_url'] = 'error'
            else:
                grent_j_url = eval(i['url'])['join_url']
                join_url['grent_j_url'] = grent_j_url
            # else:
            #     join_url['grent_j_url'] = 'error'

            grent_join_url.append(join_url)


        return render(
            request, 'm_student.html',
            {
                'course_list': course_list,
                'detail_list': detail_list,
                'grent_list': grent_list,
                'evaluate_list': evaluate_list,
                'detail_evaluate': detail_evaluate,
                'teacher_list': teacher_list,
                "stu_obj": stu_obj,
                "role": role,
                "sid_id": sid_id,
                'location_time': location_time,
                'grent_join_url': grent_join_url,
                'informations': informations,

            }
        )

    else:
        show_inf = {'status': True, 'inf': None}

        try:
            e_stot_evaluate = request.POST.get('e_stot_evaluate')
            e_stot_score = request.POST.get('e_stot_score')

            # 创建e_gid_id
            e_sid_id = request.POST.get('e_sid_id')
            e_tid_name = request.POST.get('grent_t_name')
            e_did_name = request.POST.get('grent_d_name')

            e_gid = WebGrant.objects.filter(g_tid__t_name=e_tid_name, g_sid=e_sid_id,
                                            g_did__d_name=e_did_name, ).values("g_id").first()
            e_gid_id = e_gid['g_id']

            import uuid
            s_uuid = str(uuid.uuid1())
            l_uuid = s_uuid.split('-')
            e_id = ''.join(l_uuid)

            # 创建时间
            times = time.ctime()
            e_create_time = time.mktime(time.strptime(times, "%a %b %d %H:%M:%S %Y"))
            if e_gid_id != '':
                evaluate_count = WebEvaluate.objects.filter(e_gid_id=e_gid_id).count()
                if evaluate_count == 0:
                    show_inf['inf'] = '评价成功，谢谢！'
                    WebEvaluate.objects.create(
                        e_id=e_id,
                        e_stot_evaluate=e_stot_evaluate,
                        e_stot_score=e_stot_score,
                        e_create_time=e_create_time,
                        e_gid_id=e_gid_id
                    )
                else:
                    evaluate_t = WebEvaluate.objects.filter(e_gid_id=e_gid_id).values('e_ttos_score').first()
                    evaluate_s = WebEvaluate.objects.filter(e_gid_id=e_gid_id).values('e_stot_score').first()
                    if evaluate_t['e_ttos_score'] != None and evaluate_s['e_stot_score'] == None:
                        show_inf['inf'] = '评价老师成功，谢谢！'
                        WebEvaluate.objects.filter(e_gid_id=e_gid_id).update(
                            e_stot_evaluate=e_stot_evaluate,
                            e_stot_score=e_stot_score,
                        )
                    else:
                        show_inf['inf'] = '您已经评价过该老师，无需重复评价，谢谢'
        except Exception as e:
            show_inf['status'] = False
            show_inf['inf'] = '对不起，您的评价出现了错误，请确定老师和课程是否匹配，请重新评价，谢谢！'

        res = json.dumps(show_inf)
        return HttpResponse(res)

def editdetail(request):
    show_inf = {'status': True, 'inf': None}
    if request.method == "POST":
        t_id = request.POST.get('tid')
        g_id = request.POST.get('gid')
        g_time = request.POST.get('data')
        sendurl = 'http://192.168.0.107:7000/remoteEditTime'  # 短信发送的URL,无需修改
        timeArray = time.strptime(g_time, "%Y-%m-%dT%H:%M")
        timeStamp = int(time.mktime(timeArray))
        # print('timeStamp', timeStamp)
        # print('timeStamp', type(timeStamp))
        params = 'time=%s&gid=%s&tid=%s' % (timeStamp, g_id, t_id)  # 组合参数
        print('params', params)

        wp = urllib.request.urlopen(sendurl + "?" + params)
        content = wp.read()  # 获取接口返回内容
        show_inf['inf'] = '发送成功！'
        result = json.loads(content)
        print('result', result)


    #     d_remark = request.POST.get('remark')
    #     if not d_remark:
    #         d_remark = ""
    #     # print(d_id, d_create_time, d_remark)
    #     WebDetail.objects.filter(d_id=d_id).update(
    #         d_id=d_id,
    #         d_remark=d_remark,
    #     )
    #     WebGrant.objects.filter(g_did_id=d_id).update(
    #         g_time=timeStamp
    #     )
    # except Exception as e:
    else:
        show_inf['status'] = False
        show_inf['inf'] = '发送失败！'

    res = json.dumps(show_inf)
    return HttpResponse(res)

def m_evaluate(request):
    """
    autor:孟浩
    学生评价老师
    :param request:
    :return:评价列表
    """
    account = request.session["account"]
    role = request.session.get("role", None)
    stu_obj = WebStudent.objects.filter(s_account=account).first()

    sid_id = request.GET.get('sid')
    evaluate_list = WebEvaluate.objects.filter(e_gid__g_sid_id=sid_id).values().distinct()

    evaluate_count = WebEvaluate.objects.filter(e_gid__g_sid_id=sid_id).count()

    if evaluate_count != 0:
        evaluate_gid = WebEvaluate.objects.filter(e_gid__g_sid_id=sid_id).values()
        eve_list = []
        for evaluate in evaluate_gid:
            eve = {}
            e_gid_id = evaluate['e_gid_id']
            e_ttos_evaluate = evaluate['e_ttos_evaluate']
            e_stot_evaluate = evaluate['e_stot_evaluate']
            e_ttos_score = evaluate['e_ttos_score']
            e_stot_score = evaluate['e_stot_score']
            e_remark = evaluate['e_remark']
            e_create_time = evaluate['e_create_time']
            eve = {
                'e_gid_id': e_gid_id,
                'e_ttos_evaluate': e_ttos_evaluate,
                'e_stot_evaluate': e_stot_evaluate,
                'e_ttos_score': e_ttos_score,
                'e_stot_score': e_stot_score,
                'e_remark': e_remark,
            }
            teacher_name = WebTeacher.objects.filter(webgrant__g_id=e_gid_id).values().distinct()
            for teacher in teacher_name:
                t_name = teacher['t_name']
                t_id = teacher['t_id']
                eve['t_name'] = t_name
                detail_name = WebDetail.objects.filter(webgrant__g_id=e_gid_id,
                                                       webgrant__g_tid=t_id).values().distinct()
                for detail in detail_name:
                    d_name = detail['d_name']
                    eve['d_name'] = d_name
                eve_list.append(eve)

        return render(
            request,
            'm_evaluate.html',
            {
                'eve_list': eve_list

            })
    else:
        return render(
            request,
            'm_evaluate.html',
        )


def m_evaluatestudent(request):
    """
    autor:孟浩
    老师评价学生
    :param request:
    :return:评价列表
    """
    account = request.session["account"]
    role = request.session.get("role", None)
    tea_obj = WebTeacher.objects.filter(t_account=account).first()

    tid_id = request.GET.get('tid')
    evaluate_list = WebEvaluate.objects.filter(e_gid__g_tid_id=tid_id).values().distinct()

    evaluate_count = WebEvaluate.objects.filter(e_gid__g_tid_id=tid_id).count()

    if evaluate_count != 0:
        evaluate_gid = WebEvaluate.objects.filter(e_gid__g_tid_id=tid_id).values()
        eve_list = []
        for evaluate in evaluate_gid:
            eve = {}
            e_gid_id = evaluate['e_gid_id']
            e_ttos_evaluate = evaluate['e_ttos_evaluate']
            e_stot_evaluate = evaluate['e_stot_evaluate']
            e_ttos_score = evaluate['e_ttos_score']
            e_stot_score = evaluate['e_stot_score']
            e_remark = evaluate['e_remark']
            # print('e_remark', e_remark)
            # print('e_remark', type(e_remark))
            eve = {
                'e_gid_id': e_gid_id,
                'e_ttos_evaluate': e_ttos_evaluate,
                'e_stot_evaluate': e_stot_evaluate,
                'e_ttos_score': e_ttos_score,
                'e_stot_score': e_stot_score,
                'e_remark': e_remark,
            }
            student_name = WebStudent.objects.filter(webgrant__g_id=e_gid_id).values().distinct()
            for student in student_name:
                s_name = student['s_name']
                s_id = student['s_id']
                eve['s_name'] = s_name
                detail_name = WebDetail.objects.filter(webgrant__g_id=e_gid_id,
                                                       webgrant__g_sid=s_id).values().distinct()
                for detail in detail_name:
                    d_name = detail['d_name']
                    eve['d_name'] = d_name
                eve_list.append(eve)

        return render(
            request,
            'm_evaluatestudent.html',
            {
                'eve_list': eve_list

            })
    else:
        return render(
            request,
            'm_evaluatestudent.html',
        )

import json
def m_teacher(request):
    """
    autor:孟浩
    教师端
    :param request:
    :return:
    """
    if request.method == 'GET':

        times = time.ctime()
        # 将格式字符串转换为时间戳
        times = time.mktime(time.strptime(times, "%a %b %d %H:%M:%S %Y"))
        location_time = (times + 300.0)
        # location_time = 1537856766.0
        account = request.session["account"]
        role = request.session.get("role", None)
        tea_obj = WebTeacher.objects.filter(t_account=account).first()
        tid = str(WebTeacher.objects.filter(t_account=account).values_list("t_id")[0][0])
        course_list = WebCourse.objects.filter(webdetail__webgrant__g_tid=tid).values().distinct()
        student_list = WebStudent.objects.filter(webgrant__g_tid=tid).values().distinct()
        detail_list = WebDetail.objects.filter(webgrant__g_tid_id=tid).values().distinct()
        grent_list = WebGrant.objects.filter(g_tid=tid).values().distinct()

        # 评价学生
        course_infor = []
        for grent_urls in grent_list:
            gr = {}
            grent_ur = grent_urls['g_url']
            grent_time = grent_urls['g_time']
            grent_sid = grent_urls['g_sid_id']
            grent_did = grent_urls['g_did_id']
            grent_tid = grent_urls['g_tid_id']
            grent_record = grent_urls['g_record']
            gr['url'] = grent_ur
            gr['grent_sid'] = grent_sid
            gr['grent_tid'] = grent_tid
            gr['grent_time'] = grent_time
            gr['grent_record'] = grent_record
            student_lists = WebStudent.objects.filter(webgrant__g_tid=tid,
                                                      webgrant__g_sid=grent_sid).values().distinct()
            for student in student_lists:
                s_id = student['s_id']
                s_name = student['s_name']
                gr['s_id'] = s_id
                gr['s_name'] = s_name
            detail_lists = WebDetail.objects.filter(webgrant__g_tid=tid,
                                                    webgrant__g_did=grent_did).values().distinct()
            for detail in detail_lists:
                d_id = detail['d_id']
                d_name = detail['d_name']
                gr['d_id'] = d_id
                gr['d_name'] = d_name

            course_infor.append(gr)

        grent_join_url = []
        for i in course_infor:
            join_url = {}

            grent_time = i['grent_time']
            grent_tid = i['grent_tid']
            grent_record = i['grent_record']
            grent_s_name = i['s_name']
            grent_d_name = i['d_name']

            join_url['grent_time'] = grent_time
            join_url['grent_tid'] = grent_tid
            join_url['grent_record'] = grent_record
            join_url['grent_d_name'] = grent_d_name
            join_url['grent_s_name'] = grent_s_name
            if i['url'] == None:
                join_url['grent_j_url'] = 'error'
            else:
                # if eval(i['url'])['error']:
                #     join_url['grent_j_url'] = 'error'
                # else:
                grent_j_url = eval(i['url'])['start_url']
                join_url['grent_j_url'] = grent_j_url
                # print(join_url["grent_j_url"])

            grent_join_url.append(join_url)
        # 评价学生结束


        return render(request, 'm_teacher.html',
                      {
                          'course_list': course_list,
                          'student_list': student_list,
                          'detail_list': detail_list,
                          'grent_list': grent_list,
                          "role": role,
                          "tea_obj": tea_obj,
                          'tid': tid,
                          'grent_join_url': grent_join_url,
                          'location_time': location_time,

                      })
    else:
        show_inf = {'status': True, 'inf': None}

        try:
            e_ttos_evaluate = request.POST.get('e_ttos_evaluate')
            e_ttos_score = request.POST.get('e_ttos_score')

            # 创建e_gid_id
            e_tid_id = request.POST.get('e_tid_id')
            e_sid_name = request.POST.get('grent_s_name')
            e_did_name = request.POST.get('grent_d_name')

            e_gid = WebGrant.objects.filter(g_sid__s_name=e_sid_name, g_tid=e_tid_id,
                                            g_did__d_name=e_did_name, ).values("g_id").first()
            e_gid_id = e_gid['g_id']
            # print('e_gid_id', e_gid_id)

            import uuid
            s_uuid = str(uuid.uuid1())
            l_uuid = s_uuid.split('-')
            e_id = ''.join(l_uuid)

            # 创建时间
            times = time.ctime()
            e_create_time = time.mktime(time.strptime(times, "%a %b %d %H:%M:%S %Y"))
            if e_gid_id != '':
                evaluate_count = WebEvaluate.objects.filter(e_gid_id=e_gid_id).count()

                if evaluate_count == 0:
                    show_inf['inf'] = '评价成功，谢谢！'
                    WebEvaluate.objects.create(
                        e_id=e_id,
                        e_ttos_evaluate=e_ttos_evaluate,
                        e_ttos_score=e_ttos_score,
                        e_create_time=e_create_time,
                        e_gid_id=e_gid_id
                    )
                else:
                    evaluate_s = WebEvaluate.objects.filter(e_gid_id=e_gid_id).values('e_stot_score').first()
                    evaluate_t = WebEvaluate.objects.filter(e_gid_id=e_gid_id).values('e_ttos_score').first()
                    if evaluate_s['e_stot_score'] != None and evaluate_t['e_ttos_score'] == None:
                        show_inf['inf'] = '评价学生成功，谢谢！'
                        WebEvaluate.objects.filter(e_gid_id=e_gid_id).update(
                            e_ttos_evaluate=e_ttos_evaluate,
                            e_ttos_score=e_ttos_score,
                        )
                    else:
                        show_inf['inf'] = '您已经评价过该学生，无需重复评价，谢谢'
        except Exception as e:
            show_inf['status'] = False
            show_inf['inf'] = '对不起，您的评价出现了错误，请确定学生和课程是否匹配，请重新评价，谢谢！'

        res = json.dumps(show_inf)
        return HttpResponse(res)


#吴家贵
# 通知
import time
def notice(request):
    # 后台读取当前登录用户的相关信息并返回给前台显示
    account = request.session.get("account", None)
    role = request.session.get("role", None)
    if role == "student":
        stu_obj = WebStudent.objects.filter(s_account=account).first()
        s_id = WebStudent.objects.filter(s_account=account).values("s_id")
        s_log_obj = WebLogsheet.objects.filter(l_sid=s_id).values().order_by("-l_create_time")
        all_s_log_obj = WebLogsheet.objects.filter(l_sid="all_student").values().order_by("-l_create_time")
        if s_log_obj:
            l_state_obj = WebLogsheet.objects.filter(l_sid=s_id).values()
            # print("-" * 120)
            # print(l_state_obj)
            if l_state_obj:
                for l_state in l_state_obj:
                    # l_state = l_state_obj.l_state
                    # print("-" * 120)
                    # print(l_state["l_state"])
                    if l_state["l_state"] == "0" or l_state["l_state"] == "2":
                        s_log_state = WebLogsheet.objects.filter(l_sid=s_id).update(l_state=2)
                    else:
                        s_log_state = WebLogsheet.objects.filter(l_sid=s_id).update(l_state=3)

    if role == "teacher":
        tea_obj = WebTeacher.objects.filter(t_account=account).first()
        t_id = WebTeacher.objects.filter(t_account=account).values("t_id")
        t_log_obj = WebLogsheet.objects.filter(l_tid=t_id).values().order_by("-l_create_time")
        all_t_log_obj = WebLogsheet.objects.filter(l_tid="all_teacher").values().order_by("-l_create_time")
        # print("-" * 120)
        # print(all_t_log_obj)
        # print("-" * 120)
        if t_log_obj:
            l_state_obj = WebLogsheet.objects.filter(l_tid=t_id).values()
            # l_state = l_state_obj.l_state

            if l_state_obj:
                for l_state in l_state_obj:
                    # l_state = l_state_obj.l_state
                    # print("-" * 120)
                    # print(l_state["l_state"])
                    if l_state["l_state"] == "0" or l_state["l_state"] == "1":
                        s_log_state = WebLogsheet.objects.filter(l_tid=t_id).update(l_state=2)
                    else:
                        s_log_state = WebLogsheet.objects.filter(l_tid=t_id).update(l_state=3)

            # print(type(l_state), l_state)

    return render(request, "notice.html", locals())


# 帮助
def help(request):
    account = request.session.get("account", None)
    role = request.session.get("role", None)
    stu_obj = WebStudent.objects.filter(s_account=account).first()
    tea_obj = WebTeacher.objects.filter(t_account=account).first()
    return render(request, "help.html", locals())


# 代码工具
def tool(request):
    account = request.session.get("account", None)
    role = request.session.get("role", None)
    stu_obj = WebStudent.objects.filter(s_account=account).first()
    tea_obj = WebTeacher.objects.filter(t_account=account).first()
    return render(request, "tool.html", locals())


# 班级信息
def test(request):
    account = request.session.get("account", None)
    role = request.session.get("role", None)
    stu_obj = WebStudent.objects.filter(s_account=account).first()
    tea_obj = WebTeacher.objects.filter(t_account=account).first()
    classes_list = WebClasses.objects.all()
    # print(classes_list)
    t_list = []
    for i in classes_list:
        t_obj = WebRelation.objects.filter(c_id=i.c_id).values_list("t_id__t_name", "c_id__c_name", "t_id", "c_id")
        for t in t_obj:
            t_list.append(t)

    # print(t_list)

    return render(request, "test.html", locals())


# 文章详情
def article_detail(request, id):
    if request.method == "POST":
        keyword = request.POST.get("keyword")
        article_sea = TArticles.objects.filter()
    article_list = TArticles.objects.all().order_by("-t_createtime")
    # print(article_list)
    article_obj = TArticles.objects.filter(s_id=id).first()
    return render(request, 'article_detail.html', locals())


# 文章列表
def article_list(request):

    return render(request, 'article_list.html')

#测试
# def test2(request):
#
#     return render(request, 'test2_html.html')


# 忘记密码
def change_pwd(request):
    ret = {}
    if request.method == "POST":
        account = request.POST.get("account")
        pwd = request.POST.get("pwd")
        flag = WebStudent.objects.filter(s_account=account).update(s_password=pwd)
        stu_obj = WebStudent.objects.filter(s_account=account).first()
        if flag:
            l_id = create_uuid()
            ip = get_ip()
            create_time = int(time.time())
            action = "忘记密码，修改密码成功"
            WebLogsheet.objects.create(l_id=l_id, l_action=action, l_user_id=stu_obj.s_name, l_create_time=create_time,
                                       l_state=0, l_ip=ip)
            # print(account, pwd)
            ret["status"] = 1
            ret["href"] = '/index/'
    return JsonResponse(ret)

# 显示教师详情
# def t_info_detail(request):
#     if request.method == "POST":
#         t_account = request.POST.get("t_account")
#         tea_detail_obj = WebTeacher.objects.filter(t_account=t_account).first()
#         ret = {}
#         ret["t_name"] = tea_detail_obj.t_name
#         ret["t_account"] = tea_detail_obj.t_account
#         ret["t_age"] = tea_detail_obj.t_age
#         ret["t_sex"] = tea_detail_obj.t_sex
#         ret["t_state"] = tea_detail_obj.t_state
#         ret["t_create_time"] = tea_detail_obj.t_create_time
#         ret["t_degree"] = tea_detail_obj.t_degree
#         ret["t_detail"] = tea_detail_obj.t_detail
#         ret["t_hera_img"] = tea_detail_obj.t_hera_img
#         ret["t_remark"] = tea_detail_obj.t_remark
#     return JsonResponse(ret)


def join_classes(request):
    if request.method == "POST":
        t_id = request.POST.get("t_id")
        c_id = request.POST.get("c_id")
        s_id = request.POST.get("s_id")
        u_id = create_uuid()
        WebRelation.objects.create(r_id=u_id, s_id=s_id, c_id=c_id, t_id=t_id, r_state=0)
        ret = {}
        ret["msg"] = "已加入，待审核！"
        return JsonResponse(ret)


def class_inquiry(request):
    ret = {}
    if request.method == "POST":
        c_name = request.POST.get("c_name")
        classes_list = WebClasses.objects.filter(c_name__contains=c_name).all()
        htmls = ''
        if classes_list:
            for i in classes_list:
                t_obj = WebRelation.objects.filter(c_id=i.c_id).values_list("t_id__t_name", "c_id__c_name", "t_id",
                                                                            "c_id")
                for t in t_obj:
                    htmls += '<div class="every_single_class left "><p class="center" style="margin-left: 70px">{}</p><div class="single_info left"><p>授课教师: {} </p></div><div class="right"><a href="#"><i class="fa fa-3x fa-plus-square plus_in" aria-hidden="true"></i></a></div></div>'.format(
                        t[1], t[0])

            ret["status"] = 1
            ret["msg"] = htmls
            # print(htmls)
        else:
            ret["status"] = 0
            ret["msg"] = "未找到相关班级，请重输入！"

    return JsonResponse(ret)










def build_index(request):
    # print(render(request, "/build/index.html"))
    # print("../static/build/index.html")
    return render(request, "index.html")


# 额外接口
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def build_login(request):
    ret = {}
    if request.method == "POST":
        obj = json.loads(request.body)
        # print(obj, type(obj))
        account = obj["log_account"]
        password = obj["log_password"]
        # print(account,password)

        stu_obj = WebStudent.objects.filter(s_account=account, s_password=password).first()

        if stu_obj:
            ret["status"] = 1
            ret["s_id"] = stu_obj.s_id
            ret["account"] = stu_obj.s_account
            ret["name"] = stu_obj.s_name
            ret["head_img"] = stu_obj.s_head_image
            # print(ret)
        else:
            ret["status"] = 0
    else:
        ret["status"] = 0

    return JsonResponse(ret)
