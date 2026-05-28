from django.contrib import admin

from to_do.models import Task

class TaskAdmin(admin.ModelAdmin):
    list_display = ['id', 'description', 'status', 'due_date','detail_description']
    list_filter = ['status']
    search_fields = ['description']
    fields = ['description','detail_description' ,'status', 'due_date']
    readonly_fields = []

admin.site.register(Task, TaskAdmin)

