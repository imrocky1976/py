from django.contrib import admin
from books.models import Author, Publisher, Book
# Register your models here.

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email')
    search_fields = ('first_name', 'last_name')

class BookAdmin(admin.ModelAdmin):
    # 自定义列表
    list_display = ('name', 'publisher', 'publication_date')
    search_fields = ('name',)
    list_filter = ('publisher', 'publication_date')
    ordering = ('-publication_date',)
    #自定义编辑表单
    fields = ('name', 'author', 'publisher', 'publication_date')
    filter_horizontal = ('author',)
    raw_id_fields = ('publisher',)
   
admin.site.register(Author, AuthorAdmin)
admin.site.register(Publisher)
admin.site.register(Book, BookAdmin)