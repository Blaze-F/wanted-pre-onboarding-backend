from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect

from ..models import Company, Answer


@login_required(login_url='common:login')
def vote_company(request, company_id):
    """
    pybo 질문추천등록
    """
    company = get_object_or_404(Company, pk=company_id)
    if request.user == company.author:
        messages.error(request, '본인이 작성한 글은 추천할수 없습니다')
    else:
        company.voter.add(request.user)
    return redirect('pybo:detail', company_id=company.id)

@login_required(login_url='common:login')
def vote_answer(request, answer_id):
    """
    pybo 답글추천등록
    """
    answer = get_object_or_404(Answer, pk=answer_id)
    if request.user == answer.author:
        messages.error(request, '본인이 작성한 글은 추천할수 없습니다')
    else:
        answer.voter.add(request.user)
    return redirect('pybo:detail', company_id=answer.company.id)