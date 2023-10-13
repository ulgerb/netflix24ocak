from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
   user = models.ForeignKey(User, verbose_name=("Kullanıcı"), on_delete=models.CASCADE)
   title = models.CharField(("Profil Adı"), max_length=50)
   image = models.FileField(("Profil Resimi"), upload_to='profile', max_length=100)
   kid = models.BooleanField(("Çocuk Profili"))
   
   def __str__(self) -> str:
      return self.title

# user = {username:'berkay', fname...}
# title = "osman"