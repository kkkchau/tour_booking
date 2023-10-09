from django import forms
from tours.models import Tour

class TourForm(forms.ModelForm):
    class Meta:
        model = Tour
        fields = ['name', 'description', 'start_date', 'end_date', 'price', 'tour_operator']
