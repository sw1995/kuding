from django.shortcuts import render,HttpResponse,redirect
from web import models
import json
from django.http import JsonResponse


#登陆
def login(request):
    if request.method == "POST":
        user = request.POST.get("user")
        pwd = request.POST.get("pwd")
        stu = models.WebStudent.objects.filter(s_account=user,s_password=pwd)
        tea = models.WebTeacher.objects.filter(t_account=user,t_password=pwd)
        # print("+" * 120)
        # print(stu)
        # print(tea)
        if stu:
            request.session["account"] = user
            request.session["role"] = "student"
            # print(request.session.get("account"))
            # print(request.session.get("role"))
            # role = request.session.get("role")
            return redirect('/home/')
        elif tea:
            request.session["account"] = user
            request.session["role"] = "teacher"
            # role = request.session.get("role")
            # print(request.session.get("account"))
            # print(request.session.get("role"))
            return redirect('/home/')

    return render(request,"login1.html")

#注销(退出登陆)
def logout(request):
    account = request.session.get("account")
    if account:
        del request.session["account"]
    return redirect('/login/')


#注册
#孙新洋
def reg(request):
    return render(request, 'register.html')

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
            #学生
            stu_obj = models.WebStudent.objects.filter(s_account=account).first()
            print(stu_obj)

            # 查找班主任
            teachers = models.WebGrant.objects.filter(g_sid=stu_obj.pk).first()
            # print(teachers)
            t_info_obj = models.WebTeacher.objects.filter(t_id=teachers.g_tid_id).all().values()


            # 查询课程
            course_id_list = models.WebGrant.objects.filter(g_sid=stu_obj.pk).values_list("g_did_id").distinct()
            # print(course_id_list)
            course_list = []
            for course_ids in course_id_list:
                for course_id in course_ids:
                    # print(course_id)
                    course = models.WebDetail.objects.filter(d_id=course_id).first()
                    course_list.append(course)
            # print(course_list)

            return render(request, 'home.html', locals())

        elif role == "teacher":
            #教师
            tea_obj = models.WebTeacher.objects.filter(t_account=account).first()
            # print(tea_obj.pk)
            #查找学生
            student_list = models.WebGrant.objects.filter(g_tid_id=tea_obj.pk).values_list("g_sid_id").distinct()
            # print(student_list)
            s_info_list = []
            # student_list = [("123456789123",'1321','1231')]
            for students in student_list:
                for student in students:
                    s_info = models.WebStudent.objects.filter(s_id=student).first()
                    # print(s_info)
                    s_info_list.append(s_info)
            # print(s_info_list)

            # 查询课程
            course_id_list = models.WebGrant.objects.filter(g_tid=tea_obj.pk).values_list("g_did_id").distinct()
            # print(course_id_list)
            course_list = []
            for course_ids in course_id_list:
                for course_id in course_ids:
                    # print(course_id)
                    course = models.WebDetail.objects.filter(d_id=course_id).first()
                    course_list.append(course)
            # print(course_list)

            return render(request, 'home.html',locals())

    return redirect('/login/')


#个人中心
#孙新洋
def center(request):
    #取当前登陆人的账号和身份
    account = request.session.get("account", None)
    role = request.session.get("role", None)
    stu_obj = models.WebStudent.objects.filter(s_account=account).first()
    tea_obj = models.WebTeacher.objects.filter(t_account=account).first()
    # print(tea_obj)

    #获取排行榜
    stu_rank_obj = models.WebStudent.objects.all().order_by("s_id")
    print(stu_rank_obj)
# print(stu_obj.s_create_time)
    return render(request, 'center.html', locals())


#更改个人信息
#孙新洋
def confirm_center(request):
    if request.method == "POST":
        role = request.session.get("role", None)
        account = request.session.get("account", None)
        ret = {}
        sex = request.POST.get("sex")
        grade = request.POST.get("grade")
        age = request.POST.get("age")
        if role == "student":
            models.WebStudent.objects.filter(s_account=account).update(s_sex=sex,s_grade=grade)
        else:
            models.WebTeacher.objects.filter(t_account=account).update(t_sex=sex, t_age=age)
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

        print(pwd,new_pwd,conf_pwd)

        if role == "student":
            stu_obj = models.WebStudent.objects.filter(s_password=pwd).first()
            if stu_obj:
                if new_pwd == conf_pwd:
                    models.WebStudent.objects.filter(s_account=account).update(s_password=new_pwd)
                    ret["status"] = 1
                    ret["msg"] = "保存成功"
                else:
                    ret["status"] = 0
                    ret["msg"] = "两次输入的密码不正确，请重新输入！"
            else:
                ret["status"] = 0
                ret["msg"] = "旧密码不正确，请重新输入！"
        else:
            tea_obj = models.WebTeacher.objects.filter(t_password=pwd)
            if tea_obj and new_pwd == conf_pwd:
                if new_pwd == conf_pwd:
                    models.WebTeacher.objects.filter(t_account=account).update(t_password=new_pwd)
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

    account = request.session["account"]
    role = request.session.get("role", None)
    sid = models.WebStudent.objects.filter(s_account=account).values("s_id")
    stu_obj = models.WebStudent.objects.filter(s_account=account).first()
    course_list = models.WebCourse.objects.filter(webdetail__webgrant__g_sid_id=sid).values().distinct()
    detail_list = models.WebDetail.objects.filter(webgrant__g_sid=sid).values().distinct()
    grent_list = models.WebGrant.objects.filter(g_sid=sid).values().distinct()
    evaluate_list = models.WebEvaluate.objects.filter(e_did__webevaluate__e_sid=sid).values().distinct()
    teacher_list = models.WebTeacher.objects.filter(webgrant__g_sid=sid).values().distinct()
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
        }
    )


def m_evaluate(request):
    """
    autor:孟浩
    学生评价老师
    :param request:
    :return:评价列表
    """
    account = request.session["account"]
    role = request.session.get("role", None)
    sid = models.WebStudent.objects.filter(s_account=account).values("s_id")
    stu_obj = models.WebStudent.objects.filter(s_account=account).first()
    evaluate_list = models.WebEvaluate.objects.filter(e_sid_id=sid).values().distinct()
    teacher_name = models.WebTeacher.objects.filter(webgrant__g_sid_id=sid).values_list('t_name').first()
    detail_name = models.WebDetail.objects.filter(webgrant__g_sid_id=sid).values_list('d_name').first()
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
    tea_obj = models.WebTeacher.objects.filter(t_account=account).first()
    tid = models.WebTeacher.objects.filter(t_account=account).values("t_id")
    course_list = models.WebCourse.objects.filter(webdetail__webgrant__g_tid=tid).values().distinct()
    student_list = models.WebStudent.objects.filter(webgrant__g_tid=tid).values().distinct()
    detail_list = models.WebDetail.objects.filter(webgrant__g_tid_id=tid).values().distinct()
    grent_list = models.WebGrant.objects.filter(g_tid=tid).values('g_did_id','g_url').distinct()

    print(grent_list)


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
from django.db.models import F, Q
import time


# 通知
def notice(request):
    # 后台读取当前登录用户的相关信息并返回给前台显示
    account = request.session.get("account", None)
    role = request.session.get("role", None)
    stu_obj = models.WebStudent.objects.filter(s_account=account).first()
    tea_obj = models.WebTeacher.objects.filter(t_account=account).first()
    s_id = models.WebStudent.objects.filter(s_account=account).values("s_id")
    s_name = models.WebStudent.objects.filter(s_account=account).values("s_name")
    g_record = models.WebGrant.objects.filter(g_sid_id=s_id).values("g_record")
    # print(g_record)
    ret = []
    for i in g_record:
        record = i["g_record"]
        ret1 = models.WebGrant.objects.filter(Q(g_sid__s_name=s_name) & Q(g_record=record)).values_list("g_record", "g_sid__s_name",
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
    stu_obj = models.WebStudent.objects.filter(s_account=account).first()
    tea_obj = models.WebTeacher.objects.filter(t_account=account).first()
    return render(request, "help.html", locals())


# 代码工具（暂空）
def tool(request):
    account = request.session.get("account", None)
    role = request.session.get("role", None)
    stu_obj = models.WebStudent.objects.filter(s_account=account).first()
    tea_obj = models.WebTeacher.objects.filter(t_account=account).first()
    return render(request, "tool.html", locals())


# 考试（暂空）
def test(request):
    account = request.session.get("account", None)
    role = request.session.get("role", None)
    stu_obj = models.WebStudent.objects.filter(s_account=account).first()
    tea_obj = models.WebTeacher.objects.filter(t_account=account).first()
    return render(request, "test.html", locals())






#测试
def tes1t(request):

    return render(request, 'tes1t.html')