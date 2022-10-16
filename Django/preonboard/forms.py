from django import forms
from preonboard.models import Job_opening


class JobOpeningForm(forms.ModelForm):
    class Meta:
        model = Job_opening  # 사용할 모델
        fields = ['title', 'company', 'country', 'location', 'content', 'stack', 'wanted', 'reward']  #모델의 속성
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'country': forms.TextInput(attrs={'class': 'form-control'}),
            'location': forms.TextInput(attrs={'class': 'form-control'}),
            'wanted': forms.TextInput(attrs={'class': 'form-control'}),
            'company': forms.Textarea(attrs={'class': 'form-control', 'rows': 1}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'stack': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'reward': forms.TextInput(attrs={'class': 'form-control'}),
        }