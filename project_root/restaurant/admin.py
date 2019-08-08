from django.contrib import admin

from . import models

class RestaurantAdmin(admin.ModelAdmin):
    class Meta:
        model = models.Restaurnat

class TagAdmin(admin.ModelAdmin):
    class Meta:
        model = models.Tag

class TagMatchAdmin(admin.ModelAdmin):
    class Meta:
        model = models.TagMatch

admin.site.register( models.Restaurnat, RestaurantAdmin)
admin.site.register( models.Tag, TagAdmin)
admin.site.register( models.TagMatch, TagMatchAdmin)
