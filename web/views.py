from django.shortcuts import render,HttpResponse,redirect
from django.http import JsonResponse
from web.form.student import Student_to_teacher
from web.form.reg import RegForm
# from web.form import reg
from article.models import TArticles
from web.models import WebTeacher, WebStudent, WebGrant, WebDetail, WebCourse, WebEvaluate
from web.form.login_form import LoginForm


# 首页
def index(request):
    article_list = TArticles.objects.using("articles").all().order_by("-t_createtime")
    article_list2 = []
    # print(len(article_list))
    # if len(article_list) < 3:
    #     article_list2 = article_list
    # else:
    #     pass
    # print(article_list[0],article_list[1],article_list[2])
    article_list2.append(article_list[0])
    article_list2.append(article_list[1])
    article_list2.append(article_list[2])
    # for i in range(3):

    loginForm = LoginForm()
    reg = RegForm()

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
        # print("-" * 120)
        # print(form_obj)
        # print("-" * 120)
        if form_obj.is_valid():
            account = request.POST.get("log_account")
            password = request.POST.get("log_password")
            role = request.POST.get("log_role")
            print(account, role, password)
            # print(type(role))
            # print("-" * 120)

            if role == "1":
                stu_obj = WebStudent.objects.filter(s_account=account, s_password=password).first()
                print(stu_obj)
                if stu_obj:
                    # 确认学生账号存在
                    if stu_obj.s_state == 1:
                        request.session["account"] = account
                        request.session["role"] = "student"
                        # print("-" * 120)
                        # print(request.session["account"])
                        # print(request.session["role"])
                        ret["status"] = 1
                        ret["msg"] = "/home/"

                    else:
                        # 判断学生状态
                        print("已注销")
                        ret["status"] = 3
                        ret["msg"] = "该学生已被注销"
                        print(
                            "hahahhahaha"
                        )

                else:
                    ret["status"] = 4
                    ret["msg"] = "账号或密码不正确，请重新输入！"
                    print(
                        "lalalalallallaal"
                    )

            elif role == "2":
                tea_obj = WebTeacher.objects.filter(t_account=account, t_password=password).first()
                # print(tea_obj)
                if tea_obj:
                    # 确认教师账号存在
                    if tea_obj.t_state == 1:
                        # 判断教师状态
                        ret["status"] = 1
                        request.session["account"] = account
                        request.session["role"] = "teacher"
                        ret["msg"] = "/home/"

                    else:
                        # print("已注销")
                        ret["status"] = 3
                        ret["msg"] = "该教师已被注销"

                else:
                    ret["status"] = 4
                    ret["msg"] = "账号或密码不正确，请重新输入！"


        else:
            ret['status'] = 0
            ret['msg'] = form_obj.errors
            # print(form_obj.errors)
            # print("-" * 120)
        return JsonResponse(ret)
    # 生成一个form对象
    loginForm = LoginForm()
    return render(request, 'index.html', locals())


# 注册
def reg(request):
    if request.method == "POST":
        ret = {}
        form_obj = RegForm(request.POST)
        # print(request.POST)

        # print("-" * 120)
        # print(form_obj)
        # 做校验
        if form_obj.is_valid():
            # 校验通过 在数据库中保存信息
            import uuid
            s_uuid = str(uuid.uuid1())
            l_uuid = s_uuid.split('-')
            s_id = ''.join(l_uuid)
            sex = 1
            state = 1
            grade = "一年级"
            create_time = int(time.time())
            # print("-" * 120)
            # print(form_obj.cleaned_data)
            # print("-" * 120)
            s_name = form_obj.cleaned_data["name"]
            s_account = form_obj.cleaned_data["account"]
            s_password = form_obj.cleaned_data["password"]
            # form_obj.cleaned_data.pop("re_password")
            # avatar_img = request.FILES.get("avatar")
            WebStudent.objects.create(s_id=s_id, s_account=s_account, s_password=s_password, s_name=s_name, s_sex=sex,
                                      s_state=state, s_grade=grade, s_create_time=create_time)
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
            print(match)
            if match:
                stu_obj = WebStudent.objects.filter(s_account=account)
                if stu_obj:
                    ret["status"] = 0
                    ret["error"] = "手机号码已注册！"
                    return JsonResponse(ret)
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

        appkey = '337b85164bdc1bfd18b111a17b5a3478'  # 您申请的短信服务appkey
        mobile = '{}'.format(account)  # 短信接受者的手机号码
        tpl_id = '102599'  # 申请的短信模板ID,根据实际情况修改
        tpl_value = '#code#={}&#company#=麒麟信息'.format(code)  # 短信模板变量,根据实际情况修改
        sendsms(appkey, mobile, tpl_id, tpl_value)  # 请求发送短信
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
    # print(account)
    # print(role)

    #判断身份
    if account:
        if role == "student":
            # 学生
            stu_obj = WebStudent.objects.filter(s_account=account).first()
            # print(stu_obj)

            # 查找班主任
            teachers = WebGrant.objects.filter(g_sid=stu_obj.pk).first()
            # print(teachers)
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
                        course_list.append(course)
                # print(course_list)

            return render(request, 'home.html', locals())

        elif role == "teacher":
            # 教师
            tea_obj = WebTeacher.objects.filter(t_account=account).first()
            # print(tea_obj)
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
                    course_list.append(course)
            # print(course_list)

            return render(request, 'home.html', locals())

    return redirect('/login/')


#个人中心
#孙新洋
def center(request):
    #取当前登陆人的账号和身份
    account = request.session.get("account", None)
    role = request.session.get("role", None)
    stu_obj = WebStudent.objects.filter(s_account=account).first()
    tea_obj = WebTeacher.objects.filter(t_account=account).first()
    # print(tea_obj)

    # 获取排行榜
    stu_rank_obj = WebStudent.objects.all().order_by("s_id")
    # print(stu_rank_obj)
# print(stu_obj.s_create_time)
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
        # print(username, email, grade, sex,remark)
        # print("- " * 120)
        # create_time = time.localtime(request.POST.get("create_time"))
        if role == "student":
            WebStudent.objects.filter(s_account=account).update(s_name=username, s_email=email, s_sex=sex,
                                                                s_grade=grade, s_remark=remark)
            # print("ok")
        else:
            WebTeacher.objects.filter(t_account=account).update(t_sex=sex, t_age=age, t_name=username, t_remark=remark)
            # print("ok")
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

        # print(pwd,new_pwd,conf_pwd)

        if role == "student":
            stu_obj = WebStudent.objects.filter(s_password=pwd).first()
            if stu_obj:
                if new_pwd == conf_pwd:
                    WebStudent.objects.filter(s_account=account).update(s_password=new_pwd)
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
                    ret["status"] = 1
                    ret["msg"] = "保存成功"
                else:
                    ret["status"] = 0
                    ret["msg"] = "两次输入的密码不正确，请重新输入！"
            else:
                ret["status"] = 0
                ret["msg"] = "旧密码不正确，请重新输入！"
    return JsonResponse(ret)


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
        obj_form = Student_to_teacher()
        account = request.session["account"]
        role = request.session.get("role", None)
        sid = WebStudent.objects.filter(s_account=account).values("s_id")
        sid_id = str(WebStudent.objects.filter(s_account=account).values_list("s_id")[0][0])
        stu_obj = WebStudent.objects.filter(s_account=account).first()
        course_list = WebCourse.objects.filter(webdetail__webgrant__g_sid_id=sid).values().distinct()
        detail_list = WebDetail.objects.filter(webgrant__g_sid=sid).values().distinct()
        grent_list = WebGrant.objects.filter(g_sid=sid).values().distinct()
        evaluate_list = WebEvaluate.objects.filter(e_did__webevaluate__e_sid=sid).values().distinct()
        teacher_list = WebTeacher.objects.filter(webgrant__g_sid=sid).values().distinct()
        return render(
            request,'m_student.html',
            {
                'course_list':course_list,
                'detail_list':detail_list,
                'grent_list':grent_list,
                'evaluate_list':evaluate_list,
                'teacher_list':teacher_list,
                "stu_obj":stu_obj,
                "role":role,
                "sid_id":sid_id,
                "obj_form": obj_form,
                'location_time':location_time
            }
        )

    else:
        obj_form = Student_to_teacher(request.POST)
        sid = request.POST.get('g_sid_id')
        # print(sid)
        # account = request.session["account"]
        tid = WebGrant.objects.filter(g_sid_id=sid).values_list("g_tid_id")[0][0]
        did = WebGrant.objects.filter(g_sid_id=sid).values_list("g_did_id")[0][0]
        # print( tid, did)
        # print("-" * 120)
        tea_obj = WebTeacher.objects.filter(t_id=tid).first()
        stu_obj = WebStudent.objects.filter(s_id=sid).first()
        det_obj = WebDetail.objects.filter(d_id=did).first()

        # print("-" * 120 )
        # print()
        if obj_form.is_valid():
            # 用户提交的数据
            # print('验证成功：', obj_form.cleaned_data)
            obj_form.cleaned_data["e_sid"] = stu_obj
            obj_form.cleaned_data["e_tid"] = tea_obj
            obj_form.cleaned_data["e_did"] = det_obj
            obj_form.cleaned_data["e_create_time"] = int(obj_form.cleaned_data["e_create_time"])
            # print("-" * 120)
            # print(obj_form)
            WebEvaluate.objects.create(**obj_form.cleaned_data)

            return HttpResponse('评价成功')
        else:
            # print('验证失败：', obj_form.errors)
            return render(request, 'm_student.html', {'obj_form': obj_form})
import time
def editdetail(request):
    show_inf = {'status': True, 'inf': None}
    try:
        d_id = request.POST.get('did')
        # d_name = request.POST.get('d_name')
        # d_number = request.POST.get('d_number')
        # d_time_length = request.POST.get('d_time_length')
        g_time = request.POST.get('data')
        print(g_time)
        timeArray = time.strptime(g_time, "%Y-%m-%dT%H:%M")
        timeStamp = int(time.mktime(timeArray))
        # print(timeStamp)
        # d_cid_id = request.POST.get('d_cid_id'    )
        # d_detail = request.POST.get('d_detail')
        d_remark =request.POST.get('remark')
        if not d_remark:
            d_remark = ""
        # print(d_id, d_create_time, d_remark)
        WebDetail.objects.filter(d_id=d_id).update(
            d_id=d_id,
            d_remark=d_remark,
        )
        WebGrant.objects.filter(g_did_id=d_id).update(
            g_time=timeStamp
        )
    except Exception as e:
        show_inf['status'] = False
        show_inf['inf'] = str(e)

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
    # sid = WebStudent.objects.filter(s_account=account).values("s_id")
    stu_obj = WebStudent.objects.filter(s_account=account).first()
    # evaluate_list = WebEvaluate.objects.filter(e_sid_id=sid).values().distinct()
    # teacher_name = WebTeacher.objects.filter(webgrant__g_sid_id=sid).values_list('t_name').first()
    # detail_name = WebDetail.objects.filter(webgrant__g_sid_id=sid).values_list('d_name').first()

    sid_id = request.GET.get('sid')
    # print(sid_id)
    evaluate_list = WebEvaluate.objects.filter(e_sid_id=sid_id).values().distinct()
    teacher_name = WebTeacher.objects.filter(webevaluate__e_sid_id=sid_id).values().distinct()
    detail_name = WebDetail.objects.filter(webevaluate__e_sid_id=sid_id).values().distinct()

    return render(
        request,
        'm_evaluate.html',
        {
            'evaluate_list':evaluate_list,
            'detail_name':detail_name,
            'teacher_name':teacher_name,
            "role": role,
            "stu_obj": stu_obj,

        })

import json
def m_teacher(request):
    """
    autor:孟浩
    教师端
    :param request:
    :return:
    """
    account = request.session["account"]
    role = request.session.get("role", None)
    tea_obj = WebTeacher.objects.filter(t_account=account).first()
    # print("-"* 120)
    # print(tea_obj)
    tid = WebTeacher.objects.filter(t_account=account).values("t_id")
    course_list = WebCourse.objects.filter(webdetail__webgrant__g_tid=tid).values().distinct()
    student_list = WebStudent.objects.filter(webgrant__g_tid=tid).values().distinct()
    detail_list = WebDetail.objects.filter(webgrant__g_tid_id=tid).values().distinct()
    grent_list = WebGrant.objects.filter(g_tid=tid).values('g_did_id', 'g_url', 'g_time').distinct()

    # print(grent_list)


    return render(request,'m_teacher.html',
                  {
                      'course_list':course_list,
                      'student_list':student_list,
                      'detail_list':detail_list,
                      'grent_list':grent_list,
                      "role": role,
                      "tea_obj":tea_obj,

                  })


#吴家贵
# 通知
from django.db.models import F, Q
import time
def notice(request):
    # 后台读取当前登录用户的相关信息并返回给前台显示
    account = request.session.get("account", None)
    role = request.session.get("role", None)
    stu_obj = WebStudent.objects.filter(s_account=account).first()
    tea_obj = WebTeacher.objects.filter(t_account=account).first()
    s_id = WebStudent.objects.filter(s_account=account).values("s_id")
    s_name = WebStudent.objects.filter(s_account=account).values("s_name")
    g_record = WebGrant.objects.filter(g_sid_id=s_id).values("g_record")
    # print(g_record)
    ret = []
    for i in g_record:
        record = i["g_record"]
        ret1 = WebGrant.objects.filter(Q(g_sid__s_name=s_name) & Q(g_record=record)).values_list("g_record",
                                                                                                 "g_sid__s_name",
                                                                                       "g_did__d_name", "g_time")
        ret.append(ret1)
    # print(ret)
    #
    # for i in ret:
    #     # print(i)
    #     for j in i:
    #         print(j)
    return render(request, "notice.html", locals())


# 帮助
def help(request):
    account = request.session.get("account", None)
    role = request.session.get("role", None)
    stu_obj = WebStudent.objects.filter(s_account=account).first()
    tea_obj = WebTeacher.objects.filter(t_account=account).first()
    return render(request, "help.html", locals())


# 代码工具（暂空）
def tool(request):
    account = request.session.get("account", None)
    role = request.session.get("role", None)
    stu_obj = WebStudent.objects.filter(s_account=account).first()
    tea_obj = WebTeacher.objects.filter(t_account=account).first()
    return render(request, "tool.html", locals())


# 考试（暂空）
def test(request):
    account = request.session.get("account", None)
    role = request.session.get("role", None)
    stu_obj = WebStudent.objects.filter(s_account=account).first()
    tea_obj = WebTeacher.objects.filter(t_account=account).first()
    return render(request, "test.html", locals())


# 文章详情
def article_detail(request, id):
    if request.method == "POST":
        keyword = request.POST.get("keyword")

        article_sea = TArticles.objects.filter()
    article_list = TArticles.objects.all().order_by("-t_createtime")
    print(article_list)
    article_obj = TArticles.objects.filter(s_id=id).first()
    return render(request, 'article_detail.html', locals())


# 文章列表
def article_list(request):
    return render(request, 'article_list.html')

#测试
# def test2(request):
#
#     return render(request, 'test2_html.html')
