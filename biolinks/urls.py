from django.contrib import admin
from django.urls import path, include

from biolinks.views import bio_links_view, FormView, BioLinksListView, BioLinksOwnedByUserListView


urlpatterns = [
    path('', BioLinksListView.as_view(), name='bio_links'),
    path('my/', BioLinksOwnedByUserListView.as_view(), name='bio_links_by_user'),
    # path('', bio_links_view, name='Bio Links home'),
    path('add/', FormView, name='FormView'),
]