from django.shortcuts import render, redirect
from .models import Post
# Create your views here.
def index(request):
    return render(request, 'main/index.html')

def blog(request):
    postlist = Post.objects.all()
    return render(request, 'main/blog.html', {'postlist' : postlist})

def posting(request, pk):
    post = Post.objects.get(pk=pk)
    return render(request, 'main/posting.html', {'post':post})

def new_post(request):

    '''if request.method == "POST":
        if 'file' in request.FILES:
            file = request.FILES['file']
            filename = file._name

            fp = open('%s/%s' % ('media/image/', filename), 'wb')
            for chunk in file.chunks():
                fp.write(chunk)
            fp.close()
            return HttpResponse('File Uploaded')
        return HttpResponse('Failed to Upload File')'''

    if request.method == 'POST':
        
        form = Post()
        form.postname = request.POST['postname']
        form.contents = request.POST['contents']

        try:
            form.mainphoto = request.FILES['mainphoto']

        except:
            pass

        form.save()
        '''
        mainphoto = request.FILES['mainphoto']

        if mainphoto:
            new_article = Post.objects.create(
                postname=request.POST['postname'],
                contents=request.POST['contents'],
                mainphoto=mainphoto,
            )

        else:
            new_article=Post.objects.create(
                postname=request.POST['postname'],
                contents=request.POST['contents'],
                #mainphoto=request.FILES['mainphoto'],
            )

        '''
        return redirect('/main/blog/')
    return render(request, 'main/new_post.html')

def remove_post(request, pk):
    post = Post.objects.get(pk=pk)
    if request.method == 'POST':
        post.delete()
        return redirect('/blog/')

    return render(request, 'main/remove_post.html', {'Post' : post})
'''
def upload(request):

    if request.method == "POST":
        if 'file' in request.FILES:
            file = request.FILES['file']
            filename = file._name

            fp = open('%s/%s' % ('media/image/', filename), 'wb')
            for chunk in file.chunks():
                fp.write(chunk)
            fp.close()
            return HttpResponse('File Uploaded')
        return HttpResponse('Failed to Upload File')
    def upload_pic(request): 
    
    if request.method == 'POST': 
        
        form = ImageUploadForm(request.POST, request.FILES) 
    
    if form.is_valid(): 
        
        m = ExampleModel.objects.get(pk=course_id) 
        m.model_pic = form.cleaned_data['image'] 
        m.save() 
        return HttpResponse('image upload success') 
    return HttpResponseForbidden('allowed only via POST')​
    '''