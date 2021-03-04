from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length = 20, verbose_name="아이디")
    password = models.CharField(max_length = 20, verbose_name="비밀번호")

    def __str__(self):
        return self.username
    class Meta:
        db_table = "users"

class BoardMember(models.Model):
    username = models.CharField(max_length=100, verbose_name="유저ID")
    email = models.EmailField(max_length=100, verbose_name='유저메일')
    password = models.CharField(max_length=100, verbose_name='유저PW')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='가입날짜')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='마지막 수정일')

    def __str__(self):
        return self.username

    class Meta:
        db_table = "boardmembers"
        verbose_name = "게시판 멤버"
        verbose_name_plural = "게시판 멤버"