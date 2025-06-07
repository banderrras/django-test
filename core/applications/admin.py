from django.contrib import admin
from .models import ApplicationLog

@admin.register(ApplicationLog)
class ApplicationLogAdmin(admin.ModelAdmin):
    list_display = ('city', 'success', 'message_short', 'timestamp')
    list_filter = ('success', 'timestamp')
    search_fields = ('city', 'message')

    def message_short(self, obj):
        return obj.message[:75] + ('...' if len(obj.message) > 75 else '')
    message_short.short_description = 'Сообщение'
