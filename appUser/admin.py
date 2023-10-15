from django.contrib import admin
from .models import *
# adminview

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
   '''Admin View for Profile'''

   list_display = ('user','title','kid','id') # adminde hangileri tabloda gözüksün
   list_filter = ('kid',) # listedekileri filtreleme categorisi verir
   list_editable = ('kid','title')
   search_fields = ('user__username','title') # admin paneline arama çubuğu getirir
   # date_hierarchy = '' # tarihe göre seçici zamanlayıcı
   ordering = ('user',) # tabloda sıralama

@admin.register(UserInfo)
class UserInfoAdmin(admin.ModelAdmin):
   '''Admin View for UserInfo'''

   list_display = ('user','phone')