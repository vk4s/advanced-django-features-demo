# vim: set fileencoding=utf-8 :
from django.contrib import admin
from django.urls import reverse
from django.utils.http import urlencode
from django.utils.html import format_html

import biolinks.models as models


class BioLinkAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'name',
        'link',
        'view_owner',
        'created_at',
        'updated_at',
    )
    list_filter = ('created_at', 'updated_at', 'owner', )
    search_fields = ('name',)
    date_hierarchy = 'created_at'

    fields = ('name', 'link', 'owner', 'created_at', 'updated_at',)
    readonly_fields = ('created_at', 'updated_at',)

    def view_owner(self, obj):
        url = (
            reverse("admin:users_customuser_change", args=(obj.owner.id,))
            + "?"
            + urlencode({"owner__id": f"{obj.id}"})
        )
        return format_html('<a href="{}"> {}</a>', url, obj.owner.email)
    view_owner.short_description = "Owner"


def _register(model, admin_class):
    admin.site.register(model, admin_class)


_register(models.BioLink, BioLinkAdmin)
