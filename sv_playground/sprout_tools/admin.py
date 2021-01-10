from django.contrib import admin
from .models import Video, Folder, Login
from .sprout_api_client import SproutApiClient


def grant_access(modeladmin, request, queryset):
    for login in queryset:
        client = SproutApiClient()
        client.post_access_grants(login.login_id)


grant_access.short_description = 'Grant access to all Videos'


class LoginAdmin(admin.ModelAdmin):
    list_display = ("email", "login_id")
    search_fields = ("email__startswith", "login_id__startswith")
    actions = [grant_access, ]
    pass


admin.site.register(Video)
admin.site.register(Folder)
admin.site.register(Login, LoginAdmin)
