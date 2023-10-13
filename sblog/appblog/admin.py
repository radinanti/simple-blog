from django.contrib import admin
from .models import Post,Category,usrpfp,Comment
# Register your models here.
admin.site.register(Post)
admin.site.register(Category)
admin.site.register(usrpfp)
admin.site.register(Comment)