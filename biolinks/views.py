from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.list import ListView

from biolinks.models import BioLink
from biolinks.forms import BioLinkForm
from django.contrib.auth.decorators import login_required

@login_required
def FormView(request):
    if request.method == 'POST':
        form = BioLinkForm(request.POST)
        if form.is_valid():
            form.instance.owner = request.user
            form.instance.save()
            form.save()
            return HttpResponse('New Link Saved')
    else:
        form = BioLinkForm()
        context = {
            'form': form,
        }
    return render(request, 'biolinks/form.html', context)

def bio_links_view(request):
    bio_links = BioLink.objects.all()
    context = {'bio_links': bio_links}
    return render(request, 'biolinks/index.html', context)

class BioLinksListView(ListView):
    model = BioLink
    template_name = 'biolinks/index.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get the context
        context = super(BioLinksListView, self).get_context_data(**kwargs)
        # Create any data and add it to the context
        context['bio_links'] = self.get_queryset()
        return context

class BioLinksOwnedByUserListView(ListView):
    model = BioLink
    template_name = 'biolinks/index.html'

    def get_queryset(self):
        return BioLink.objects.filter(owner=self.request.user)

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get the context
        context = super(BioLinksOwnedByUserListView, self).get_context_data(**kwargs)
        # Create any data and add it to the context
        context['bio_links'] = self.get_queryset()
        return context

