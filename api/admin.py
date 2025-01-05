from django.contrib import admin

from api.models import Analyses


# Register your models here.
@admin.register(Analyses)
class AnalysesAdmin(admin.ModelAdmin):
    pass