from django.urls import path
from .views import *
#이미지를 업로드하자
#from django.conf.urls.static import static
#from django.conf import settings
from finalproject import urls
app_name = 'main'

urlpatterns = [
    path('', index),
    path('blog/', blog),
    path('blog/<int:pk>/', posting, name="posting"),
    path('blog/new_post/', new_post),
    path('blog/<int:pk>/remove/', remove_post),
]