from django.db import models
from Users.models import *
# Create your models here.
class RecordInfos(models.Model):
    id = models.AutoField(primary_key=True)
    content = models.TextField('内容')
    isShared = models.BooleanField('是否分享', default=False)
    created = models.DateTimeField('创建时间', auto_now_add=True)
    label = models.OneToOneField('LabelInfos', on_delete=models.CASCADE, related_name='label_id', null=True, blank=True)
    user = models.ForeignKey(UserInfos, on_delete=models.CASCADE, related_name='userInfo_id')
    students = models.ManyToManyField(StudentInfos, related_name='studentInfo_id', null=True, blank=True)

    def __str__(self):
        self.id

    class Meta:
        verbose_name = '记录表'
        verbose_name_plural = '记录表'


class LabelInfos(models.Model):
    id = models.AutoField(primary_key=True)
    labelName = models.CharField('标签名称', max_length=50)
    fatherLabel = models.ForeignKey('LabelInfos', on_delete=models.CASCADE, null=True, blank=True, related_name='father_id')
    userInfo = models.ForeignKey(UserInfos, on_delete=models.CASCADE, related_name='creater_id')

    def __str__(self):
        self.id

    class Meta:
        verbose_name = '标签列表'
        verbose_name_plural = '标签列表'

class ImgInfos(models.Model):
    id = models.AutoField(primary_key=True)
    imgUrl = models.ImageField('图片地址', upload_to='RecordImg')
    record = models.ForeignKey('RecordInfos', on_delete=models.CASCADE, related_name='recordImg_id')

    def __str__(self):
        self.imgUrl

    class Meta:
        verbose_name = '图片地址'
        verbose_name_plural = '图片地址'