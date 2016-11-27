from django.contrib import admin

from .models import Model1, Person, Book, MyAdmin
# Register your models here.
admin.site.register(Model1)
admin.site.register(Book)
admin.site.register(Person)
admin.site.register(MyAdmin)
