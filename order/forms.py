from .models import *
from django import forms

class OrderCreateForm(forms.ModelForm):
    class Meta:
        model=Order
        fields = ['first_name', 'last_name', 'email', 'address', 'postal_code', 'city']
        # '__all__'
