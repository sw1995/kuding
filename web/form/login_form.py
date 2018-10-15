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


class LoginForm(forms.Form):
    log_account = forms.CharField(
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
    log_password = forms.CharField(
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
            render_value=True
        )
    )
    log_role = forms.ChoiceField(
        choices=((1, u"学生"), (2, u"教师")),
        label="用户角色",
        initial=1,
        widget=forms.widgets.RadioSelect()
    )
