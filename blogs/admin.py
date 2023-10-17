# vim: set fileencoding=utf-8 :
from django.contrib import admin
from django.urls import reverse
from django.utils.http import urlencode
from django.utils.html import format_html

import blogs.models as models


class BlogAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'title',
        'view_author',
        'created_at',
        'updated_at',
    )
    list_filter = (
        'author',
        'created_at',
        'updated_at',
    )
    date_hierarchy = 'created_at'

    search_fields = ('title', 'author__email',)

    fields = ('title', 'summary', 'description', 'author', 'created_at', 'updated_at',)
    readonly_fields = ('created_at', 'updated_at',)

    def view_author(self, obj):
        url = (
            reverse("admin:users_customuser_change", args=(obj.author.id,))
            + "?"
            + urlencode({"author__id": f"{obj.id}"})
        )
        return format_html('<a href="{}"> {}</a>', url, obj.author.email)
    view_author.short_description = "Author"


def _register(model, admin_class):
    admin.site.register(model, admin_class)


_register(models.Blog, BlogAdmin)
