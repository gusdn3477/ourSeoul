#forms.py
from django import forms
from .models import User

class LoginForm(forms.Form):
    username = forms.CharField(error_messages={'required' : '아이디를 입력하세요!'}, max_length = 50, label="사용자 이름")
    password = forms.CharField(error_messages={'required' : '비밀번호를 입력하세요!'}, widget=forms.PasswordInput, label="비밀번호")
    
    def clean(self):
        cleaned_data = super().clean()
        #처음 값이 들어왔다는 검증 진행
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')

        if username and password:

            try:
                user = User.objects.get(username=username)

            except User.DoesNotExist:
                self.add_error('username', '아이디가 없습니다!')
                return

            if not check_password(password, user.password):
                self.add_error('password', '비밀번호가 다릅니다!')

            else:
                self.user_id = user.id