from django.shortcuts import render

# Create your views here
def visit_palace(request):
    return render(request, 'korea/palace.html')

#def visit_ntower(request)i
#    return render(request, 'korea/ntower.html')

def mainpage(req):
    return render(req, 'korea/mainpage.html')