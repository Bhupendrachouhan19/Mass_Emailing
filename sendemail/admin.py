# One of the most powerful parts of Django is the automatic admin interface. It reads metadata from your models to provide a quick, model-centric interface where trusted users can manage content on your site. The admin’s recommended use is limited to an organization’s internal management tool. It’s not intended for building your entire front end around.

from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Newsletter

# Register your models here.
class EmailAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ['email']

admin.site.register(Newsletter,EmailAdmin)

