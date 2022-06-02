from django.contrib import admin
from .models import Tag, Post


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'id', )
    search_fields = ('title', )
    filter_horizontal = ('tags',)


admin.site.register(Tag)
admin.site.register(Post, PostAdmin)

