from django.contrib import admin
from .models import VerificationCode

@admin.register(VerificationCode)
class VerificationCodeAdmin(admin.ModelAdmin):
    fields = ('engine', 'code')
    list_display = ('engine', 'code')
