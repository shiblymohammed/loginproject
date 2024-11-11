from django.urls import path
from . import views
urlpatterns = [
    path('', views.loginPage , name = 'login'),
    path('dashboard/', views.dashboardPage , name = 'dashboard'),
    path('logout/', views.logoutPage, name='logout'),
    path('new/', views.new, name='new'),


    
]
