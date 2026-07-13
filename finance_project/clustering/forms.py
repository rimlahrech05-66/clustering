from django import forms
from .models import Client

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = [
            "current_age",
            "yearly_income",
            "total_debt",
            "credit_score",
            "num_credit_cards"
        ]