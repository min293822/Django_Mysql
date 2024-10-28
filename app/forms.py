from django import forms
from django.contrib.auth.models import User
from .models import Headmaster

class HeadmasterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))
    username = forms.CharField(max_length=150, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}))

    class Meta:
        model = Headmaster
        fields = ['username', 'email', 'age', 'gender', 'degree', 'salary', 'experience', 'photo', 'password']
        
        widgets = {
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'age': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Age'}),
            'gender': forms.Select(attrs={'class': 'form-control'}),
            'degree': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Degree'}),
            'salary': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Salary'}),
            'experience': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Experience'}),
            'photo': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }

    def save(self, commit=True):
        # Create user object
        user = User.objects.create_user(
            username=self.cleaned_data['username'],
            email=self.cleaned_data['email'],
            password=self.cleaned_data['password']
        )
        # Create headmaster instance
        headmaster = super().save(commit=False)
        headmaster.name = user  # Link User instance to Headmaster
        if commit:
            headmaster.save()
        return headmaster
