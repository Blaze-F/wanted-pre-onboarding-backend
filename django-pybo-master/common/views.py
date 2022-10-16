from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from common.forms import UserForm

# Create your views here.
def signup(request):
    """
    계정생성
    """
    if request.method == "POST":#입력으로 전달받은 데이터를 이용하여 사용자를 생성
        form = UserForm(request.POST)#is_valid() 함수로 폼 체크시 위 3개 속성을 필수값으로 체크.
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')#form.cleaned_data.get 함수는 입력값을 개별적으로 얻고 싶은 경우에 사용하는 함수
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)#신규 사용자를 저장한 후에 자동 로그인 될 수 있도록 authenticate와 login함수 사용
            login(request, user)#authenticate와 login함수는 django.contrib.auth 패키지의 함수로 사용자 인증과 로그인을 담당
            return redirect('index')
    else:
        form = UserForm()
    return render(request, 'common/signup.html', {'form': form})