from django.contrib import admin

from to_do.models import Task

class TaskAdmin(admin.ModelAdmin):
    list_display = ['id', 'description', 'status', 'due_date']
    list_filter = ['status']
    search_fields = ['description']
    fields = ['description', 'status', 'due_date']
    readonly_fields = []

admin.site.register(Task, TaskAdmin)

