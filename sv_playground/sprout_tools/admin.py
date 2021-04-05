from django.contrib import admin
from .models import Video, Folder, Login
from .sprout_api_client import SproutApiClient


def grant_access_to_all(modeladmin, request, queryset, access='all'):
    for login in queryset:
        client = SproutApiClient()
        client.post_access_grants(login.login_id, access)


grant_access_to_all.short_description = 'Grant access to all Videos'


def grant_access_to_beginners(modeladmin, request, queryset, access='beginners'):
    for login in queryset:
        client = SproutApiClient()
        client.post_access_grants(login.login_id, access)


grant_access_to_beginners.short_description = 'Grant access to Beginners Videos'


class LoginAdmin(admin.ModelAdmin):
    list_display = ("email", "login_id")
    search_fields = ("email__startswith", "login_id__startswith")
    actions = [
        grant_access_to_all,
        grant_access_to_beginners,
    ]


admin.site.register(Video)
admin.site.register(Folder)
admin.site.register(Login, LoginAdmin)
