from django import forms 
from users.models import ReviewRating

class ReviewForm(forms.ModelForm):
    class Meta:
        model = ReviewRating
        fields= ['subject', 'review', 'rating']
        