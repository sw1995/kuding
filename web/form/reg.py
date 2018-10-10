from django import forms
# from django.forms import fields
from django.core.exceptions import ValidationError
from django.forms import widgets

# 自定义验证规则
import re


def mobile_validate(value):
    mobile_re = re.compile(r'^(13[0-9]|15[012356789]|17[678]|18[0-9]|14[57])[0-9]{8}$')
    if not mobile_re.match(value):
        raise ValidationError('手机号码格式错误')


class RegForm(forms.Form):
    name = forms.CharField(
        max_length=32,
        label="用户名：",
        error_messages={
            "max_length": "用户名最长为32位",
            "required": "用户名不能为空",
        },
        widget=widgets.TextInput(
            attrs={'placeholder': u'请输入用户名'},
        )
    )
    password = forms.CharField(
        min_length=6,
        max_length=32,
        label="密码：",
        error_messages={
            "min_length": "密码不能少于6位",
            "max_length": "密码最长32位",
            "required": "密码不能为空",
        },
        widget=widgets.PasswordInput(
            attrs={'placeholder': u'请输入密码'},
        )
    )
    re_password = forms.CharField(
        min_length=6,
        max_length=32,
        label="确认密码：",
        error_messages={
            "min_length": "确认密码不能少于6位",
            "max_length": "密码最长32位",
            "required": "确认密码不能为空",
        },
        widget=widgets.PasswordInput(
            attrs={'placeholder': u'请重复输入密码'},
        )
    )
    account = forms.CharField(
        max_length=32,
        label="手机号：",
        validators=[mobile_validate, ],
        error_messages={
            "required": "手机号不能为空",
        },
        widget=widgets.TextInput(
            attrs={'placeholder': u'手机号码'},
        )
    )

    # 对确认密码进行校验
    def clean(self):
        password = self.cleaned_data.get("password")
        re_password = self.cleaned_data.get("re_password")

        if re_password and re_password != password:
            self.add_error("re_password", ValidationError("两次密码不一致"))

        else:
            return self.cleaned_data
