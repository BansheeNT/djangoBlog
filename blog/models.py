# coding:utf8
from __future__ import unicode_literals

from django.db import models
from mdeditor.fields import MDTextField


#年月筛选
class ArticleManager(models.Manager):
    def distinct_date(self):  # 该管理器定义了一个distinct_date方法，目的是找出所有的不同日期
        distinct_date_list = []  # 建立一个列表用来存放不同的日期 年-月
        date_list = self.values('date')  # 根据文章字段date找出所有文章的发布时间
        for date in date_list:  # 对所有日期进行遍历，当然这里会有许多日期是重复的，目的就是找出多少种日期
            date = date['date'].strftime('%Y%m') # 取出一个日期改格式为 ‘xxx年/xxx月 存档’
            if date not in distinct_date_list:
                distinct_date_list.append(date)
        return distinct_date_list

# Create your models here.
class Category(models.Model):
    """
    博客分类
    """
    name = models.CharField('名称',max_length=32)
    class Meta:
        verbose_name = "类别"
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.name

class Tag(models.Model):
    """
    博客标签
    """
    name = models.CharField('名称',max_length=16)
    class Meta:
        verbose_name = "标签"
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.name

class Article(models.Model):
    """
    博客
    """
    title = models.CharField('标题',max_length=72)
    intro = models.CharField('概述',max_length=512,blank=True)
    content = MDTextField('文章正文')
    date = models.DateField('发布日期', auto_now_add=True)
    createdTime = models.DateTimeField('创建时间',auto_now_add=True)
    category = models.ForeignKey(Category,verbose_name='分类',on_delete='CASCADE')
    tags = models.ManyToManyField(Tag,verbose_name='标签')
    objects = ArticleManager()
    class Meta:
        verbose_name = "文章"
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.title

class Comment(models.Model):
    """
    评论
    """
    article = models.ForeignKey(Article,verbose_name='文章',on_delete='CASCADE')
    name = models.CharField('称呼',max_length=16)
    email = models.EmailField('邮箱',blank=True)
    content = models.CharField('内容',max_length=240)
    createdTime = models.DateTimeField('创建时间',auto_now_add=True)
    class Meta:
        verbose_name = "评论"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.content
