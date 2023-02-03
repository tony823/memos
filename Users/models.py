from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class UserInfos(models.Model):
    id = models.AutoField(primary_key=True)
    nicName = models.CharField('用户昵称', max_length=20)
    roles = models.ManyToManyField('RoleInfos', related_name='role_id')
    authUser = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    #classInfo = models.ManyToManyField('ClassInfos', related_name='jionClass_id')

    def __str__(self):
        return self.nicName

    class Meta:
        verbose_name = '用户信息'
        verbose_name_plural = '用户信息'


ROLERTYPE = (
    ('家长', '家长'),
    ('教师', '教师'),
)


class RoleInfos(models.Model):
    id = models.AutoField(primary_key=True)
    roleName = models.CharField('角色名称', max_length=20, choices=ROLERTYPE)

    def __str__(self):
        return self.roleName

    class Meta:
        verbose_name = '角色信息'
        verbose_name_plural = '角色信息'


class StudentInfos(models.Model):
    id = models.AutoField(primary_key=True)
    studentName = models.CharField('学生姓名', max_length=20)
    userName = models.ManyToManyField('UserInfos', related_name='user_id')


    #classInfo = models.ManyToManyField('ClassInfos', related_name='class_id')

    def __str__(self):
        return self.studentName

    class Meta:
        verbose_name = '学生信息'
        verbose_name_plural = '学生信息'


class ClassInfos(models.Model):
    id = models.AutoField(primary_key=True)
    className = models.CharField('班级名称', max_length=20)
    owner = models.ForeignKey('UserInfos', on_delete=models.SET_NULL, related_name='owner_id', null=True)
    grade = models.ForeignKey('GradeInfos', on_delete=models.CASCADE, related_name='grade_id')

    def __str__(self):
        return self.className

    class Meta:
        verbose_name = '班级信息'
        verbose_name_plural = '班级信息'


class GradeInfos(models.Model):
    id = models.AutoField(primary_key=True)
    gradeName = models.CharField('年级名称', max_length=20)
    schoolInfo = models.ForeignKey('SchoolInfos', on_delete=models.CASCADE, related_name='school_id')

    def __str__(self):
        return self.gradeName

    class Meta:
        verbose_name = '年级信息'
        verbose_name_plural = '年级信息'


SCHOOLTYPE = (
    ('学前', '学前'),
    ('小学', '小学'),
    ('初中', '初中'),
    ('高中', '高中'),
    ('大学', '大学'),
    ('培训机构', '培训机构'),
)


class SchoolInfos(models.Model):
    id = models.AutoField(primary_key=True)
    schoolName = models.CharField('学校名称', max_length=20)
    schoolType = models.CharField('学校类别', max_length=8, choices=SCHOOLTYPE)
    abCode = models.CharField('高德区域编码', max_length=6, null=True, blank=True)
    schoolCode = models.CharField('高德学校ID', max_length=10, null=True, blank=True)

    def __str__(self):
        return self.schoolName

    class Meta:
        verbose_name = '学校信息'
        verbose_name_plural = '学校信息'


class TeacherBindClassList(models.Model):
    id = models.AutoField(primary_key=True)
    teachers = models.ForeignKey('UserInfos', related_name='teacher_id', on_delete=models.CASCADE)
    classes = models.ForeignKey('ClassInfos', related_name='teacherBindClass_id', on_delete=models.CASCADE)
    isProcess = models.BooleanField(default=False)

    def __str__(self):
        return self.id

    class Meta:
        verbose_name = '教师绑定班级信息表'
        verbose_name_plural = '教师绑定班级信息表'


class StudentBindClassList(models.Model):
    id = models.AutoField(primary_key=True)
    students = models.ForeignKey('StudentInfos', related_name='student_id', on_delete=models.CASCADE)
    classes = models.ForeignKey('ClassInfos', related_name='studentBindClass_id', on_delete=models.CASCADE)
    isProcess = models.BooleanField(default=False)

    def __str__(self):
        return self.id

    class Meta:
        verbose_name = '学生绑定班级信息表'
        verbose_name_plural = '学生绑定班级信息表'