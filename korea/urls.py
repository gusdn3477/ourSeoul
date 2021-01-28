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
    path('hotplaces/', views.hotplaces, name="hotplaces"),
    path('region/', views.region, name="region"),
    path('introduction/', views.introduction, name="introduction"),
    path('hotplaces/palace/', views.palace, name='palace'),
    path('hotplaces/63building/', views.highbuilding, name='63building'),
    path('hotplaces/bukchon/', views.bukchon, name='bukchon'),
    path('hotplaces/lotteworld/', views.lotteworld, name='lotteworld'),
    path('hotplaces/myeongdong/', views.myeondong, name='myeondong'),
    path('hotplaces/ntower/', views.palace, name='ntower'),

   # path('ntower/'), views.visit_ntower, name='ntower'),
]
