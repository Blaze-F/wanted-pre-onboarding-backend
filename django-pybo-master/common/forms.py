from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserForm(UserCreationForm):#UserForm은 django.contrib.auth.forms 패키지의 UserCreationForm 클래스를 상속
    email = forms.EmailField(label="이메일")

    class Meta: #UserCreationForm은 is_valid() 함수로 폼 체크시 위 3개 속성을 필수값으로 체크
        model = User
        fields = ("username", "email")