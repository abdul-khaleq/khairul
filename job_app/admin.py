from django.contrib import admin
from job_app.models import EmployeeModel,Comment,Job_seeker

# Register your models here.
admin.site.register(EmployeeModel)
admin.site.register(Comment)
# admin.site.register(Dashboard)
admin.site.register(Job_seeker)
# admin.site.register(DashboardModel)