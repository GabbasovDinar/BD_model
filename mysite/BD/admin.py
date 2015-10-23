from django.contrib import admin
from .models import User, Project, ProjectUser, Tasks, WorkLogs

class ProjectUserInline(admin.TabularInline):
    model = ProjectUser
    extra = 3
    
class WorkLogsLine(admin.TabularInline):
    model = WorkLogs
    extra = 3
    
class UserAdmin(admin.ModelAdmin):
    fields = ['Name', 'Email']

class ProjectAdmin(admin.ModelAdmin):
    fields = ['NameProject', 'Client']
    inlines = [ProjectUserInline]
    list_display = ('NameProject', 'Client')
    search_fields = ['NameProject']
    
class TasksAdmin(admin.ModelAdmin):
    fields = ['ProjectID', 'ProgrammerID', 'Description']
    inlines = [WorkLogsLine]

     
    

admin.site.register(User, UserAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Tasks, TasksAdmin)