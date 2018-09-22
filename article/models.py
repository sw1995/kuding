from __future__ import unicode_literals

from django.db import models


class Attach(models.Model):
    n_id = models.AutoField(db_column='N_ID', primary_key=True)  # Field name made lowercase.
    s_type = models.CharField(db_column='S_TYPE', max_length=10, blank=True, null=True)  # Field name made lowercase.
    s_path = models.CharField(db_column='S_PATH', max_length=500, blank=True, null=True)  # Field name made lowercase.
    s_name = models.CharField(db_column='S_NAME', max_length=100, blank=True, null=True)  # Field name made lowercase.
    t_term = models.DateTimeField(db_column='T_TERM', blank=True, null=True)  # Field name made lowercase.
    s_remark = models.CharField(db_column='S_REMARK', max_length=500, blank=True,
                                null=True)  # Field name made lowercase.
    s_isuse = models.CharField(db_column='S_ISUSE', max_length=1, blank=True, null=True)  # Field name made lowercase.
    s_creater = models.CharField(db_column='S_CREATER', max_length=20, blank=True,
                                 null=True)  # Field name made lowercase.
    t_createtime = models.DateTimeField(db_column='T_CREATETIME', blank=True, null=True)  # Field name made lowercase.
    s_updater = models.CharField(db_column='S_UPDATER', max_length=20, blank=True,
                                 null=True)  # Field name made lowercase.
    t_updatetime = models.DateTimeField(db_column='T_UPDATETIME', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'attach'
        app_label = "article"


class TArticles(models.Model):
    s_id = models.CharField(db_column='S_ID', primary_key=True, max_length=36)  # Field name made lowercase.
    s_cateno = models.CharField(db_column='S_CATENO', max_length=36, blank=True,
                                null=True)  # Field name made lowercase.
    s_cateid = models.CharField(db_column='S_CATEID', max_length=36, blank=True,
                                null=True)  # Field name made lowercase.
    s_stitle = models.CharField(db_column='S_STITLE', max_length=100, blank=True,
                                null=True)  # Field name made lowercase.
    s_title = models.CharField(db_column='S_TITLE', max_length=100, blank=True, null=True)  # Field name made lowercase.
    s_summary = models.CharField(db_column='S_SUMMARY', max_length=200, blank=True,
                                 null=True)  # Field name made lowercase.
    s_content = models.TextField(db_column='S_CONTENT', blank=True, null=True)  # Field name made lowercase.
    s_imgif = models.CharField(db_column='S_IMGIF', max_length=1, blank=True, null=True)  # Field name made lowercase.
    d_paixu = models.FloatField(db_column='D_PAIXU', blank=True, null=True)  # Field name made lowercase.
    s_imgurl = models.CharField(db_column='S_IMGURL', max_length=255, blank=True,
                                null=True)  # Field name made lowercase.
    s_checked = models.CharField(db_column='S_CHECKED', max_length=1, blank=True,
                                 null=True)  # Field name made lowercase.
    n_readcunt = models.IntegerField(db_column='N_READCUNT', blank=True, null=True)  # Field name made lowercase.
    s_pageurl = models.CharField(db_column='S_PAGEURL', max_length=1000, blank=True,
                                 null=True)  # Field name made lowercase.
    s_remark = models.CharField(db_column='S_REMARK', max_length=500, blank=True,
                                null=True)  # Field name made lowercase.
    s_isuse = models.CharField(db_column='S_ISUSE', max_length=1, blank=True, null=True)  # Field name made lowercase.
    s_creater = models.CharField(db_column='S_CREATER', max_length=20, blank=True,
                                 null=True)  # Field name made lowercase.
    t_createtime = models.DateTimeField(db_column='T_CREATETIME', blank=True, null=True)  # Field name made lowercase.
    t_start = models.DateTimeField(db_column='T_START', blank=True, null=True)  # Field name made lowercase.
    t_stop = models.DateTimeField(db_column='T_STOP', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_articles'
        app_label = "article"


class TUserinfos(models.Model):
    s_id = models.CharField(db_column='S_ID', primary_key=True, max_length=36)  # Field name made lowercase.
    s_acountno = models.CharField(db_column='S_ACOUNTNO', max_length=50, blank=True,
                                  null=True)  # Field name made lowercase.
    s_password = models.CharField(db_column='S_PASSWORD', max_length=100, blank=True,
                                  null=True)  # Field name made lowercase.
    s_name = models.CharField(db_column='S_NAME', max_length=100, blank=True, null=True)  # Field name made lowercase.
    s_tel = models.CharField(db_column='S_TEL', max_length=20, blank=True, null=True)  # Field name made lowercase.
    s_phone = models.CharField(db_column='S_PHONE', max_length=30, blank=True, null=True)  # Field name made lowercase.
    s_email = models.CharField(db_column='S_EMAIL', max_length=100, blank=True, null=True)  # Field name made lowercase.
    s_remark = models.CharField(db_column='S_REMARK', max_length=500, blank=True,
                                null=True)  # Field name made lowercase.
    s_state = models.TextField(db_column='S_STATE', blank=True,
                               null=True)  # Field name made lowercase. This field type is a guess.
    s_usertype = models.CharField(db_column='S_USERTYPE', max_length=10, blank=True,
                                  null=True)  # Field name made lowercase.
    s_orgcode = models.CharField(db_column='S_ORGCODE', max_length=36, blank=True,
                                 null=True)  # Field name made lowercase.
    s_isuse = models.CharField(db_column='S_ISUSE', max_length=1)  # Field name made lowercase.
    s_creater = models.CharField(db_column='S_CREATER', max_length=20)  # Field name made lowercase.
    t_createtime = models.DateTimeField(db_column='T_CREATETIME')  # Field name made lowercase.
    s_updater = models.CharField(db_column='S_UPDATER', max_length=20, blank=True,
                                 null=True)  # Field name made lowercase.
    t_updatetime = models.DateTimeField(db_column='T_UPDATETIME', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_userinfos'
        app_label = "article"


class User(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    username = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user'
        app_label = "article"
