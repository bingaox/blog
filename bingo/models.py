from django.db import models

# Create your models here.


# Create your models here.
class Article(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length = 100)  #博客题目
    sub_head = models.TextField(max_length=100, blank=True)
    category = models.CharField(max_length = 50, blank = True)  #博客标签
    date_time = models.DateTimeField(auto_now_add = True)  #博客日期
    content = models.TextField(blank = True, null = True)  #博客文章正文

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-date_time']


class AboutMe(models.Model):
    id = models.AutoField(primary_key=True)
    date_time = models.DateField(auto_now_add=True)
    content = models.TextField(blank=True, null=False)

    def __str__(self):
        return self.content

    class Meta:
        ordering = ['-date_time']