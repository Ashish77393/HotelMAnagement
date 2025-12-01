"""
URL configuration for ProjectAsh project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from .views import home, signup, Dashboard, BookNow, Payment, logout_view
from service.views import *
from contact.views import *
from About.views import *
from Feature.views import *
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('admin/', admin.site.urls),
    path("",home),
    path("signup/",signup),
    path('Dashboard/',Dashboard),
    path('logout/', logout_view),
    path('BookNow/',BookNow),
    path('Payment/',Payment),
    path('About/',About),
    path('Contact/',Contact),
    path("Features/",Features),
    path('Services/',Services)
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
