from django.shortcuts import render

# Create your views here
def visit_palace(request):
    return render(request, 'korea/palace.html')

#def visit_ntower(request)i
#    return render(request, 'korea/ntower.html')

def main(req):
    return render(req, 'korea/index.html')

def section_place(req):
    return render(req, 'korea/section_place.html')

def theme_place(req):
    return render(req, 'korea/theme_place.html')

def will(req):
    return render(req, 'korea/will.html')

