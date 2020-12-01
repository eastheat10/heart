from django import forms
from .models import Works


class WorksForm(forms.ModelForm):
    class Meta:
        model =  Works
        fields =['v_name','v_member','v_point','body']