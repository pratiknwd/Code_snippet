from django import forms
from .models import SavedData

class SavedDataForm(forms.ModelForm):
    class Meta:
        model = SavedData
        fields = "__all__"
