from django import forms

from bingo.models import FieldValue


class NewFieldValuedForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(NewFieldValuedForm, self).__init__(*args, **kwargs)

        self.fields['name'] = forms.CharField(required=True)
        self.fields['description'] = forms.CharField(required=False)
        self.fields['image'] = forms.ImageField(required=False)

    class Meta:
        model = FieldValue
        fields = '__all__'