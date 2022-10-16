from django import forms
from preonboard.models import Job_opening


class JobOpeningForm(forms.ModelForm):
    class Meta:
        model = Job_opening  # 사용할 모델
        fields = ['title', 'company', 'content', 'stack', 'reward']  #모델의 속성
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'company': forms.Textarea(attrs={'class': 'form-control', 'rows': 1}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 8}),
            'stack': forms.Textarea(attrs={'class': 'form-control', 'rows': 8}),
        }