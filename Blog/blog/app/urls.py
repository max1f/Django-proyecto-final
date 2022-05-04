from django.contrib import admin
from django.urls import path,include
from app import views
from .views import inicio,post,about,contact,publicar,login_request,register,feed
from django.contrib.auth.views import LogoutView,LoginView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.inicio, name='inicio'),
    path('post', views.post),
    path('about', views.about),
    path('contact', views.contact),
    path('publicar', views.feed),
    path('post/#!', views.inicio),
    path('about/#!', views.inicio),
    path('contact/#!', views.inicio),
    path('publicar/#!', views.inicio),
    path('login', LoginView.as_view(template_name='sign.html'), name='login'),
    path('register', views.register, name= 'register'),
    path('logout', LogoutView.as_view(template_name='logout.html'), name= 'Logout'),
]   
