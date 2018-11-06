# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class WebClasses(models.Model):
    c_id = models.CharField(primary_key=True, max_length=36)
    c_name = models.CharField(max_length=100)
    c_time = models.BigIntegerField(blank=True, null=True)
    c_state = models.IntegerField()
    c_remark = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'web_classes'


class WebCourse(models.Model):
    c_id = models.CharField(primary_key=True, max_length=36)
    c_name = models.CharField(max_length=64)
    c_create_time = models.BigIntegerField()
    c_detail = models.CharField(max_length=255, blank=True, null=True)
    c_count = models.IntegerField()
    c_remark = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'web_course'


class WebDetail(models.Model):
    d_id = models.CharField(primary_key=True, max_length=36)
    d_name = models.CharField(max_length=64)
    d_number = models.IntegerField()
    d_time_length = models.IntegerField()
    d_detail = models.CharField(max_length=255, blank=True, null=True)
    d_create_time = models.BigIntegerField(blank=True, null=True)
    d_remark = models.CharField(max_length=255, blank=True, null=True)
    d_cid = models.ForeignKey(WebCourse, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'web_detail'


class WebEvaluate(models.Model):
    e_id = models.CharField(primary_key=True, max_length=36)
    e_ttos_evaluate = models.CharField(max_length=255, blank=True, null=True)
    e_stot_evaluate = models.CharField(max_length=255, blank=True, null=True)
    e_ttos_score = models.IntegerField(blank=True, null=True)
    e_stot_score = models.IntegerField(blank=True, null=True)
    e_remark = models.CharField(max_length=255, blank=True, null=True)
    e_create_time = models.BigIntegerField(blank=True, null=True)
    e_gid = models.ForeignKey('WebGrant', models.DO_NOTHING, unique=True, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'web_evaluate'


class WebGrant(models.Model):
    g_id = models.CharField(primary_key=True, max_length=36)
    g_record = models.CharField(max_length=12)
    g_time = models.BigIntegerField(blank=True, null=True)
    g_url = models.CharField(max_length=1000, blank=True, null=True)
    g_remark = models.CharField(max_length=255, blank=True, null=True)
    g_did = models.ForeignKey(WebDetail, models.DO_NOTHING, blank=True, null=True)
    g_sid = models.ForeignKey('WebStudent', models.DO_NOTHING, blank=True, null=True)
    g_tid = models.ForeignKey('WebTeacher', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'web_grant'


class WebLogsheet(models.Model):
    l_id = models.CharField(primary_key=True, max_length=36)
    l_action = models.CharField(max_length=255)
    l_user_id = models.CharField(max_length=36)
    l_ip = models.CharField(max_length=20)
    l_create_time = models.BigIntegerField()
    l_state = models.CharField(max_length=1)
    l_remark = models.CharField(max_length=255, blank=True, null=True)
    l_sid = models.CharField(max_length=36, blank=True, null=True)
    l_tid = models.CharField(max_length=36, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'web_logsheet'


class WebRelation(models.Model):
    r_id = models.CharField(primary_key=True, max_length=36)
    r_state = models.IntegerField()
    r_remark = models.CharField(max_length=255, blank=True, null=True)
    c_id = models.ForeignKey(WebClasses, models.DO_NOTHING)
    s_id = models.ForeignKey('WebStudent', models.DO_NOTHING)
    t_id = models.ForeignKey('WebTeacher', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'web_relation'


class WebStudent(models.Model):
    s_id = models.CharField(primary_key=True, max_length=36)
    s_account = models.CharField(unique=True, max_length=32)
    s_password = models.CharField(max_length=32)
    s_name = models.CharField(max_length=32)
    s_sex = models.IntegerField()
    s_state = models.IntegerField()
    s_create_time = models.BigIntegerField()
    s_grade = models.CharField(max_length=32, blank=True, null=True)
    s_head_image = models.CharField(max_length=100, blank=True, null=True)
    s_remark = models.CharField(max_length=255, blank=True, null=True)
    s_email = models.CharField(max_length=32, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'web_student'


class WebTeacher(models.Model):
    t_id = models.CharField(primary_key=True, max_length=36)
    t_account = models.CharField(unique=True, max_length=32)
    t_password = models.CharField(max_length=32)
    t_name = models.CharField(max_length=100)
    t_age = models.IntegerField(blank=True, null=True)
    t_sex = models.IntegerField()
    t_state = models.IntegerField()
    t_create_time = models.BigIntegerField()
    t_degree = models.CharField(max_length=32, blank=True, null=True)
    t_detail = models.CharField(max_length=255, blank=True, null=True)
    t_head_image = models.CharField(max_length=100, blank=True, null=True)
    t_remark = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'web_teacher'
