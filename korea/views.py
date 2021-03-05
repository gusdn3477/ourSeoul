from django.shortcuts import render
from .models import Contact
# Create your views here

def main(request):

    if request.method =='GET':
        return render(request, 'korea/index.html')

    elif request.method == 'POST':

        res = {}
        email = request.POST['email']
        contents = request.POST['contents']

        if not email and not contents:
            res['error'] = '이메일과 내용을 입력해 주세요'

        elif not email:
            res['error'] = '이메일 주소를 입력해 주세요'

        elif len(contents) < 10:
            res['error'] = '내용을 10자 이상 입력해 주세요.'


        if not res:
            new_contents = Contact(email=email, contents = contents)
            new_contents.save()
            return render(request, 'korea/index.html', res)

        else:
            return render(request, 'korea/index.html', res)

def hotplaces(request):
    return render(request, 'korea/hotplaces.html')

def region(request):
    return render(request, 'korea/region.html')    

def introduction(request):
    return render(request, 'korea/introduction.html')

def palace(request):
    return render(request, 'korea/palace.html')

def highbuilding(request):
    return render(request, 'korea/63building.html')

def bukchon(request):
    return render(request, 'korea/bukchon.html')

def lotteworld(request):
    return render(request, 'korea/lotteworld.html')

def myeondong(request):
    return render(request, 'korea/myeongdong.html')

def ntower(request):
    return render(request, 'korea/ntower.html')