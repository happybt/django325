from django.shortcuts import render, HttpResponse
from . import models
from django.db.models import Avg, Max, Min, Count, Sum, F, Q
from django.shortcuts import render, HttpResponse
from .MyForms import EmpForm
from django.core.exceptions import ValidationError


# Create your views here.
def add_book(request):
    """
    单表实例
    :param request:
    :return:
    """

    """
    方式一：实例化对象后要执行 对象.save() 才能在数据库中新增成功
    方式二：通过 ORM 提供的 objects 提供的方法 create 来实现（推荐）
    """
    # books = models.Book(title="菜鸟教程", price=300, publish="菜鸟出版社", pub_date="2008-8-8")
    # books.save()
    # return HttpResponse("<p>数据添加成功！</p>")

    # books = models.Book.objects.create(title='如来神掌', price=200, publish='功夫出版社', pub_date='2010-10-10')
    # books = models.Book.objects.create(title='POSTGRESQL学习手册', price=200, publish='POSTGRESQL出版社', pub_date='2018-11-27')

    # print(books, type(books))  # Book object
    # return HttpResponse("<p>数据添加成功！</p>")

    """
    查找使用 all() 方法来查询所有内容。
    返回的是 QuerySet 类型数据，类似于 list，里面放的是一个个模型类的对象，可用索引下标取出模型类的对象。
    """
    books = models.Book.objects.all()
    # for i in books:
    #     print(i.title)
    # print(books, type(books))
    # QuerySet类型，类似于list，访问 url 时数据显示在命令行窗口中。

    """
    filter() 方法用于查询符合条件的数据。
    返回的是 QuerySet 类型数据，类似于 list，里面放的是满足条件的模型类的对象，可用索引下标取出模型类的对象。
    pk=3 的意思是主键 primary key=3，相当于 id=3。
    因为 id 在 pycharm 里有特殊含义，是看内存地址的内置函数 id()，因此用 pk。
    """
    # books = models.Book.objects.filter(pk=2)
    # print(books)
    # print('-' * 50)
    # books = models.Book.objects.filter(publish='菜鸟出版社',price=300)
    # print(books, type(books))  # QuerySet类型，类似于list。

    """
    exclude() 方法用于查询不符合条件的数据。
    返回的是 QuerySet 类型数据，类似于 list，里面放的是不满足条件的模型类的对象，可用索引下标取出模型类的对象。
    """
    # books = models.Book.objects.filter(pk=2)
    # print(books)
    # print('-' * 50)
    # books = models.Book.objects.exclude(publish='菜鸟出版社', price=300)
    # print(books, type(books))  # QuerySet类型，类似于list。

    """
    get() 方法用于查询符合条件的返回模型类的对象符合条件的对象只能为一个，
    如果符合筛选条件的对象超过了一个或者没有一个都会抛出错误。
    """
    # books = models.Book.objects.get(pk=2)
    # books = models.Book.objects.get(pk=38)  # 报错，没有符合条件的对象
    # books = models.Book.objects.get(price=200)  # 报错，符合条件的对象超过一个
    # print(books, type(books))

    """
    order_by() 方法用于对查询结果进行排序。
    返回的是 QuerySet类型数据，类似于list，里面放的是排序后的模型类的对象，可用索引下标取出模型类的对象。
    注意：
        a、参数的字段名要加引号。
        b、降序为在字段前面加个负号 -。
    """
    # books_up = models.Book.objects.order_by('price')  # 查询所有，按照价格升序排列
    # books_low = models.Book.objects.order_by('-price')  # 查询所有，按照价格降序排列
    # print(books_up)
    # print(books_low)

    """
    reverse() 方法用于对查询结果进行反转。
    返回的是 QuerySe t类型数据，类似于 list，里面放的是反转后的模型类的对象，可用索引下标取出模型类的对象。
    """
    # 按照价格升序排列：降序再反转
    # books_reverse = models.Book.objects.order_by('-price').reverse
    # print(books_reverse)

    """
    count() 方法用于查询数据的数量返回的数据是整数。
    """
    # books_all = models.Book.objects.count()   # 查询所有数据的数量
    # books_price_200 = models.Book.objects.filter(price=200).count()  # 查询符合条件数据的数量
    # print(books_all)
    # print(books_price_200)

    """
    first() 方法返回第一条数据返回的数据是模型类的对象也可以用索引下标 [0]。
    """
    # books_first = models.Book.objects.first()   # 返回所有数据的第一条数据
    # print(books_first)

    """
    last() 方法返回最后一条数据返回的数据是模型类的对象不能用索引下标 [-1]，ORM 没有逆序索引。
    """
    # books_last = models.Book.objects.last()  # 返回所有数据的最后一条数据
    # print(books_last)

    """
    exists() 方法用于判断查询的结果 QuerySet 列表里是否有数据。
    返回的数据类型是布尔，有为 true，没有为 false。
    注意：判断的数据类型只能为 QuerySet 类型数据，不能为整型和模型类的对象。
    """
    # books_exists = models.Book.objects.exists()
    # print(books_exists)

    # books_count_exists = models.Book.objects.count().exists()
    # 报错，判断的数据类型只能为QuerySet类型数据，不能为整型

    # books_first_exists = models.Book.objects.first().exists()
    # 报错，判断的数据类型只能为QuerySet类型数据，不能为模型类对象

    """
    values() 方法用于查询部分字段的数据。
    返回的是 QuerySet 类型数据，类似于 list，里面不是模型类的对象，而是一个可迭代的字典序列，字典里的键是字段，值是数据。
    注意：
        参数的字段名要加引号
        想要字段名和数据用 values
    """
    # books_values = models.Book.objects.values('pk', 'price')
    # 查询所有的id字段和price字段的数据

    # print(books_values[0]['price'], type(books_values))
    # 得到的是第一条记录的price字段的数据

    """
    values_list() 方法用于查询部分字段的数据。
    返回的是 QuerySet 类型数据，类似于 list，里面不是模型类的对象，而是一个个元组，元组里放的是查询字段对应的数据。
    注意：
        参数的字段名要加引号
        只想要数据用 values_list
    """
    # books = models.Book.objects.values_list('price', 'publish')
    # 查询所有的price字段和publish字段的数据
    # print(books)

    # print(books[0][0], type(books))
    # 得到的是第一条记录的price字段的数据

    """
    distinct() 方法用于对数据进行去重。
    返回的是 QuerySet 类型数据。
    注意：
        对模型类的对象去重没有意义，因为每个对象都是一个不一样的存在。
        distinct() 一般是联合 values 或者 values_list 使用。
    """
    # 查询一共有多少个出版社
    # books = models.Book.objects.values_list('publish')

    # 对模型类的对象去重没有意义，因为每个对象都是一个不一样的存在。
    # books = models.Book.objects.values_list('publish').distinct()

    # 对BOOK数据去重,没有意义
    # books = models.Book.objects.distinct()

    """
    filter() 方法基于双下划线的模糊查询（exclude 同理）。
    注意：filter 中运算符号只能使用等于号 = ，不能使用大于号 > ，小于号 < ，等等其他符号。
    __in 用于读取区间，= 号后面为列表 。
    __gt 大于号 ，= 号后面为数字。
    __lt 小于，=号后面为数字。
    __lte 小于等于，= 号后面为数字。
    __range 在 ... 之间，左闭右闭区间，= 号后面为两个元素的列表。
    __contains 包含，= 号后面为字符串。
    __icontains 不区分大小写的包含，= 号后面为字符串。
    __year 是 DateField 数据类型的年份，= 号后面为数字。
    __month 是DateField 数据类型的月份，= 号后面为数字。
    __day 是DateField 数据类型的天数，= 号后面为数字。
    
    """
    # 查询价格为200或者300的数据
    # books = models.Book.objects.filter(price__in=[200,300])

    # 查询价格大于200的数据
    # books = models.Book.objects.filter(price__gt=200)

    # 查询价格小于300的数据
    # books = models.Book.objects.filter(price__lt=300)

    # 查询价格小于等于300的数据
    # books = models.Book.objects.filter(price__lte=300)

    # 查询价格在200到300之间的数据
    # books = models.Book.objects.filter(price__range=[200, 300])

    # 查询包含字符串的数据
    # books = models.Book.objects.filter(title__contains="菜")

    # 查询数据，不区分大小写
    # books = models.Book.objects.filter(title__icontains="python")  # 不区分大小写

    # 查询出版日期是2008年的数据
    # books = models.Book.objects.filter(pub_date__year=2008)
    # books = models.Book.objects.filter(pub_date__month=10)
    # books = models.Book.objects.filter(pub_date__day=1)

    """
    删除
    方式一：使用模型类的 对象.delete()。
        返回值：元组，第一个元素为受影响的行数
    方式二：使用 QuerySet 类型数据.delete()(推荐)
        返回值：元组，第一个元素为受影响的行数。
    注意：
        a. Django 删除数据时，会模仿 SQL约束 ON DELETE CASCADE 的行为，
            也就是删除一个对象时也会删除与它相关联的外键对象。
        b. delete() 方法是 QuerySet 数据类型的方法，但并不适用于 Manager 本身。
            也就是想要删除所有数据，不能不写 all。
    """
    # books = models.Book.objects.filter(pk=8).first().delete()
    # books = models.Book.objects.filter(pk__in=[1, 2]).delete()

    # books = models.Book.objects.delete()　  # 报错
    # books = models.Book.objects.all().delete()　　  # 删除成功

    """
    修改
    方式一：
        模型类的对象.属性 = 更改的属性值
        模型类的对象.save()
        返回值：编辑的模型类的对象。
    方式二：QuerySet 类型数据.update(字段名=更改的数据)（推荐）
        返回值：整数，受影响的行数
    """
    # books = models.Book.objects.filter(pk=7).first()
    # books.price = 400
    # books.save()

    # books = models.Book.objects.filter(pk__in=[3, 6]).update(price=888)

    return HttpResponse('<p>查询成功</p>')


def add_note(request):
    """
    多表实例
    :param request:
    :return:
    """

    """
    ORM - 添加数据
    一对多(外键 ForeignKey)
        方式一: 传对象的形式，返回值的数据类型是对象，书籍对象。
            步骤：
                a. 获取出版社对象
                b. 给书籍的出版社属性 pulish 传出版社对象
        方式二: 传对象 id 的形式(由于传过来的数据一般是 id,所以传对象 id 是常用的)。
            一对多中，设置外键属性的类(多的表)中，MySQL 中显示的字段名是:外键属性名_id。
            返回值的数据类型是对象，书籍对象。
            步骤：
                a. 获取出版社对象的 id
                b. 给书籍的关联出版社字段 pulish_id 传出版社对象的 id
                
    多对多(ManyToManyField)：在第三张关系表中新增数据
        方式一: 传对象形式，无返回值。
            步骤：
                a. 获取作者对象
                b. 获取书籍对象
                c. 给书籍对象的 authors 属性用 add 方法传作者对象
        方式二: 传对象id形式，无返回值。
            步骤：
                a. 获取作者对象的 id
                b. 获取书籍对象
                c. 给书籍对象的 authors 属性用 add 方法传作者对象的 id
                
    关联管理器(对象调用)
    前提：
        多对多（双向均有关联管理器）
        一对多（只有多的那个类的对象有关联管理器，即反向才有）
    语法格式：
        正向：属性名
        反向：小写类名加 _set
        注意：一对多只能反向
    
    常用方法：
        add()：用于多对多，把指定的模型对象添加到关联对象集（关系表）中。
        注意：add() 在一对多(即外键)中，只能传对象（ *QuerySet数据类型），不能传 id（*[id表]）。
    
    *[ ] 的使用:
        # 方式一：传对象
        # 方式二：传对象 id
    create()：创建一个新的对象，并同时将它添加到关联对象集之中。
        返回新创建的对象。
    remove()：从关联对象集中移除执行的模型对象。
        对于 ForeignKey 对象，这个方法仅在 null=True（可以为空）时存在，无返回值。
    clear()：从关联对象集中移除一切对象，删除关联，不会删除对象。
        对于 ForeignKey 对象，这个方法仅在 null=True（可以为空）时存在。
        无返回值。
    """
    #  获取出版社对象
    # pub_obj = models.Publish.objects.filter(pk=1).first()

    #  给书籍的出版社属性publish传出版社对象
    # note = models.Note.objects.create(title='PYTHON教程', price=300, pub_date='2020-1-1',publish=pub_obj)

    print('-' * 50)
    #  获取出版社对象
    # pub_obj = models.Publish.objects.filter(pk=1).first()

    #  获取出版社对象的id
    # pk = pub_obj.pk
    #  给书籍的关联出版社字段 publish_id 传出版社对象的id
    # note = models.Note.objects.create(title="冲灵剑法", price=100, pub_date="2004-04-04", publish_id=pk)

    # 多对多(ManyToManyField)：在第三张关系表中新增数据
    # 方式一: 传对象形式，无返回值。
    #     步骤：
    #         a. 获取作者对象
    #         b. 获取书籍对象
    #         c. 给书籍对象的 authors 属性用 add 方法传作者对象
    #  获取作者对象
    # chong = models.Author.objects.filter(name="令狐冲").first()
    # ying = models.Author.objects.filter(name="任盈盈").first()
    #  获取书籍对象
    # note = models.Note.objects.filter(title="菜鸟教程").first()
    #  给书籍对象的 authors 属性用 add 方法传作者对象
    # note.authors.add(chong, ying)

    print('-' * 50)
    # 多对多(ManyToManyField)：在第三张关系表中新增数据
    # 方式二: 传对象id形式，无返回值。
    #         步骤：
    #             a. 获取作者对象的 id
    #             b. 获取书籍对象
    #             c. 给书籍对象的 authors 属性用 add 方法传作者对象的 id
    #  获取作者对象
    # chong = models.Author.objects.filter(name="令狐冲").first()
    #  获取作者对象的id
    # pk = chong.pk
    #  获取书籍对象
    # note = models.Note.objects.filter(title="冲灵剑法").first()
    #  给书籍对象的 authors 属性用 add 方法传作者对象的id
    # note.authors.add(pk)
    # print(note, type(note))

    # 关联管理器(对象调用)
    # 前提：
    #     多对多（双向均有关联管理器）
    #     一对多（只有多的那个类的对象有关联管理器，即反向才有）
    # 语法格式：
    #     正向：属性名
    #     反向：小写类名加 _set
    #     注意：一对多只能反向
    # 常用方法：
    #     add()：用于多对多，把指定的模型对象添加到关联对象集（关系表）中。
    #     注意：add() 在一对多(即外键)中，只能传对象（ *QuerySet数据类型），不能传 id（*[id表]）。
    #     *[ ] 的使用:
    #     # 方式一：传对象
    #     # 方式二：传对象 id
    # 方式一：传对象
    # note_obj = models.Note.objects.get(id=10)
    # author_list = models.Author.objects.filter(id__gt=2)
    # note_obj.authors.add(*author_list)  # 将 id 大于2的作者对象添加到这本书的作者集合中

    # 方式二：传对象 id
    # note_obj.authors.add(*[1, 3])  # 将 id=1 和 id=3 的作者对象添加到这本书的作者集合中

    # 反向：小写表名_set

    # 把author任盈盈 加入到《冲灵剑法》的author列表
    # ying = models.Author.objects.filter(name="任盈盈").first()
    # note = models.Note.objects.filter(title="冲灵剑法").first()
    # ying.note_set.add(note)

    # create()：创建一个新的对象，并同时将它添加到关联对象集之中。
    #     返回新创建的对象。

    # pub = models.Publish.objects.filter(name="明教出版社").first()
    # wo = models.Author.objects.filter(name="任我行").first()
    # note = wo.note_set.create(title="吸星大法", price=300, pub_date="1999-9-19", publish=pub)
    # print(note, type(note))

    # remove()：从关联对象集中移除执行的模型对象。
    #     对于 ForeignKey 对象，这个方法仅在 null=True（可以为空）时存在，无返回值。

    # author_obj = models.Author.objects.get(id=1)
    # note_obj = models.Note.objects.get(id=11)
    # author_obj.note_set.remove(note_obj)

    # clear()：从关联对象集中移除一切对象，删除关联，不会删除对象。
    #     对于 ForeignKey 对象，这个方法仅在 null=True（可以为空）时存在。
    #     无返回值。

    #  清空独孤九剑关联的所有作者
    # note = models.Note.objects.filter(title="菜鸟教程").first()
    # note.authors.clear()

    """
    ORM 查询
        基于对象的跨表查询。
        
        正向：属性名称
        反向：小写类名_set
        一对多
        查询主键为 1 的书籍的出版社所在的城市（正向）。
    """
    note = models.Note.objects.filter(pk=10).first()
    res = note.publish.city
    print(res, type(res))

    """
    查询明教出版社出版的书籍名（反向）。
    反向：对象.小写类名_set(pub.book_set) 可以跳转到关联的表(书籍表)。
    pub.note_set.all()：取出书籍表的所有书籍对象，在一个 QuerySet 里，遍历取出一个个书籍对象。
    """
    pub = models.Publish.objects.filter(name='明教出版社').first()
    res = pub.note_set.all()
    for i in res:
        print(i.title)

    """
    一对一
    查询令狐冲的电话（正向）
    正向：对象.属性 (author.au_detail) 可以跳转到关联的表(作者详情表)
    """
    author = models.Author.objects.filter(name='令狐冲').first()
    res = author.au_detail.tel
    print(res, type(res))

    """
    查询所有住址在黑木崖的作者的姓名（反向）。
    一对一的反向，用 对象.小写类名 即可，不用加 _set。
    反向：对象.小写类名(addr.author)可以跳转到关联的表(作者表)。
    """
    addr = models.AuthorDetail.objects.filter(addr="黑木崖").first()
    res = addr.author.name
    print(res, type(res))

    """
    多对多
    菜鸟教程所有作者的名字以及手机号（正向）。
    正向：对象.属性(book.authors)可以跳转到关联的表(作者表)。
    作者表里没有作者电话，因此再次通过对象.属性(i.au_detail)跳转到关联的表（作者详情表）。
    """
    note = models.Note.objects.filter(title="菜鸟教程").first()
    res = note.authors.all()
    for i in res:
        print(i.name, i.au_detail.tel)

    """
    查询任我行出过的所有书籍的名字（反向）。
    """
    author = models.Author.objects.filter(name="任我行").first()
    res = author.note_set.all()
    for i in res:
        print(i.title)

    """
    基于双下划线的跨表查询
    正向：属性名称__跨表的属性名称 反向：小写类名__跨表的属性名称
    一对多
        查询菜鸟出版社出版过的所有书籍的名字与价格。
    """
    res = models.Note.objects.filter(publish__name="菜鸟出版社").values_list("title", "price")

    """
    反向：通过 小写类名__跨表的属性名称（book__title，book__price） 跨表获取数据。
    """

    res = models.Publish.objects.filter(name="菜鸟出版社").values_list("note__title", "note__price")

    """
    多对多
    查询任我行出过的所有书籍的名字。
    
    正向：通过 属性名称__跨表的属性名称(authors__name) 跨表获取数据：
    res = models.Book.objects.filter(authors__name="任我行").values_list("title")
    
    反向：通过 小写类名__跨表的属性名称（book__title） 跨表获取数据：
    res = models.Author.objects.filter(name="任我行").values_list("note__title")
    """
    # 正向：通过属性名称__跨表的属性名称(authors__name)跨表获取数据：
    # res = models.Book.objects.filter(authors__name="任我行").values_list("title")

    # 反向：通过小写类名__跨表的属性名称（book__title） 跨表获取数据：
    # res = models.Author.objects.filter(name="任我行").values_list("note__title")

    """
    一对一
    查询任我行的手机号。
    正向：通过 属性名称__跨表的属性名称(au_detail__tel) 跨表获取数据。
    反向：通过 小写类名__跨表的属性名称（author__name） 跨表获取数据。
    """
    # 正向：通过属性名称__跨表的属性名称(au_detail__tel)跨表获取数据。
    res = models.Author.objects.filter(name="任我行").values_list("au_detail__tel")

    # 反向：通过小写类名__跨表的属性名称（author__name） 跨表获取数据。
    res = models.AuthorDetail.objects.filter(author__name="任我行").values_list("tel")

    return HttpResponse(res)


def add_aggregate(request):
    """
    Django ORM – 多表实例（聚合与分组查询）
    聚合查询（aggregate）
        聚合查询函数是对一组值执行计算，并返回单个值。
        Django 使用聚合查询前要先从 django.db.models 引入 Avg、Max、Min、Count、Sum（首字母大写）。
        from django.db.models import Avg,Max,Min,Count,Sum  #   引入函数

    聚合查询返回值的数据类型是字典。
    聚合函数 aggregate() 是 QuerySet 的一个终止子句， 生成的一个汇总值，相当于 count()。
    使用 aggregate() 后，数据类型就变为字典，不能再使用 QuerySet 数据类型的一些 API 了。
    日期数据类型(DateField)可以用 Max 和 Min。
    返回的字典中：键的名称默认是（属性名称加上__聚合函数名），值是计算出来的聚合值。
    如果要自定义返回字典的键的名称，可以起别名：
    aggregate(别名 = 聚合函数名("属性名称"))

    :param request:
    :return:
    """
    """
    计算所有图书的平均价格
    """
    res = models.Note.objects.aggregate(Avg('price'))

    """
    计算所有图书的数量、最贵价格和最便宜价格:
    """
    res = models.Note.objects.aggregate(c=Count('id'), max=Max('price'), min=Min('price'))

    print(res, type(res))

    return HttpResponse(res)


def add_annotate(request):
    """
    分组查询（annotate）
        分组查询一般会用到聚合函数，所以使用前要先从 django.db.models 引入 Avg,Max,Min,Count,Sum（首字母大写）。
        from django.db.models import Avg,Max,Min,Count,Sum  #   引入函数

    返回值：
        分组后，用 values 取值，则返回值是 QuerySet 数据类型里面为一个个字典；
        分组后，用 values_list 取值，则返回值是 QuerySet 数据类型里面为一个个元组。
        MySQL 中的 limit 相当于 ORM 中的 QuerySet 数据类型的切片。

    注意：
        annotate 里面放聚合函数。
        values 或者 values_list 放在 annotate 前面：
            values 或者 values_list 是声明以什么字段分组，annotate 执行分组。
        values 或者 values_list 放在annotate后面：
            annotate 表示直接以当前表的pk执行分组，values 或者 values_list 表示查询哪些字段，
            并且要将 annotate 里的聚合函数起别名，在 values 或者 values_list 里写其别名。

    :param request:
    :return:
    """

    """
    统计每一个出版社的最便宜的书的价格：
    """
    res = models.Publish.objects.values('name').annotate(in_price=Min('note__price'))
    # res = models.Publish.objects.values('name')

    """
    统计每一本书的作者个数：
    """
    res = models.Note.objects.annotate(c=Count('authors__name')).values('title', 'c')

    """
    统计每一本以"菜"开头的书籍的作者个数：
    """
    res = models.Note.objects.filter(title__startswith='菜').annotate(c=Count('authors__name')).values('title', 'c')

    """
    统计不止一个作者的图书名称：
    """
    res = models.Note.objects.annotate(c=Count('authors__name')).filter(c__gt=0).values('title', 'c')

    """
    根据一本图书作者数量的多少对查询集 QuerySet 进行降序排序:
    """
    res = models.Note.objects.annotate(c=Count('authors__name')).order_by('-c').values('title', 'c')

    """
    查询各个作者出的书的总价格:
    """
    res = models.Author.objects.annotate(all=Sum('note__price')).values('name', 'all')

    return HttpResponse(res)


def add_FQ(request):
    """
    F() 查询
        F() 的实例可以在查询中引用字段，来比较同一个 model 实例中两个不同字段的值。
        之前构造的过滤器都只是将字段值与某个常量做比较，如果想要对两个字段的值做比较，就需要用到 F()。
    使用前要先从 django.db.models 引入 F:
    from django.db.models import F
    用法：
        F("字段名称")
        F 动态获取对象字段的值，可以进行运算。
        Django 支持 F() 对象之间以及 F() 对象和常数之间的加减乘除和取余的操作。
        修改操作（update）也可以使用 F() 函数。

    Q() 查询
        使用前要先从 django.db.models 引入 Q:
        from django.db.models import Q
    用法：
        Q(条件判断)
    例如：
    Q(title__startswith="菜")
        之前构造的过滤器里的多个条件的关系都是 and，如果需要执行更复杂的查询（例如 or 语句），就可以使用 Q 。
        Q 对象可以使用 & | ~ （与 或 非）操作符进行组合。
    优先级从高到低：~ & |。
    可以混合使用 Q 对象和关键字参数，Q 对象和关键字参数是用"and"拼在一起的（即将逗号看成 and ），
    但是 Q 对象必须位于所有关键字参数的前面。


    :param request:
    :return:
    """

    """
    F() : 查询工资大于年龄的人：
    """
    res = models.Emp.objects.filter(salary__gt=F('age')).values('name', 'age')

    """
    F() : 将每一本书的价格提高100元:
    """
    # numeric field overflow
    # DETAIL:  A field with precision 5, scale 2 must round to an absolute value less than 10^3.
    # res = models.Note.objects.update(price=F('price')+100)

    """
    Q() :查询价格大于 350 或者名称以菜开头的书籍的名称和价格。
    """
    res = models.Note.objects.filter(Q(price__gt=350) | Q(title__startswith='菜')).values('title', 'price')

    """
    Q() :查询以"菜"结尾或者不是 2010 年 10 月份的书籍:
    """
    res = models.Note.objects.filter(
        Q(title__endswith='菜') | ~Q(Q(pub_date__year=2010) & Q(pub_date__month=10))).values('title')

    """
    查询出版日期是 2004 或者 1999 年，并且书名中包含有"菜"的书籍。
    Q 对象和关键字混合使用，Q 对象要在所有关键字的前面:
    """
    res = models.Note.objects.filter(Q(Q(pub_date__year=2004) | Q(pub_date__year=1999)), title__contains='菜').values(
        'title')

    return HttpResponse(res)


def add_emp(request):
    if request.method == 'GET':
        form = EmpForm()
        return render(request, '../templates/add_emp.html', {'form': form})
    else:
        form = EmpForm(request.POST)
        if form.is_valid():  # 进行数据校验
            # 校验成功
            data = form.cleaned_data  # 校验成功的值，会放在cleaned_data里。
            data.pop('r_salary')
            print(data)

            models.Emp.objects.create(**data)
            return HttpResponse('ok')
            # return render(request, 'add_emp.html', {'form': form})
        else:
            # 校验失败
            print(form.errors)  # 打印错误信息
            clean_errors = form.errors.get('__all__')
            print(222, clean_errors)
        return render(request, '../templates/add_emp.html', {'form': form, 'clean_errors': clean_errors})
