from django.urls import path
from .views import company_views, company_views, answer_views, comment_views, vote_views
#pybo앱 이외의 다른 앱이 프로젝트에 추가 될 경우 서로 다른 앱에서 동일한 URL 별칭을 사용한다면 중복이 발생 -> 네임스페이스선언.
app_name = 'preonboard'

urlpatterns = [  #name으로 별칭사용 url규칙 바뀔경우 일일이 바꿔야함으로 별칭사용, int는 숫자값이 매핑됨을 의미.
    # company_views.py
    path('', base_views.index, name='index'),
    path('<int:company_id>/', base_views.detail, name='detail'),

    # company_views.py
    path('company/create/', company_views.company_create, name='company_create'),
    path('company/modify/<int:company_id>/', company_views.company_modify, name='company_modify'),
    path('company/delete/<int:company_id>/', company_views.company_delete, name='company_delete'),

    # answer_views.py
    path('answer/create/<int:company_id>/', answer_views.answer_create, name='answer_create'),
    path('answer/modify/<int:answer_id>/', answer_views.answer_modify, name='answer_modify'),
    path('answer/delete/<int:answer_id>/', answer_views.answer_delete, name='answer_delete'),

    # comment_views.py
    path('comment/create/company/<int:company_id>/', comment_views.comment_create_company, name='comment_create_company'),
    path('comment/modify/company/<int:comment_id>/', comment_views.comment_modify_company, name='comment_modify_company'),
    path('comment/delete/company/<int:comment_id>/', comment_views.comment_delete_company, name='comment_delete_company'),
    path('comment/create/answer/<int:answer_id>/', comment_views.comment_create_answer, name='comment_create_answer'),
    path('comment/modify/answer/<int:comment_id>/', comment_views.comment_modify_answer, name='comment_modify_answer'),
    path('comment/delete/answer/<int:comment_id>/', comment_views.comment_delete_answer, name='comment_delete_answer'),

    # vote_views.py
    path('vote/company/<int:company_id>/', vote_views.vote_company, name='vote_company'),
    path('vote/answer/<int:answer_id>/', vote_views.vote_answer, name='vote_answer'),
]