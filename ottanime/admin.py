from django.contrib import admin

# for importing all the files form root file form model
from . models import *


# Register your models here.
admin.site.register(CustomUser)
admin.site.register(Profile)
admin.site.register(Movie)
admin.site.register(Video)
