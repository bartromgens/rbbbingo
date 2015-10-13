from django import forms

from bingo.models import FieldValue
from bingo.models import Game


class NewGameForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(NewGameForm, self).__init__(*args, **kwargs)

        self.fields['name'] = forms.CharField(required=True)

    class Meta:
        model = Game
        fields = '__all__'


class NewFieldValuedForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(NewFieldValuedForm, self).__init__(*args, **kwargs)

        self.fields['name'] = forms.CharField(required=True, max_length=20)
        self.fields['description'] = forms.CharField(required=False)
        self.fields['image'] = forms.ImageField(required=False)

    class Meta:
        model = FieldValue
        fields = '__all__'