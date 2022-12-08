from django import forms 
from users.models import ReviewRating
from store.models import Report

class ReviewForm(forms.ModelForm):
    class Meta:
        model = ReviewRating
        fields= ['subject', 'review', 'rating']

class ReportForm(forms.ModelForm):
    class Meta:
        model = Report
        fields = ['subject', 'body']