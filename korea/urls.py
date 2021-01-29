from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.main, name='index'),
    path('hotplaces/', views.hotplaces, name="hotplaces"),
    path('region/', views.region, name="region"),
    path('introduction/', views.introduction, name="introduction"),
    path('hotplaces/palace/', views.palace, name='palace'),
    path('hotplaces/63building/', views.highbuilding, name='63building'),
    path('hotplaces/bukchon/', views.bukchon, name='bukchon'),
    path('hotplaces/lotteworld/', views.lotteworld, name='lotteworld'),
    path('hotplaces/myeongdong/', views.myeondong, name='myeondong'),
    path('hotplaces/ntower/', views.ntower, name='ntower'),

   # path('ntower/'), views.visit_ntower, name='ntower'),
]
