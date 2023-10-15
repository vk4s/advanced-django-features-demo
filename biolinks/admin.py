# vim: set fileencoding=utf-8 :
from django.contrib import admin

import biolinks.models as models


class BioLinkAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'name',
        'link',
        'owner',
        'created_at',
        'updated_at',
    )
    list_filter = ('owner', 'created_at', 'updated_at', 'id', 'name', 'link')
    search_fields = ('name',)
    date_hierarchy = 'created_at'


def _register(model, admin_class):
    admin.site.register(model, admin_class)


_register(models.BioLink, BioLinkAdmin)
