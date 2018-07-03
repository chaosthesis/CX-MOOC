from django.db import models
from django.contrib.auth.models import User
#from easy_thumbnails.fields import ThumbnailerImageField

class Passport(models.Model):
    user   = models.OneToOneField(User)
    bio = models.TextField('Short bio')
    
    def __str__(self):
        return self.user.username

User.passport = property(lambda u: Passport.objects.get_or_create(user=u)[0])