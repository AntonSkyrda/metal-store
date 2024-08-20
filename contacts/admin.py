from django.contrib import admin

from .models import (
    PhoneNumber,
    CallBack,
    WorkSchedule,
    ContactEmail,
)


class CallBackAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone_number', 'email', 'message')
    search_fields = ('name', 'email')


admin.site.register(PhoneNumber)
admin.site.register(CallBack)
admin.site.register(WorkSchedule)
admin.site.register(ContactEmail)
