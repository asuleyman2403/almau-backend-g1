from django.contrib import admin
from my_auth.models import User, ResetPassword
# Register your models here.


class ResetPasswordAdmin(admin.ModelAdmin):
    list_display = ('email', 'token', 'created_at',)


admin.site.register(User)
admin.site.register(ResetPassword, ResetPasswordAdmin)
