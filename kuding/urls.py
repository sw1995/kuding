"""kuding URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url, include
from web import views

# from article import urls as article_urls

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^login/$', views.login),
    url(r'^index/$', views.index),
    url(r'^verify_code/$', views.verify_code),
    url(r'^stu_show/$', views.stu_show),
    url(r'^Teachers_lineup/$', views.Teachers_lineup),
    url(r'^contact/$', views.contact),
    url(r'^news/$', views.news),
    url(r'^class_type/$', views.class_type),
    url('reg/', views.reg),
    url(r'^home/$',views.home),
    # url(r'^home2/$',views.home2),
    url(r'^center/$',views.center),
    url(r'^confirm_center/$',views.confirm_center),
    url(r'^confirm_pwd/$',views.confirm_pwd),
    # url(r'^tes1t/$',views.tes1t),
    url(r'^logout/$',views.logout),
    url(r'^get_code/$', views.get_code),
    url(r'^change_pwd/$', views.change_pwd),
    url(r'^build/$', views.build_index),
    # url(r'^t_info_detail/$',views.t_info_detail),


    # 文章相关
    # url(r'^article/', include(article_urls)),
    url(r'article/(\w+)', views.article_detail),


    # 孟浩
    url(r'^student/$', views.m_student),
    url(r'^teacher/$', views.m_teacher),
    url(r'^evaluate/$', views.m_evaluate),
    url(r'^evaluatestudent/$', views.m_evaluatestudent),
    url(r'^editdetail/$', views.editdetail),


    #吴家贵
    url('notice/$', views.notice),
    url('help/$', views.help),
    url('tool/$', views.tool),
    url('test/$', views.test),

    # 测试
    # url('test2/', views.test2),
]
