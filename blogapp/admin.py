from django.contrib import admin
from .models import *

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title','description','url','image_url','add_date')
    search_fields = ('title',)

class PostAdmin(admin.ModelAdmin):
    list_display = ('title','content','url','image_url','cat')
    search_fields = ('title',)
    list_filter = ('cat',)
    list_per_page = 50
    class Media:
        js = ('https://cdn.tiny.cloud/1/no-api-key/tinymce/6/tinymce.min.js',"js/script.js",) 

admin.site.register(Category,CategoryAdmin)
admin.site.register(Post,PostAdmin)