from django.contrib import admin
from .models import Borrowing, Return

admin.site.register(Borrowing)
admin.site.register(Return)
