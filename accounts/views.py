from django.shortcuts import render, redirect, get_object_or_404
from .models import User
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password, check_password
from .forms import LoginForm
# Create your views here.

def home(request):
    return render(request, 'home.html')

def login(request):

    if request == "POST":
        form = LoginForm(request.POST)

        if form.is_valid():
            #session_code 검증
            request.session['user'] = form.user_id
            return redirect('/')

    else:
        form = LoginForm()
        # 빈 클래스 변수를 만듦

    return render(request, 'accounts/login.html', {'form':form})
'''
    if request.method == "GET":
        return render(request, 'accounts/login.html')

    elif request.method == "POST":
        #전송받은 이메일 비밀번호 확인
        username = request.POST.get('username')
        password = request.POST.get('password')

        #유효성 처리
        res_data = {}
        if not username and not password:
            res_data['error'] = "아이디와 비밀번호를 모두 입력해 주세요"

        elif not username:
            res_data['error'] = "아이디를 입력해 주세요"

        elif not password:
            res_data['error'] = "비밀번호를 입력해 주세요"

        else:

            #기존(DB)에 있는 User 모델과 같은 값인 것을 가져온다.
            user = User.objects.get(username = username) #(필드명 = 값)

            if check_password(password, user.password): # 암호화 된 비밀번호 확인하는 코드
                request.session['user'] = user.id

                #리다이렉트
                return redirect('/home')

            else:
                res_data['error'] = "비밀번호가 틀렸습니다"
                
        return render(request, 'accounts/login.html', res_data)
        '''

def logout(request):
    if request.session['user'] : #로그인 중이라면
        del(request.session['user'])

    return redirect('/home')

def register(request):
    if request.method == "GET":
        return render(request, 'accounts/register.html')

    elif request.method == 'POST':
        #여기에 회원가입 처리 코드
        username = request.POST['username']
        password = request.POST['password']
        re_password = request.POST['re-password']

        res_data = {}

        #아이디, 비밀번호 둘 다 입력 안 된 경우
        if not username and not (password and re_password):
            res_data['error'] = "아이디와 비밀번호를 입력해 주세요."

        #아이디만 입력되지 않은 경우
        elif not username:
            res_data['error'] = "아이디를 입력해 주세요"

        #비밀번호가 입력되지 않은 경우
        elif not (password or re_password):
            res_data['error'] = "비밀번호를 입력해 주세요"

        #비밀번호가 다른 경우
        elif password != re_password:
            #return HttpResponse("비밀번호가 다릅니다.")
            res_data['error'] = "비밀번호가 일치하지 않습니다."

        else:

            #user = User.objects.get(username = username)
            user = User.objects.filter(username=username)

            if user:
                res_data['error'] = '중복된 아이디입니다.'

            #if User.objects.get(username = username): #(필드명 = 값), 존재하는 아이디가 있으면
            #    res_data['error'] = '중복된 아이디입니다.'

            else:
                user = User(
                    username = username,
                    password = make_password(password),
                )
                user.save()

        if not res_data:
            res_data['error'] = "회원가입이 완료되었습니다."

        return render(request, 'accounts/register.html', res_data)