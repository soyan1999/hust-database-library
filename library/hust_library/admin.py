from django.contrib import admin
from .models import Book, Store, Loan, Write, Ticket
# Register your models here.

admin.site.register(Book)
admin.site.register(Store)
admin.site.register(Loan)
admin.site.register(Write)
admin.site.register(Ticket)
