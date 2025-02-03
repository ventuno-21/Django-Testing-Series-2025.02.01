from django.contrib import admin
from app_pytest.models import Company

# Register your models here.


class CompanyAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "status",
        "last_update",
    ]
    list_editable = ["status"]
    # list_filter = ['']
    # search_fields = [']
    # raw_id_fields = ['']
    # date_hierarchy = ''
    # ordering = ['']


admin.site.register(Company, CompanyAdmin)
