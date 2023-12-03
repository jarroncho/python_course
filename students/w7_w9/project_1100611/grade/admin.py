from django.contrib import admin
from .models import Student,grade_list


class grade_listAdmin(admin.ModelAdmin):
    list_display = ('student', '國文', '英文', '數學', '理化')

# Register your models here.
admin.site.register(Student)
admin.site.register(grade_list,grade_listAdmin)

