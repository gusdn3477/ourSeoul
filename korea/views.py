from django.shortcuts import render
from .models import Contact
# Create your views here

def main(request):

    if request.method =='GET':
        return render(request, 'korea/index.html')

    elif request.method == 'POST':
        email = request.POST['email']
        contents = request.POST['contents']

        new_contents = Contact(email=email, contents = contents)
        new_contents.save()

        return render(request, 'korea/index.html')

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