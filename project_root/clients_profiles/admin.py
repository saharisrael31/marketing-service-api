from django.contrib import admin

from .models import Account, Profile

class AccountAdmin(admin.ModelAdmin):
    class Meta:
        model = Account

class ProfileAdmin(admin.ModelAdmin):
    class Meta:
        model = Profile

admin.site.register(Account, AccountAdmin)
admin.site.register(Profile, ProfileAdmin)