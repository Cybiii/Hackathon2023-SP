from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name = 'home'),
    path('one/', views.one, name = 'pageone'),
    path('two/', views.two, name = 'pagetwo'),

]

