from django.contrib import admin
from websitesetting.models import Setting

# Register Website Setting
class WebsiteSettingAdmin(admin.ModelAdmin):
    list_display = ('site_name', 'site_meta_keywords')
    search_fields = ('site_name', 'site_meta_keywords')


admin.site.register(Setting, WebsiteSettingAdmin)
