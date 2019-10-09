from app.models import modelname
from django import forms
class NewUser(forms.ModelForm):
    class Meta():
        model = modelname
        fields = "__all__"