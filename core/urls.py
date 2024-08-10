"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from home.views import *
from rece.views import *
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', home, name = 'home'),
    path('admin/', admin.site.urls),
    path('login/', login_page, name = 'login_page'),
    path('recepe/', recepe_page, name = 'recepe_page'),
    path('about/', about_page, name = 'about_page'),
    path('register/', register_page, name = 'register_page'),
    path('recepe/delete/<id>/', delete_recepe, name = 'delete_recepe'),
    path('recepe/update/<id>/', update_recepe, name = 'update_recepe'),
    path('logout_page/', logout_page, name = 'logout_page'),
]


urlpatterns += static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)

