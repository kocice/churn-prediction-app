# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

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
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()
    first_name = models.CharField(max_length=150)

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


class BankData(models.Model):
    attrition_flag = models.CharField(db_column='Attrition_Flag', max_length=50, blank=True, null=True)  # Field name made lowercase.
    customer_age = models.IntegerField(db_column='Customer_Age', blank=True, null=True)  # Field name made lowercase.
    gender = models.CharField(db_column='Gender', max_length=50, blank=True, null=True)  # Field name made lowercase.
    dependent_count = models.IntegerField(db_column='Dependent_count', blank=True, null=True)  # Field name made lowercase.
    education_level = models.CharField(db_column='Education_Level', max_length=50, blank=True, null=True)  # Field name made lowercase.
    marital_status = models.CharField(db_column='Marital_Status', max_length=50, blank=True, null=True)  # Field name made lowercase.
    income_category = models.CharField(db_column='Income_Category', max_length=50, blank=True, null=True)  # Field name made lowercase.
    card_category = models.CharField(db_column='Card_Category', max_length=50, blank=True, null=True)  # Field name made lowercase.
    months_on_book = models.IntegerField(db_column='Months_on_book', blank=True, null=True)  # Field name made lowercase.
    total_relationship_count = models.IntegerField(db_column='Total_Relationship_Count', blank=True, null=True)  # Field name made lowercase.
    months_inactive_12_mon = models.IntegerField(db_column='Months_Inactive_12_mon', blank=True, null=True)  # Field name made lowercase.
    contacts_count_12_mon = models.IntegerField(db_column='Contacts_Count_12_mon', blank=True, null=True)  # Field name made lowercase.
    credit_limit = models.FloatField(db_column='Credit_Limit', blank=True, null=True)  # Field name made lowercase.
    total_revolving_bal = models.IntegerField(db_column='Total_Revolving_Bal', blank=True, null=True)  # Field name made lowercase.
    avg_open_to_buy = models.FloatField(db_column='Avg_Open_To_Buy', blank=True, null=True)  # Field name made lowercase.
    total_amt_chng_q4_q1 = models.FloatField(db_column='Total_Amt_Chng_Q4_Q1', blank=True, null=True)  # Field name made lowercase.
    total_trans_amt = models.IntegerField(db_column='Total_Trans_Amt', blank=True, null=True)  # Field name made lowercase.
    total_trans_ct = models.IntegerField(db_column='Total_Trans_Ct', blank=True, null=True)  # Field name made lowercase.
    total_ct_chng_q4_q1 = models.FloatField(db_column='Total_Ct_Chng_Q4_Q1', blank=True, null=True)  # Field name made lowercase.
    avg_utilization_ratio = models.FloatField(db_column='Avg_Utilization_Ratio', blank=True, null=True)  # Field name made lowercase.
    id = models.AutoField()
    predict = models.CharField(db_column='Predict', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'bank_data'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    action_flag = models.PositiveSmallIntegerField()

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


class PredBanquePredresults(models.Model):
    age = models.IntegerField()
    total_relationship_count = models.IntegerField()
    contacts_count_12_mon = models.IntegerField()
    total_revolving_bal = models.IntegerField()
    avg_open_to_buy = models.FloatField()
    total_amt_chng_q4_q1 = models.FloatField()
    total_trans_amt = models.FloatField()
    total_trans_ct = models.FloatField()
    total_ct_chng_q4_q1 = models.FloatField()
    classification = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'pred_banque_predresults'

        # action="{% url 'pred_banque:submit_prediction' %}" method="POST"

