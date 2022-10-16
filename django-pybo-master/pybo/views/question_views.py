from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

from ..forms import companyForm
from ..models import Company

@login_required(login_url='common:login')
def company_create(request):
    """
    pybo 질문등록
    """
    if request.method == 'POST':
        form = companyForm(request.POST)# companyForm의 subject와 content에는 request.POST로 전달받은 데이터가 저장
        if form.is_valid():
            company = form.save(commit=False)#commit=False라는 옵션을 사용하면 폼에 연결된 모델을 저장하지 않고 생성된 모델 객체만 리턴
            company.author = request.user  # 추가한 속성 author 적용
            company.create_date = timezone.now()
            company.save()
            return redirect('pybo:index')
    else:
        form = companyForm()
    context = {'form': form}
    return render(request, 'pybo/company_form.html', context)

@login_required(login_url='common:login')
def company_modify(request, company_id):
    """
    pybo 질문수정
    """
    company = get_object_or_404(Company, pk=company_id)
    if request.user != company.author:
        messages.error(request, '수정권한이 없습니다')#messages는 장고가 제공하는 함수로 넌필드 오류(non-field error)를 발생시킬 경우에 사용
        return redirect('pybo:detail', company_id=company.id)

    if request.method == "POST": #상세조회 화면에서 "수정" 버튼을 클릭하면 http://localhost:8000/pybo/company/modify/2/ 페이지가 GET 방식으로 호출되어 질문수정 화면이 호출되고 질문수정 화면에서 "저장하기" 버튼을 클릭하면 http://localhost:8000/pybo/company/modify/2/ 페이지가POST 방식으로 호출되어 데이터가 수정
        form = companyForm(request.POST, instance=company) #조회된 질문의 내용으로 companyForm을 생성하지만 request.POST의 값으로 덮어씀.
        if form.is_valid():
            company = form.save(commit=False)
            company.author = request.user
            company.modify_date = timezone.now()  # 수정일시 저장
            company.save()
            return redirect('pybo:detail', company_id=company.id)
    else:
        form = companyForm(instance=company)#폼 생성시 이처럼 instance값을 지정하면 폼에 값이 채워진 상태로 보여짐(기존 제목, 내용).
    context = {'form': form}
    return render(request, 'pybo/company_form.html', context)

@login_required(login_url='common:login')
def company_delete(request, company_id):
    """
    pybo 질문삭제
    """
    company = get_object_or_404(Company, pk=company_id)
    if request.user != company.author:
        messages.error(request, '삭제권한이 없습니다')
        return redirect('pybo:detail', company_id=company.id)
    company.delete()
    return redirect('pybo:index')
