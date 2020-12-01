from django.db import models
# from myvenv.socialaccount.models import SocialAccount
# from accounts.models import SocialAccount




from django.contrib.auth import authenticate
from django.contrib.sites.models import Site
from django.contrib.sites.shortcuts import get_current_site
from django.core.exceptions import PermissionDenied
from django.db import models
from django.utils.crypto import get_random_string
from django.utils.encoding import force_str
from django.utils.translation import gettext_lazy as _
import allauth.app_settings
from allauth.account.models import EmailAddress
from allauth.account.utils import get_next_redirect_url, setup_user_email
from allauth.utils import get_user_model
# Create your models here.
class Post(models.Model):
    B_TYPES = (
        ('A','A형'),
        ('B','B형'),
        ('AB','AB형'),
        ('O','O형'),
        ('Weak-A','Weak-A형'),
        ('Weak-B','Weak-B형'),
        ('RH-','RH-형'),
        ('RH+','RH+형'),
        ('Cis-AB','Cis-AB형'),
        ('MkMk','MkMk형'),
    )

    Regions = (
        ('Gangwon','강원'),
        ('Gyeonggi','경기'),
        ('Gyeongnam','경남'),
        ('Gyeongbuk ','경북'),
        ('Gwangju','광주'),
        ('Daegu','대구'),
        ('Busan','부산'),
        ('Seoul ','서울'),
        ('Incheon','인천'),
        ('Jeonnam','전남'),
        ('Jeonbuk','전북'),
        ('Jeju','제주'),
        ('Chungnam','충남'),
        ('Chungbuk','충북'),
    )

    Post_type = (
        ('Donor','공여자'),
        ('recipient','수혜자'),
    )
    user = models.ForeignKey(allauth.app_settings.USER_MODEL,on_delete=models.CASCADE)
    post_type = models.CharField(max_length= 50, choices= Post_type)
    title = models.CharField(max_length= 200)
    pub_date = models.DateTimeField(auto_now_add=True)
    b_type = models.CharField(max_length=50, choices = B_TYPES)
    body = models.TextField()
    region = models.CharField(max_length= 50, choices=Regions)
