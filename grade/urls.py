from django.urls import path

from . import views

urlpatterns = [
    path('chart/',views.chart,name='chart'),
    path('login/',views.login,name='login'),    
    
]
