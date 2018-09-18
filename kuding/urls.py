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
from django.conf.urls import url
from web import views

urlpatterns = [
    url('admin/', admin.site.urls),
    url('login/', views.login),
    url('reg/', views.reg),
    url(r'^home/$',views.home),
    # url(r'^home2/$',views.home2),
    url(r'^center/$',views.center),
    url(r'^confirm_center/$',views.confirm_center),
    url(r'^confirm_pwd/$',views.confirm_pwd),
    # url(r'^tes1t/$',views.tes1t),
    url(r'^logout/$',views.logout),

    # 孟浩
    url(r'^student/$', views.m_student),
    url(r'^teacher/$', views.m_teacher),
    url(r'^evaluate/$', views.m_evaluate),
    url(r'^editdetail/$', views.editdetail),


    #吴家贵
    url('notice/$', views.notice),
    url('help/$', views.help),
    url('tool/$', views.tool),
    url('test/$', views.test),
]
