from django import forms
from .models import AdPayment  # Make sure you're using the correct model (AdPayment)

class AdPaymentForm(forms.ModelForm):
    class Meta:
        model = AdPayment
        fields = ['title', 'category', 'description', 'location', 'price', 'image', 'account_holder_name', 'account_number', 'bank']
        widgets = {
            'category': forms.Select(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'rows': 3}),
            'account_holder_name': forms.TextInput(attrs={'class': 'form-control'}),
            'account_number': forms.TextInput(attrs={'class': 'form-control'}),
            'bank': forms.Select(attrs={'class': 'form-control'}),  # This will render the choices as a dropdown
        }

