from django.contrib import admin
from .models import Post

# Register your models here.
#Con esta linea podemos crear porst desde el admin
admin.site.register(Post)
