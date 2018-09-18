from django import forms as dforms
from django.forms import fields
from web import models
from django.forms import widgets

class Student_to_teacher(dforms.Form):
    e_id = fields.CharField(
        required=True,
        label='ID',
        error_messages={},
        widget=widgets.TextInput(attrs={'class': 'form-control'})

    )
    e_ttos_evaluate = fields.CharField(
        required=False,
        label='老师对学生评价',
        widget=widgets.TextInput(attrs={'class': 'form-control'})
    )

    e_stot_evaluate = fields.CharField(
        required=False,
        label='学生对老师评价',
        widget=widgets.TextInput(attrs={'class': 'form-control'})
    )

    e_ttos_score = fields.IntegerField(
        required=False,
        label='老师对学生的打分',
        widget=widgets.TextInput(attrs={'class': 'form-control'})
    )
    e_stot_score = fields.IntegerField(
        required=False,
        label='学生对老师的打分',
        widget=widgets.TextInput(attrs={'class': 'form-control'})
    )

    e_remark = fields.CharField(
        required=False,
        label='备注',
        widget=widgets.TextInput(attrs={'class': 'form-control'})
    )

    e_create_time = fields.IntegerField(
        required=True,
        label = '创建时间',
        widget=widgets.TextInput(attrs={'class': 'form-control'})
    )

    e_tid = fields.IntegerField(
        required=False,
        widget=widgets.Select(attrs={'class': 'form-control'}),
        label = '老师姓名',
    )
    e_sid = fields.IntegerField(
        required=False,
        widget=widgets.Select(attrs={'class': 'form-control'}),
        label = '学生姓名',
    )
    e_did = fields.IntegerField(
        required=False,
        widget=widgets.Select(attrs={'class': 'form-control'}),
        label = '节课程名称',
    )


    def __init__(self, *args, **kwargs):
        super(Student_to_teacher, self).__init__(*args, **kwargs)
        self.fields['e_tid'].widget.choices = models.WebTeacher.objects.values_list('t_id', 't_name')
        self.fields['e_sid'].widget.choices = models.WebStudent.objects.values_list('s_id', 's_name')
        self.fields['e_did'].widget.choices = models.WebDetail.objects.values_list('d_id', 'd_name')