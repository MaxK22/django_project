from django.contrib import admin

# Register your models here.
# max
# max12345

from .models import Book, Author

admin.site.register(Book)
admin.site.register(Author)