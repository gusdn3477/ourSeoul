from django.urls import path
from . import views

urlpatterns = [
    path('palace/', views.visit_palace, name='palace'),
   # path('ntower/'), views.visit_ntower, name='ntower'),
]
