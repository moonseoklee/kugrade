import os, sys
sys.path.append( os.path.dirname(os.path.abspath(os.path.dirname(__file__))) )
import grade.urls
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('grade.urls')),
    path('login/',include('grade.urls')),
]
