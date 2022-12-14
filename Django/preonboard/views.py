# Create your views here.
import objects
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

from .forms import JobOpeningForm, CompanyRegisterForm
from preonboard.models import Job_opening, Applicate, Company


def index(request):
    page = request.GET.get('page', '1')  # 페이지
    kw = request.GET.get('kw', '')  # 검색어
    job_opening_list = Job_opening.objects.order_by('-create_date')
    if kw:
        job_opening_list = job_opening_list.filter(
            Q(company__name__icontains=kw) |  # 회사 이름 검색
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
        Q(company__name__exact=job_opening.company.name)  # 회사 이름 검색한 결과로 필터링
    ).distinct()
    paginator = Paginator(job_opening_list, 10)  # 페이지당 10개씩 보여주기
    page_obj = paginator.get_page(page)
    context = {'job_opening_list': page_obj, 'page': page, 'job_opening': job_opening}
    return render(request, 'preonboard/job_opening_detail.html', context)

#job opening control
@login_required(login_url='common:login')
def job_opening_create(request):
    if request.method == 'POST':
        company_form = CompanyRegisterForm(request.POST)
        job_form = JobOpeningForm(request.POST)
        if job_form.is_valid() and company_form.is_valid():
            Company_saved = company_form.save(commit=False)
            Companies, is_saved = Company.objects.get_or_create(name=Company_saved.name,
                                                                country=Company_saved.country,
                                                                register=request.user,
                                                                location=Company_saved.location)
            Job_opening = job_form.save(commit=False)
            Job_opening.author = request.user
            Job_opening.company = Companies  # fk Create
            # author 속성에 로그인 계정 저장
            Job_opening.create_date = timezone.now()
            Job_opening.save()

            return redirect('preonboard:index')
    else:
        company_form = CompanyRegisterForm()
        job_form = JobOpeningForm()
    context = {'job_form': job_form, 'company_form': company_form}
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

#Apply Control
@login_required(login_url='common:login')
def apply_list(request):
    user = request.user
    applies_list = Applicate.objects.order_by('-create_date')
    filterd = applies_list.filter(
        Q(applicant__id__exact=user.id)
    ).distinct()

    context = {'filterd':filterd}
    return render(request, 'preonboard/job_list.html', context)


@login_required(login_url='common:login')
def apply_create(request, job_opening_id):
    job_opening = get_object_or_404(Job_opening, pk=job_opening_id)
    applicate = Applicate(job_opening=job_opening, applicant=request.user, create_date=timezone.now())
    applicate.save()
    return redirect('preonboard:index')
