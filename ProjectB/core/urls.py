from django.contrib import admin
from django.urls import path
from website import views

urlpatterns = [
    path('', views.home, name='home'),
    path('tracking/', views.tracking, name='tracking'),
    path('services/', views.services, name='services'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('calculator/', views.calculator, name='calculator'),
    path('estimates/', views.estimate_lookup, name='estimate_lookup'),
    path('admin/', admin.site.urls),
    path("about/", views.about, name="about"),
]
