from django.contrib import admin

# Register your models here.

from .models.book import Book
from .models.menu import Menu
from .models.author import Author
from .models.category import Category
from .models.publisher import Publisher
admin.site.register(Book)
admin.site.register(Menu)
admin.site.register(Author)
admin.site.register(Category)
admin.site.register(Publisher)
