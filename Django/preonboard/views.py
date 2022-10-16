# Create your views here.
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

from .forms import JobOpeningForm, CompanyRegisterForm
from preonboard.models import Job_opening, Applicate


def index(request):
    page = request.GET.get('page', '1')  # 페이지
    kw = request.GET.get('kw', '')  # 검색어
    job_opening_list = Job_opening.objects.order_by('-create_date')
    if kw:
        job_opening_list = job_opening_list.filter(
            Q(company__icontains=kw) |  # 회사 이름 검색
            Q(stack__icontains=kw) |  # 사용 기술 검색
            Q(title__icontains=kw)  # 제목 검색
        ).distinct()
    paginator = Paginator(job_opening_list, 10)  # 페이지당 10개씩 보여주기
    page_obj = paginator.get_page(page)
    context = {'job_opening_list': page_obj, 'page': page, 'kw': kw}
    return render(request, 'preonboard/job_opening_list.html', context)


def detail(request, job_opening_id):
    job_opening = get_object_or_404(Job_opening, pk=job_opening_id)  # 404 처리
    page = request.GET.get('page', '1')  # 페이지
    job_opening_list = Job_opening.objects.order_by('-create_date')
    job_opening_list = job_opening_list.filter(
        Q(company__name__icontains=job_opening.company.name)  # 회사 이름 검색한 결과로 필터링
    ).distinct()
    paginator = Paginator(job_opening_list, 10)  # 페이지당 10개씩 보여주기
    page_obj = paginator.get_page(page)
    context = {'job_opening_list': page_obj, 'page': page, 'job_opening': job_opening}
    return render(request, 'preonboard/job_opening_detail.html', context)


@login_required(login_url='common:login')
def apply_list(request):
    applies_list = Applicate.objects.order_by('-create_date')
    return render(request, applies_list)


@login_required(login_url='common:login')
def apply_create(request, job_opening_id):
    job_opening = get_object_or_404(Job_opening, pk=job_opening_id)
    applicate = Applicate(job_opening=job_opening, applicant=request.user, create_date=timezone.now())
    applicate.save()
    return redirect('preonboard:detail', job_opening_id=job_opening_id)


@login_required(login_url='common:login')
def job_opening_create(request):
    if request.method == 'POST':
        Company_form = CompanyRegisterForm(request.POST)
        job_form = JobOpeningForm(request.POST)
        if job_form.is_valid() and Company_form.is_valid():  # 두개의 폼을 동시에 유효성 확인
            Company = Company_form.save(commit=False)
            Company.register = request.user  # Company too
            Company.save()
            Job_opening = job_form.save(commit=False)
            Job_opening.author = request.user
            Job_opening.company = Company #fk Create
            # author 속성에 로그인 계정 저장
            Job_opening.create_date = timezone.now()
            Job_opening.save()

            return redirect('preonboard:index')
    else:
        Company_form = CompanyRegisterForm()
        job_form = JobOpeningForm()
    context = {'job_form': job_form, 'Company_form': Company_form}
    return render(request, 'preonboard/job_opening_form.html', context)


# 회사에 대한 CRUD 는 언급이 안되었으나 회사라는 모델명은 언급되었기에 폼을 두개로 나눠서
# 한번의 submit에 나눠서 저장되게 구현함

@login_required(login_url='common:login')
def job_opening_modify(request, job_opening_id):
    job_opening = get_object_or_404(Job_opening, pk=job_opening_id)
    if request.user != job_opening.author:
        messages.error(request, '수정권한이 없습니다')
        return redirect('preonboard:detail', job_opening_id=job_opening.id)
    if request.method == "POST":
        job_form = JobOpeningForm(request.POST, instance=job_opening)
        if job_form.is_valid():
            job_opening = job_form.save(commit=False)
            job_opening.modify_date = timezone.now()  # 수정일시 저장
            job_opening.save()
            return redirect('preonboard:detail', job_opening_id=job_opening.id)
    else:
        job_form = JobOpeningForm(instance=job_opening)
    context = {'job_form': job_form}
    return render(request, 'preonboard/job_opening_form.html', context)


@login_required(login_url='common:login')
def job_opening_delete(request, job_opening_id):
    job_opening = get_object_or_404(Job_opening, pk=job_opening_id)
    if request.user != job_opening.author:
        messages.error(request, '삭제권한이 없습니다')
        return redirect('preonboard:detail', job_opening_id=job_opening.id)
    job_opening.delete()
    return redirect('preonboard:index')


# Company
@login_required(login_url='common:login')
def apply_list(request):
    applies_list = Applicate.objects.order_by('-create_date')
    return render(request, applies_list)
