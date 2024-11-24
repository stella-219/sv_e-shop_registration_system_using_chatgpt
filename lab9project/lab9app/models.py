# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Admin(models.Model):
    user = models.OneToOneField('User', models.DO_NOTHING, db_column='User_ID', primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ADMIN'


class Customer(models.Model):
    user = models.OneToOneField('User', models.DO_NOTHING, db_column='User_ID', primary_key=True)  # Field name made lowercase.
    bank_account = models.CharField(db_column='Bank_Account', max_length=50, blank=True, null=True)  # Field name made lowercase.
    home_address = models.CharField(db_column='Home_Address', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CUSTOMER'


class Delivery(models.Model):
    delivery_id = models.AutoField(db_column='Delivery_ID', primary_key=True)  # Field name made lowercase.
    user = models.ForeignKey('User', models.DO_NOTHING, db_column='User_ID', blank=True, null=True)  # Field name made lowercase.
    order = models.ForeignKey('Orders', models.DO_NOTHING, db_column='Order_ID', blank=True, null=True)  # Field name made lowercase.
    delivery_method = models.CharField(db_column='Delivery_Method', max_length=50, blank=True, null=True)  # Field name made lowercase.
    delivery_address = models.TextField(db_column='Delivery_Address', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DELIVERY'


class FoodBeverage(models.Model):
    product = models.OneToOneField('Products', models.DO_NOTHING, db_column='Product_ID', primary_key=True)  # Field name made lowercase.
    sell_by = models.DateField(db_column='Sell_By', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'FOOD_BEVERAGE'


class GeneralMerchandise(models.Model):
    product = models.OneToOneField('Products', models.DO_NOTHING, db_column='Product_ID', primary_key=True)  # Field name made lowercase.
    color = models.CharField(db_column='Color', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'GENERAL_MERCHANDISE'


class Orders(models.Model):
    order_id = models.AutoField(db_column='Order_ID', primary_key=True)  # Field name made lowercase.
    user = models.ForeignKey('User', models.DO_NOTHING, db_column='User_ID', blank=True, null=True)  # Field name made lowercase.
    order_status = models.CharField(db_column='Order_Status', max_length=11, blank=True, null=True)  # Field name made lowercase.
    order_date = models.DateTimeField(db_column='Order_Date', blank=True, null=True)  # Field name made lowercase.
    total_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)  # Add this line

    class Meta:
        managed = False
        db_table = 'ORDERS'


class OrderItem(models.Model):
    order_item_id = models.AutoField(db_column='Order_Item_ID', primary_key=True)  # Field name made lowercase.
    order = models.ForeignKey(Orders, models.DO_NOTHING, db_column='Order_ID', blank=True, null=True)  # Field name made lowercase.
    product = models.ForeignKey('Products', models.DO_NOTHING, db_column='Product_ID', blank=True, null=True)  # Field name made lowercase.
    quantity = models.IntegerField(db_column='Quantity')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ORDER_ITEM'


class Payment(models.Model):
    payment_id = models.AutoField(db_column='Payment_ID', primary_key=True)  # Field name made lowercase.
    user = models.ForeignKey('User', models.DO_NOTHING, db_column='User_ID', blank=True, null=True)  # Field name made lowercase.
    order = models.ForeignKey(Orders, models.DO_NOTHING, db_column='Order_ID', blank=True, null=True)  # Field name made lowercase.
    order_date = models.DateTimeField(db_column='Order_Date', blank=True, null=True)  # Field name made lowercase.
    total_amount = models.DecimalField(db_column='Total_Amount', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PAYMENT'


class Products(models.Model):
    product_id = models.AutoField(db_column='Product_ID', primary_key=True)  # Field name made lowercase.
    proname = models.CharField(db_column='ProName', max_length=200, blank=True, null=True)  # Field name made lowercase.
    brand = models.CharField(db_column='Brand', max_length=200, blank=True, null=True)  # Field name made lowercase.
    cost = models.DecimalField(db_column='Cost', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    price = models.DecimalField(db_column='Price', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    prodescription = models.TextField(db_column='ProDescription', blank=True, null=True)  # Field name made lowercase.
    category = models.CharField(db_column='Category', max_length=50, blank=True, null=True)  # Field name made lowercase.
    image = models.CharField(db_column='Image', max_length=500, blank=True, null=True)  # Field name made lowercase.
    quantity_available = models.IntegerField(db_column='Quantity_Available', blank=True, null=True)  # Field name made lowercase.
    quantity_sold = models.IntegerField(db_column='Quantity_Sold', blank=True, null=True)  # Field name made lowercase.
    popular_items = models.IntegerField(db_column='Popular_Items', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PRODUCTS'


class Rating(models.Model):
    rate_id = models.AutoField(db_column='Rate_ID', primary_key=True)  # Field name made lowercase.
    comments = models.TextField(db_column='Comments', blank=True, null=True)  # Field name made lowercase.
    product = models.ForeignKey(Products, models.DO_NOTHING, db_column='Product_ID', blank=True, null=True)  # Field name made lowercase.
    user = models.ForeignKey('User', models.DO_NOTHING, db_column='User_ID', blank=True, null=True)  # Field name made lowercase.
    rate_score = models.IntegerField(db_column='Rate_Score', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'RATING'


class User(models.Model):
    user_id = models.AutoField(db_column='User_ID', primary_key=True)  # Field name made lowercase.
    user_name = models.CharField(db_column='User_Name', max_length=100)  # Field name made lowercase.
    phone_number = models.CharField(db_column='Phone_Number', max_length=15, blank=True, null=True)  # Field name made lowercase.
    email_address = models.CharField(db_column='Email_Address', max_length=100, blank=True, null=True)  # Field name made lowercase.
    password = models.CharField(db_column='Password', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'USER'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
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
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
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
    action_flag = models.PositiveSmallIntegerField()
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
    id = models.BigAutoField(primary_key=True)
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
