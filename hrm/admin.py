from django.contrib import admin
from .models import Department, Employee

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('fullname', 'position', 'department', 'salary', 'phone')
    list_filter = ('department',)
    search_fields = ('fullname', 'position')