from distutils.command.upload import upload
from email.policy import default
# from unicodedata import category
from django.db import models
from accounts.models import User
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from popit_project import settings
from django.db.models.signals import post_save
#from django.dispatch import receiver
from accounts.models import Category
#from imagekit.models import ProcesssedImageField
#from imagekit.processors import ResizeToFill


'''
# 프로필
class Profile(models.Model):
    # User model 과 One-To-One 연결
    # => User 객체가 생성될 때 같이 연결된 사용자 모델이 같이 생성되게 하는 방법이다. 기존 User 모델에 손상주지 않으면서 새 필드들을 추가할 수 있다.
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete = models.CASCADE) # User 모델과 1:1 관계를 형성해야하므로, OneToOneField 사용
    nickname = models.CharField(max_length = 40, blank = True)
    #profile_image = models.ImageField(blank = True, null = True, upload_to = 'media/images/%Y/%m')
    profile_image = models.ImageField(blank = True, null = True, upload_to = 'uploads')


# receiver를 사용하면 이벤트가 발생할 때를 찾을 수 있다. Save 이벤트가 발생할때마다 create_user_profile와 save_user_profile 를 호출해 User가 생성될때 Profile 모델도 생성되도록한다.
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
'''

# 팝 (게시글)
class Pop(models.Model):
    contents = models.CharField(null = True, max_length = 500) # 팝 내용 (최대 500자)
    likes_count = models.IntegerField(null = True, default = 0) # 좋아요 수
    comments_count = models.IntegerField(null = True, default = 0) # 댓글 수       
    created_at = models.DateTimeField(auto_now_add = True) # 생성 날짜
    writer = models.ForeignKey(User, null = True, on_delete = models.CASCADE) # 해당 팝의 작성자
    foreign_category = models.ForeignKey(Category, null = True, on_delete = models.CASCADE) # 해당 팝의 카테고리 종류
    user_who_like = models.ManyToManyField(User,related_name='user_who_like')

# 댓글
class Comment(models.Model):
    comments = models.CharField(null = True, max_length = 200)
    foregin_pop = models.ForeignKey(Pop, null = True, on_delete = models.CASCADE) # 어느 팝에 종속한 댓글인지
    foregin_user = models.ForeignKey(User, null = True, on_delete = models.CASCADE)
    # on_delete => 참조 객체인 팝이 삭제되면 댓글도 같이 삭제

    def __str__(self):
        return self.comments