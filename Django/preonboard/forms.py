from django import forms
from preonboard.models import Job_opening, Company


class JobOpeningForm(forms.ModelForm):
    class Meta:
        model = Job_opening  # 사용할 모델
        fields = ['title', 'content', 'stack', 'wanted', 'reward']  # 모델의 속성
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'location': forms.TextInput(attrs={'class': 'form-control'}),
            'wanted': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'stack': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'reward': forms.TextInput(attrs={'class': 'form-control'}),
        }


class CompanyRegisterForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ['name', 'country', 'location']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'country': forms.TextInput(attrs={'class': 'form-control'}),
            'location': forms.TextInput(attrs={'class': 'form-control'}),
        }
