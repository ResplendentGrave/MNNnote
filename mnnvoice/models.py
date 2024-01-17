from django.db import models

# Create your models here.
class Lecture(models.Model):
    title = models.CharField("课程名称", max_length=50,null=False)

class Note(models.Model):
    id = models.AutoField('noteID',primary_key=True)
    createTime = models.CharField("上传时间",db_column="create_time",max_length=50)
    title = models.CharField("笔记标题", max_length=50,null=False)
    lecture = models.ForeignKey(Lecture , on_delete=models.CASCADE)

class Voice(models.Model):
    comment = models.CharField("评论", max_length=150)
    createTime = models.CharField("上传时间",db_column="create_time",max_length=50)
    lecture = models.ForeignKey(Lecture, on_delete=models.CASCADE)

