from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from CXMOOC_Account.models import Passport


class PassportInline(admin.StackedInline):
    model = Passport
    can_delete = False
    verbose_name_plural = 'passport'


class UserAdmin(UserAdmin):
    inlines = (PassportInline,)
    
    
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
