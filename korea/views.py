from django.shortcuts import render

# Create your views here
def visit_palace(request):
    return render(request, 'korea/palace.html')

def visit_ntower(request):
    return render(request, 'korea/ntower.html')

def visit_63building(request):
    return render(request, 'korea/63building.html')

def visit_lotteworld(request):
    return render(request, 'korea/lotteworld.html')

def visit_bukchon(request):
    return render(request, 'korea/bukchon.html')

def visit_myeongdong(request):
    return render(request, 'korea/myeongdong.html')

def main(req):
    return render(req, 'korea/index.html')

def section_place(req):
    return render(req, 'korea/section_place.html')

def theme_place(req):
    return render(req, 'korea/theme_place.html')

def will(req):
    return render(req, 'korea/will.html')

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