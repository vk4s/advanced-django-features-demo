from django import forms

from biolinks.models import BioLink

class BioLinkForm(forms.ModelForm):
    class Meta:
        model = BioLink
        fields = ('name', 'link', )

    def __init__(self, *args, **kwargs):
        super(BioLinkForm, self).__init__(*args, **kwargs)
        print('-'*10, kwargs)
        # self.fields['owner_id'] = self.request.user.id

