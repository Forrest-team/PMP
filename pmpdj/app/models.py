# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Relationship10(models.Model):
    customer = models.ForeignKey('Customer', models.DO_NOTHING, primary_key=True)
    notice_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'Relationship_10'
        unique_together = (('customer', 'notice_id'),)


class Complain(models.Model):
    complain_id = models.AutoField(primary_key=True)
    owner = models.ForeignKey('Owner', models.DO_NOTHING, blank=True, null=True)
    complain_content = models.CharField(max_length=512, blank=True, null=True)
    complain_create_time = models.DateTimeField(blank=True, null=True)
    complain_end_time = models.DateTimeField(blank=True, null=True)
    complain_status = models.CharField(max_length=30, blank=True, null=True)
    complain_feedback = models.CharField(max_length=512, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'complain'


class Customer(models.Model):
    customer_id = models.AutoField(primary_key=True)
    customer_name = models.CharField(max_length=20, blank=True, null=True)
    customer_age = models.IntegerField(blank=True, null=True)
    customer_sex = models.IntegerField(blank=True, null=True)
    customer_phone = models.IntegerField(blank=True, null=True)
    customer_salary = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'customer'


class Engineering(models.Model):
    engineering_id = models.AutoField(primary_key=True)
    engineering_name = models.CharField(max_length=20, blank=True, null=True)
    engineering_age = models.IntegerField(blank=True, null=True)
    engineering_sex = models.IntegerField(blank=True, null=True)
    engineering_phone = models.IntegerField(blank=True, null=True)
    engineering_salary = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'engineering'


class Finance(models.Model):
    finance_id = models.AutoField(primary_key=True)
    order = models.ForeignKey('Orders', models.DO_NOTHING, blank=True, null=True)
    finance_name = models.CharField(max_length=20, blank=True, null=True)
    finance_age = models.IntegerField(blank=True, null=True)
    finance_sex = models.IntegerField(blank=True, null=True)
    finance_phone = models.IntegerField(blank=True, null=True)
    finance_salary = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'finance'


class Logistics(models.Model):
    logistics_id = models.AutoField(primary_key=True)
    order = models.ForeignKey('Orders', models.DO_NOTHING, blank=True, null=True)
    logistics_name = models.CharField(max_length=20, blank=True, null=True)
    logistics_age = models.IntegerField(blank=True, null=True)
    logistics_sex = models.IntegerField(blank=True, null=True)
    logistics_phone = models.IntegerField(blank=True, null=True)
    logistics_salary = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'logistics'


class Manage(models.Model):
    manage_id = models.AutoField(primary_key=True)
    order = models.ForeignKey('Orders', models.DO_NOTHING, blank=True, null=True)
    manager_name = models.CharField(max_length=20, blank=True, null=True)
    manage_age = models.IntegerField(blank=True, null=True)
    manage_sex = models.IntegerField(blank=True, null=True)
    manage_phone = models.IntegerField(blank=True, null=True)
    manage_salary = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'manage'


class Manpower(models.Model):
    manpower_id = models.AutoField(primary_key=True)
    order = models.ForeignKey('Orders', models.DO_NOTHING, blank=True, null=True)
    manpower_name = models.CharField(max_length=20, blank=True, null=True)
    manpower_age = models.IntegerField(blank=True, null=True)
    manpower_sex = models.IntegerField(blank=True, null=True)
    manpower_phone = models.IntegerField(blank=True, null=True)
    manpower_salary = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'manpower'


class Money(models.Model):
    money_id = models.AutoField(primary_key=True)
    order = models.ForeignKey('Orders', models.DO_NOTHING, blank=True, null=True)
    costype = models.CharField(max_length=50, blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    m_data = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'money'


class Orders(models.Model):
    order_id = models.AutoField(primary_key=True)
    owner = models.ForeignKey('Owner', models.DO_NOTHING, blank=True, null=True)
    engineering = models.ForeignKey(Engineering, models.DO_NOTHING, blank=True, null=True)
    customer = models.ForeignKey(Customer, models.DO_NOTHING, blank=True, null=True)
    server_project = models.IntegerField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    end_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'orders'


class Owner(models.Model):
    owner_id = models.AutoField(primary_key=True)
    owner_name = models.CharField(max_length=20, blank=True, null=True)
    owner_phone = models.IntegerField(blank=True, null=True)
    owner_sex = models.IntegerField(blank=True, null=True)
    owner_age = models.IntegerField(blank=True, null=True)
    owner_marriage = models.IntegerField(db_column='owner_Marriage', blank=True, null=True)  # Field name made lowercase.
    owner_car = models.IntegerField(blank=True, null=True)
    owner_icon = models.CharField(max_length=256, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'owner'


class Security(models.Model):
    security_id = models.AutoField(primary_key=True)
    order = models.ForeignKey(Orders, models.DO_NOTHING, blank=True, null=True)
    security_name = models.CharField(max_length=20, blank=True, null=True)
    security_age = models.IntegerField(blank=True, null=True)
    security_sex = models.IntegerField(blank=True, null=True)
    security_phone = models.IntegerField(blank=True, null=True)
    security_salary = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'security'
