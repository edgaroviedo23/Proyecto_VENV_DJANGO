from nuevo_proyecto.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.LoginView, name='login'),
    path('registro/', views.registroView, name='registro'),
    path('logout/', views.logoutView, name='logout')
]
