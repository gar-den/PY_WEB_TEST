from django.contrib import admin
from bookmark.models import Bookmark


# Register your models here.
class BookmarkAdmin(admin.ModelAdmin):
	list_display = ('title', 'url', 'create_date', 'modify_date')


admin.site.register(Bookmark, BookmarkAdmin)
