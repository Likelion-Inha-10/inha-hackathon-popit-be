from distutils.command.upload import upload
from email.policy import default
from operator import mod
# from unicodedata import category
from django.db import models
from accounts.models import User,Category
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
# from popit_project import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
#from imagekit.models import ProcesssedImageField
#from imagekit.processors import ResizeToFill

# 팝 (게시글)
class Pop(models.Model):
    contents = models.CharField(null = True, max_length = 500) # 팝 내용 (최대 500자)
    likes_count = models.IntegerField(null = True, default = 0) # 좋아요 수
    comments_count = models.IntegerField(null = True, default = 0) # 댓글 수       
    created_at = models.DateTimeField(auto_now_add = True) # 생성 날짜
    writer = models.ForeignKey(User, null = True, on_delete = models.CASCADE) # 해당 팝의 작성자
    foreign_category = models.ForeignKey(Category, null = True, on_delete = models.CASCADE) # 해당 팝의 카테고리 종류
    user_who_like = models.ManyToManyField(User,related_name='user_who_like',blank=True)
    pop_image = models.ImageField(blank = True, null = True, upload_to = 'popimg')
    save_user = models.ManyToManyField(User,related_name='save_pop',blank=True)

# 댓글
class Comment(models.Model):
    comments = models.CharField(null = True, max_length = 200)
    foregin_pop = models.ForeignKey(Pop, null = True, on_delete = models.CASCADE) # 어느 팝에 종속한 댓글인지
    foregin_user = models.ForeignKey(User, null = True, on_delete = models.CASCADE)
    # on_delete => 참조 객체인 팝이 삭제되면 댓글도 같이 삭제
    user_who_commentlike = models.ManyToManyField(User,related_name='user_who_commentlike',blank=True)

    def __str__(self):
        return self.comments