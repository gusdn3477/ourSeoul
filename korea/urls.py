from django.urls import path
from . import views

urlpatterns = [
    path('palace/', views.visit_palace, name='palace'),
    path('ntower/', views.visit_ntower, name='palace'),
    path('63building/', views.visit_63building, name='palace'),
    path('bukchon/', views.visit_bukchon, name='palace'),
    path('myeongdong/', views.visit_myeongdong, name='palace'),
    path('lotteworld/', views.visit_lotteworld, name='palace'),
    path('', views.main, name='index'),
    path('section_place/', views.section_place, name="secton_place"),
    path('theme_place/', views.theme_place, name="theme_place"),
    path('will/', views.will, name="will"),
    
   # path('ntower/'), views.visit_ntower, name='ntower'),
]
