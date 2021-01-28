from django.urls import path
from . import views

urlpatterns = [
    path('palace/', views.visit_palace, name='palace'),
    path('', views.main, name='index'),
    path('section_place/', views.section_place, name="secton_place"),
    path('theme_place/', views.theme_place, name="theme_place"),
    path('will/', views.will, name="will"),
    
   # path('ntower/'), views.visit_ntower, name='ntower'),
]
