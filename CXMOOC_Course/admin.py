from django.contrib import admin
from CXMOOC_Course.models import Course, Enrollment, Discuss, Assignment, Submission

#class CourseAdmin(admin.ModelAdmin):
#    prepopulated_fields = {"slug": ("name",)}

admin.site.register(Course)
admin.site.register(Enrollment)
admin.site.register(Discuss)
admin.site.register(Assignment)
admin.site.register(Submission)