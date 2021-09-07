from django.db import models


# Create your models here.
class Book(models.Model):

    id = models.AutoField(primary_key=True)  # id 会自动创建,可以手动写入
    title = models.CharField(max_length=32)  # 书籍名称
    price = models.DecimalField(max_digits=5, decimal_places=2)  # 书籍价格
    publish = models.CharField(max_length=32)  # 出版社名称
    pub_date = models.DateField()  # 出版时间


"""
说明：

    1、EmailField 数据类型是邮箱格式，底层继承 CharField，进行了封装，相当于 MySQL 中的 varchar。
    2、Django1.1 版本不需要联级删除：on_delete=models.CASCADE，Django2.2 需要。
    3、一般不需要设置联级更新.
    4、外键在一对多的多中设置：models.ForeignKey("关联类名", on_delete=models.CASCADE)。
    5、OneToOneField = ForeignKey(...，unique=True)设置一对一。
    6、若有模型类存在外键，创建数据时，要先创建外键关联的模型类的数据，
        不然创建包含外键的模型类的数据时，外键的关联模型类的数据会找不到。

表结构
    书籍表 Book：title 、 price 、 pub_date 、 publish（外键，多对一） 、 authors（多对多）
    出版社表 Publish：name 、 city 、 email
    作者表 Author：name 、 age 、 au_detail（一对一）
    作者详情表 AuthorDetail：gender 、 tel 、 addr 、 birthday
"""

class Note(models.Model):
    title = models.CharField(max_length=32)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    pub_date = models.DateField()
    publish = models.ForeignKey('Publish', on_delete=models.CASCADE)
    authors = models.ManyToManyField('Author')


class Publish(models.Model):
    name = models.CharField(max_length=32)
    city = models.CharField(max_length=64)
    email = models.EmailField()


class Author(models.Model):
    name = models.CharField(max_length=32)
    age = models.SmallIntegerField()
    au_detail = models.OneToOneField('AuthorDetail', on_delete=models.CASCADE)


class AuthorDetail(models.Model):
    gender_choices = (
        (0, '女'),
        (1, '男'),
        (2, '保密'),
    )
    gender = models.SmallIntegerField(choices=gender_choices)
    tel = models.CharField(max_length=32)
    addr = models.CharField(max_length=64)
    birthday = models.DateField()


"""
分组查询（annotate）模型
"""


class Emp(models.Model):
    name = models.CharField(max_length=32)
    age = models.IntegerField()
    salary = models.DecimalField(max_digits=8, decimal_places=2)
    dep = models.CharField(max_length=32)
    province = models.CharField(max_length=32)


class Emps(models.Model):
    name = models.CharField(max_length=32)
    age = models.IntegerField()
    salary = models.DecimalField(max_digits=8, decimal_places=2)
    dep = models.ForeignKey('Dep', on_delete=models.CASCADE)
    province = models.CharField(max_length=32)


class Dep(models.Model):
    title = models.CharField(max_length=32)


