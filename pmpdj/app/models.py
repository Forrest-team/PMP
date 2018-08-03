# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from datetime import datetime
from django.db import models


class Relationship11(models.Model):
    notice = models.ForeignKey('Notice', models.DO_NOTHING, primary_key=True)
    customer = models.ForeignKey('Customer', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'Relationship_11'
        unique_together = (('notice', 'customer'),)


class Complain(models.Model):
    complain_id = models.AutoField(primary_key=True)
    owner = models.ForeignKey('Owner', models.DO_NOTHING, blank=True, null=True)
    complain_content = models.CharField(max_length=512, blank=True, null=True)
    complain_create_time = models.DateTimeField()
    complain_end_time = models.DateTimeField()
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


class ImgCode(models.Model):
    code = models.CharField(max_length=4, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'imgcode'


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
    m_data = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'money'


class Notice(models.Model):
    notice_id = models.AutoField(primary_key=True)
    comment = models.TextField(blank=True, null=True)
    create_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'notice'


class Orders(models.Model):
    order_id = models.AutoField(primary_key=True)
    owner = models.ForeignKey('Owner', models.DO_NOTHING, blank=True, null=True)
    engineering = models.ForeignKey(Engineering, models.DO_NOTHING, blank=True, null=True)
    customer = models.ForeignKey(Customer, models.DO_NOTHING, blank=True, null=True)
    server_project = models.IntegerField(blank=True, null=True)
    create_time = models.DateTimeField()
    end_time = models.DateTimeField()
    count = models.IntegerField(default=1)
    status = models.IntegerField(default=0)

    def to_dict(self):
        return {
            'order_id ': self.order_id,
            'owner': self.owner,
            'engineering': self.engineering,
            'customer': self.customer,
            'server_project': self.server_project,
            'create_time': self.create_time,
            'end_time': self.end_time,
            'count': self.count,
            'status': self.status
        }

    class Meta:
        managed = False
        db_table = 'orders'


class Owner(models.Model):
    owner_id = models.AutoField(primary_key=True)
    number = models.CharField(max_length=16, unique=True)
    owner_name = models.CharField(max_length=20, blank=True, null=True)
    owner_phone = models.CharField(max_length=11, blank=True, null=True)
    owner_sex = models.IntegerField(blank=True, null=True)
    owner_age = models.IntegerField(blank=True, null=True)
    married = models.IntegerField(blank=True, null=True)
    owner_car = models.IntegerField(blank=True, null=True)
    owner_icon = models.CharField(max_length=256, blank=True, null=True)

    @property
    def to_dict(self):
        return {
            'id': self.owner_id,
            'number': self.number,
            'username': self.owner_name,
            'sex': self.owner_sex,
            'phone': self.owner_phone,
            'car_no': self.owner_car
        }

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


class House(models.Model):
    house_id = models.AutoField(primary_key=True)
    owner = models.ForeignKey(Owner, on_delete=None)
    address = models.CharField(max_length=200)  # 地址
    img = models.CharField(max_length=200)  # 图片
    type = models.IntegerField()  # 租赁或是买卖{0:租赁,1:买卖}
    price = models.FloatField()  # 价格
    acreage = models.IntegerField()  # 房屋面积
    unit = models.CharField(max_length=50)  # 房间单元 如几室几厅
    deposit = models.FloatField(default=0)  # 房屋押金

    @property
    def to_dict(self):
        return {
            'acreage': self.acreage,
            'img': self.img,
            'price': self.price,
            'address': self.address,
            'unit': self.unit,
            'deposit': self.deposit
        }

    class Meta:
        db_table = 'house'


class HouseOrderModel(models.Model):
    id = models.AutoField(primary_key=True)
    house = models.ForeignKey(House, on_delete=None)
    start_time = models.DateTimeField(default=datetime.now())
    days = models.IntegerField(null=True, blank=True)
    status = models.IntegerField(default=0)  # 订单状态{0:待处理,1:处理中,2:处理完毕, 3:拒单, 4:取消}
    reason = models.CharField(max_length=200)

    class Meta:
        db_table = 'house_order'
