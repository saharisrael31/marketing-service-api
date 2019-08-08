from django.contrib import admin

# Register your models here.

from .models import TrafficSourceModel, TrafficSourceGroupingModel

class TrafficSourceAdmin(admin.ModelAdmin):
    class Meta:
        model = TrafficSourceModel


class TrafficSourceGroupingModelAdmin(admin.ModelAdmin):
    class Meta:
        model = TrafficSourceGroupingModel


admin.site.register(TrafficSourceGroupingModel, TrafficSourceGroupingModelAdmin)
admin.site.register(TrafficSourceModel, TrafficSourceAdmin)
