# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin sqlcustom [app_label]'
# into your database.
from __future__ import unicode_literals

from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup)
    permission = models.ForeignKey('AuthPermission')

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group_id', 'permission_id'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType')
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type_id', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser)
    group = models.ForeignKey(AuthGroup)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user_id', 'group_id'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser)
    permission = models.ForeignKey(AuthPermission)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user_id', 'permission_id'),)


class ControlLuxThreshold(models.Model):
    time = models.DateTimeField()
    g22 = models.IntegerField(db_column='G22', blank=True, null=True)  # Field name made lowercase.
    g23 = models.IntegerField(db_column='G23', blank=True, null=True)  # Field name made lowercase.
    rpi_0 = models.IntegerField(db_column='RPi_0', blank=True, null=True)  # Field name made lowercase.
    g24 = models.IntegerField(db_column='G24', blank=True, null=True)  # Field name made lowercase.
    g25_1 = models.IntegerField(db_column='G25.1', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    g25_2 = models.IntegerField(db_column='G25.2', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    g26_1 = models.IntegerField(db_column='G26.1', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    g26_2 = models.IntegerField(db_column='G26.2', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    g27 = models.IntegerField(db_column='G27', blank=True, null=True)  # Field name made lowercase.
    g31_1 = models.IntegerField(db_column='G31.1', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    g31_2 = models.IntegerField(db_column='G31.2', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    g32_1 = models.IntegerField(db_column='G32.1', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    g32_2 = models.IntegerField(db_column='G32.2', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'control_lux_threshold'


class ControlLuxUpperThreshold(models.Model):
    time = models.DateTimeField()
    g22 = models.IntegerField(db_column='G22', blank=True, null=True)  # Field name made lowercase.
    g23 = models.IntegerField(db_column='G23', blank=True, null=True)  # Field name made lowercase.
    rpi_0 = models.IntegerField(db_column='RPi_0', blank=True, null=True)  # Field name made lowercase.
    g24 = models.IntegerField(db_column='G24', blank=True, null=True)  # Field name made lowercase.
    g25_1 = models.IntegerField(db_column='G25.1', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    g25_2 = models.IntegerField(db_column='G25.2', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    g26_1 = models.IntegerField(db_column='G26.1', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    g26_2 = models.IntegerField(db_column='G26.2', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    g27 = models.IntegerField(db_column='G27', blank=True, null=True)  # Field name made lowercase.
    g31_1 = models.IntegerField(db_column='G31.1', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    g31_2 = models.IntegerField(db_column='G31.2', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    g32_1 = models.IntegerField(db_column='G32.1', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    g32_2 = models.IntegerField(db_column='G32.2', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'control_lux_upper_threshold'


class ControlLuxWLights(models.Model):
    time = models.DateTimeField()
    g22 = models.IntegerField(db_column='G22', blank=True, null=True)  # Field name made lowercase.
    g23 = models.IntegerField(db_column='G23', blank=True, null=True)  # Field name made lowercase.
    rpi_0 = models.IntegerField(db_column='RPi_0', blank=True, null=True)  # Field name made lowercase.
    g24 = models.IntegerField(db_column='G24', blank=True, null=True)  # Field name made lowercase.
    g25_1 = models.IntegerField(db_column='G25.1', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    g25_2 = models.IntegerField(db_column='G25.2', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    g26_1 = models.IntegerField(db_column='G26.1', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    g26_2 = models.IntegerField(db_column='G26.2', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    g27 = models.IntegerField(db_column='G27', blank=True, null=True)  # Field name made lowercase.
    g31_1 = models.IntegerField(db_column='G31.1', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    g31_2 = models.IntegerField(db_column='G31.2', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    g32_1 = models.IntegerField(db_column='G32.1', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    g32_2 = models.IntegerField(db_column='G32.2', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'control_lux_w_lights'


class ControlMode(models.Model):
    time = models.DateTimeField()
    g22 = models.IntegerField(db_column='G22', blank=True, null=True)  # Field name made lowercase.
    g23 = models.IntegerField(db_column='G23', blank=True, null=True)  # Field name made lowercase.
    rpi_0 = models.IntegerField(db_column='RPi_0', blank=True, null=True)  # Field name made lowercase.
    g24 = models.IntegerField(db_column='G24', blank=True, null=True)  # Field name made lowercase.
    g25_1 = models.IntegerField(db_column='G25.1', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    g25_2 = models.IntegerField(db_column='G25.2', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    g26_1 = models.IntegerField(db_column='G26.1', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    g26_2 = models.IntegerField(db_column='G26.2', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    g27 = models.IntegerField(db_column='G27', blank=True, null=True)  # Field name made lowercase.
    g31_1 = models.IntegerField(db_column='G31.1', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    g31_2 = models.IntegerField(db_column='G31.2', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    g32_1 = models.IntegerField(db_column='G32.1', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    g32_2 = models.IntegerField(db_column='G32.2', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'control_mode'


class ControlTd1(models.Model):
    time = models.DateTimeField()
    g22 = models.IntegerField(db_column='G22', blank=True, null=True)  # Field name made lowercase.
    g23 = models.IntegerField(db_column='G23', blank=True, null=True)  # Field name made lowercase.
    rpi_0 = models.IntegerField(db_column='RPi_0', blank=True, null=True)  # Field name made lowercase.
    g24 = models.IntegerField(db_column='G24', blank=True, null=True)  # Field name made lowercase.
    g25_1 = models.IntegerField(db_column='G25.1', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    g25_2 = models.IntegerField(db_column='G25.2', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    g26_1 = models.IntegerField(db_column='G26.1', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    g26_2 = models.IntegerField(db_column='G26.2', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    g27 = models.IntegerField(db_column='G27', blank=True, null=True)  # Field name made lowercase.
    g31_1 = models.IntegerField(db_column='G31.1', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    g31_2 = models.IntegerField(db_column='G31.2', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    g32_1 = models.IntegerField(db_column='G32.1', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    g32_2 = models.IntegerField(db_column='G32.2', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'control_td1'


class ControlTd2(models.Model):
    time = models.DateTimeField()
    g22 = models.IntegerField(db_column='G22', blank=True, null=True)  # Field name made lowercase.
    g23 = models.IntegerField(db_column='G23', blank=True, null=True)  # Field name made lowercase.
    rpi_0 = models.IntegerField(db_column='RPi_0', blank=True, null=True)  # Field name made lowercase.
    g24 = models.IntegerField(db_column='G24', blank=True, null=True)  # Field name made lowercase.
    g25_1 = models.IntegerField(db_column='G25.1', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    g25_2 = models.IntegerField(db_column='G25.2', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    g26_1 = models.IntegerField(db_column='G26.1', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    g26_2 = models.IntegerField(db_column='G26.2', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    g27 = models.IntegerField(db_column='G27', blank=True, null=True)  # Field name made lowercase.
    g31_1 = models.IntegerField(db_column='G31.1', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    g31_2 = models.IntegerField(db_column='G31.2', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    g32_1 = models.IntegerField(db_column='G32.1', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    g32_2 = models.IntegerField(db_column='G32.2', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'control_td2'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', blank=True, null=True)
    user = models.ForeignKey(AuthUser)

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


class LogButton(models.Model):
    time = models.DateTimeField()
    room = models.TextField(blank=True, null=True)
    state = models.IntegerField(blank=True, null=True)
    lux = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'log_button'


class LogControl(models.Model):
    time = models.DateTimeField()
    name = models.TextField(blank=True, null=True)
    ip = models.TextField(blank=True, null=True)
    room = models.TextField(blank=True, null=True)
    lux = models.IntegerField(blank=True, null=True)
    td = models.IntegerField(db_column='TD', blank=True, null=True)  # Field name made lowercase.
    dt = models.IntegerField(blank=True, null=True)
    action = models.TextField(blank=True, null=True)
    occupied = models.IntegerField(blank=True, null=True)
    dark = models.IntegerField(blank=True, null=True)
    bright = models.IntegerField(blank=True, null=True)
    lights = models.IntegerField(blank=True, null=True)
    buttonontime = models.IntegerField(db_column='buttonOnTime', blank=True, null=True)  # Field name made lowercase.
    buttonofftime = models.IntegerField(db_column='buttonOffTime', blank=True, null=True)  # Field name made lowercase.
    trigger = models.TextField(blank=True, null=True)
    mode = models.IntegerField(blank=True, null=True)
    timetaken = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'log_control'


class LogFalseOff(models.Model):
    time = models.DateTimeField()
    room = models.CharField(max_length=255, blank=True, null=True)
    count = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'log_false_off'


class LogLighting(models.Model):
    time = models.DateTimeField()
    g22 = models.IntegerField(db_column='G22', blank=True, null=True)  # Field name made lowercase.
    g23 = models.IntegerField(db_column='G23', blank=True, null=True)  # Field name made lowercase.
    rpi_0 = models.IntegerField(db_column='RPi_0', blank=True, null=True)  # Field name made lowercase.
    g24 = models.IntegerField(db_column='G24', blank=True, null=True)  # Field name made lowercase.
    g25_1 = models.IntegerField(db_column='G25.1', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    g25_2 = models.IntegerField(db_column='G25.2', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    g26_1 = models.IntegerField(db_column='G26.1', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    g26_2 = models.IntegerField(db_column='G26.2', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    g27w = models.IntegerField(db_column='G27W', blank=True, null=True)  # Field name made lowercase.
    g27f = models.IntegerField(db_column='G27F', blank=True, null=True)  # Field name made lowercase.
    g31_1 = models.IntegerField(db_column='G31.1', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    g31_2 = models.IntegerField(db_column='G31.2', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    g32_1 = models.IntegerField(db_column='G32.1', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    g32_2 = models.IntegerField(db_column='G32.2', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'log_lighting'


class LogLiveStatus(models.Model):
    time_of_last_update = models.DateTimeField(blank=True, null=True)
    room = models.TextField(blank=True, null=True)
    occupancy = models.IntegerField(blank=True, null=True)
    lux = models.IntegerField(blank=True, null=True)
    lights = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'log_live_status'


class LogLux(models.Model):
    time = models.DateTimeField()
    g22 = models.IntegerField(db_column='G22', blank=True, null=True)  # Field name made lowercase.
    g23 = models.IntegerField(db_column='G23', blank=True, null=True)  # Field name made lowercase.
    rpi_0 = models.IntegerField(db_column='RPi_0', blank=True, null=True)  # Field name made lowercase.
    g24 = models.IntegerField(db_column='G24', blank=True, null=True)  # Field name made lowercase.
    g25_1 = models.IntegerField(db_column='G25.1', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    g25_2 = models.IntegerField(db_column='G25.2', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    g26_1 = models.IntegerField(db_column='G26.1', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    g26_2 = models.IntegerField(db_column='G26.2', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    g27 = models.IntegerField(db_column='G27', blank=True, null=True)  # Field name made lowercase.
    g31_1 = models.IntegerField(db_column='G31.1', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    g31_2 = models.IntegerField(db_column='G31.2', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    g32_1 = models.IntegerField(db_column='G32.1', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    g32_2 = models.IntegerField(db_column='G32.2', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'log_lux'


class LogLuxThreshold(models.Model):
    time = models.DateTimeField()
    room = models.TextField(blank=True, null=True)
    state = models.IntegerField(blank=True, null=True)
    lux = models.IntegerField(blank=True, null=True)
    index = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'log_lux_threshold'


class LogOccupancy(models.Model):
    time = models.DateTimeField()
    room = models.TextField(blank=True, null=True)
    state = models.IntegerField(blank=True, null=True)
    dsid = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'log_occupancy'


class OccSurveyAdmintext(models.Model):
    index = models.TextField()
    update1 = models.TextField()
    update2 = models.TextField()
    update3 = models.TextField()
    profile = models.TextField()
    comfort = models.TextField()
    control = models.TextField()

    class Meta:
        managed = False
        db_table = 'occ_survey_admintext'


class OccSurveyAnswer(models.Model):
    username = models.CharField(max_length=255)
    answer = models.IntegerField(blank=True, null=True)
    in_date = models.DateTimeField()
    question = models.ForeignKey('OccSurveyQuestion')
    answer_text = models.TextField()

    class Meta:
        managed = False
        db_table = 'occ_survey_answer'


class OccSurveyChoice(models.Model):
    name = models.CharField(unique=True, max_length=30)
    type = models.CharField(max_length=10)
    choice1 = models.CharField(max_length=30, blank=True, null=True)
    choice2 = models.CharField(max_length=30, blank=True, null=True)
    choice3 = models.CharField(max_length=30, blank=True, null=True)
    choice4 = models.CharField(max_length=30, blank=True, null=True)
    choice5 = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'occ_survey_choice'


class OccSurveyQuestion(models.Model):
    date_updated = models.DateTimeField()
    question_text = models.CharField(max_length=255)
    question_cat = models.CharField(max_length=255)
    order = models.IntegerField()
    choice = models.ForeignKey(OccSurveyChoice, blank=True, null=True)
    choice_name = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'occ_survey_question'


class OccSurveyUserprofile(models.Model):
    room = models.CharField(max_length=10)
    profile_isdone = models.IntegerField(db_column='profile_isDone')  # Field name made lowercase.
    impromptu_count = models.IntegerField()
    remote_use_count = models.IntegerField()
    user = models.ForeignKey(AuthUser, unique=True)
    username = models.CharField(max_length=20)
    comfort_isdone = models.IntegerField(db_column='comfort_isDone')  # Field name made lowercase.
    control_isdone = models.IntegerField(db_column='control_isDone')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'occ_survey_userprofile'


class Structure(models.Model):
    name = models.TextField(blank=True, null=True)
    room = models.TextField(blank=True, null=True)
    location = models.TextField(blank=True, null=True)
    ip = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'structure'


class StructureDevices(models.Model):
    room = models.TextField(blank=True, null=True)
    device_name = models.TextField(blank=True, null=True)
    device_id = models.TextField(blank=True, null=True)
    device_type = models.TextField(blank=True, null=True)
    other_info = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'structure_devices'
