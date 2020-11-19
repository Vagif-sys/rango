from django import forms
from.models import Customer

class CustForm(forms.ModelForm):
    class Meta:
        model=Customer
        fields = ('name','phone','email','date_created',)