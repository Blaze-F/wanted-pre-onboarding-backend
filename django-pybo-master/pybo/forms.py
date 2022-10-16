from django import forms
from pybo.models import Company, Answer, Comment

#companyForm은 company이라는 모델과 연결된 폼이고 속성으로 subject와 content를 사용한다고 정의
class companyForm(forms.ModelForm): #모델 폼은 모델(Model)과 연결된 폼으로 폼을 저장하면 연결된 모델의 데이터를 저장할 있음.
    class Meta: #Meta 클래스에는 사용할 모델과 모델의 속성을 적어주어야 함.
        model = Company
        fields = ['subject', 'content']

        labels = {
            'subject': '제목',
            'content': '내용',
        }

class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['content']
        labels = {
            'content': '답변내용',
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        labels = {
            'content': '댓글내용',
        }