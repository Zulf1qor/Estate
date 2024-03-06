from django.contrib import admin
from . import models
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext, gettext_lazy as _

@admin.register(models.User)
class UserAdmin(UserAdmin):
    list_display = ['id','username', 'first_name', 'last_name', 'is_active']
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'email')}),
        (_('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        (_('Extra'), {'fields': ('gender','phone_number','img','bio','birthday','month_of_birth','born_smelly')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )

admin.site.register(models.Estate)
admin.site.register(models.Cassa)
admin.site.register(models.Customers)
admin.site.register(models.History_contracts)
admin.site.register(models.Location)
admin.site.register(models.Building)
admin.site.register(models.Payment)
admin.site.register(models.PaymentReciept)
admin.site.register(models.Agents)
admin.site.register(models.Meeting)

