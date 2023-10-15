from django.db import models
from django.contrib.auth.models import User


class UserInfo(models.Model):
   user = models.OneToOneField(User, verbose_name=("Kullanıcı"), on_delete=models.CASCADE)
   phone = models.CharField(("Telefon"), max_length=50)
   
   

class Profile(models.Model):
   user = models.ForeignKey(User, verbose_name=("Kullanıcı"), on_delete=models.CASCADE)
   title = models.CharField(("Profil Adı"), max_length=50)
   image = models.FileField(("Profil Resimi"), upload_to='profile', max_length=100)
   kid = models.BooleanField(("Çocuk Profili"))
   plogin = models.BooleanField(("Profile Login"), default=False, null=True)
   
   def __str__(self) -> str:
      return self.title


# user = {username:'berkay', fname...}
# title = "osman"