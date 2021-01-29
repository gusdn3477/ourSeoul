from django.shortcuts import render

# Create your views here


def main(req):
    return render(req, 'korea/index.html')

def hotplaces(req):
    return render(req, 'korea/hotplaces.html')

def region(req):
    return render(req, 'korea/region.html')    

def introduction(req):
    return render(req, 'korea/introduction.html')

def palace(req):
    return render(req, 'korea/palace.html')

def highbuilding(req):
    return render(req, 'korea/63building.html')

def bukchon(req):
    return render(req, 'korea/bukchon.html')

def lotteworld(req):
    return render(req, 'korea/lotteworld.html')

def myeondong(req):
    return render(req, 'korea/myeongdong.html')

def ntower(req):
    return render(req, 'korea/ntower.html')