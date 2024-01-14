from django import forms
from .models import Classes


status = {('True', 'Active'), ('False', 'Inactive')}


class Classes_Form(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','placeholder': 'Enter Title'}))
    description = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','placeholder': 'Enter Description'}))
    image = forms.ImageField(label="Choose Image")
    url = forms.URLField(widget=forms.TextInput(attrs={'class': 'form-control','placeholder': 'Enter URL'}))
    status = forms.CharField(widget=forms.Select(choices=status, attrs={'class': 'form-control', 'placeholder': 'Enter Status' }))

    class Meta:
        model = Classes
        fields = ['title', 'description', 'image', 'url', 'status']

