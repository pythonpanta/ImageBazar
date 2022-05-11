from django.contrib import admin
from .models import Category,Post

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created_on','updated_on')
    list_filter = ("name",)
    search_fields = ['name']

admin.site.register(Category,CategoryAdmin)

class PostAdmin(admin.ModelAdmin):
    list_display = ('id','title','category','imageDisplay','created_on','updated_on')
    list_filter = ("category",)
    search_fields = ['title']
admin.site.register(Post, PostAdmin)
