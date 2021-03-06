from django import forms
from django.utils.translation import ugettext_lazy as _

from core.forms.widgets import MultipleChoiceFilterWidget
from bundles.models import Bundle


class BundleCreateForm(forms.ModelForm):
    """Form used to create a new bundle."""

    class Meta:
        model = Bundle
        fields = ['name']


class BookmarkForm(forms.Form):
    bundles = forms.ModelMultipleChoiceField(
        label=_('Add this aid to the following bundles:'),
        queryset=None,
        required=False,
        widget=MultipleChoiceFilterWidget)

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        self.user_bundles = kwargs.pop('bundles')
        super().__init__(*args, **kwargs)

        self.fields['bundles'].queryset = self.user_bundles
