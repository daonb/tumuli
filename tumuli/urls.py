"""tumuli URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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

from django.core.exceptions import ImproperlyConfigured
from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from biography import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # url(r'^api-auth/', include('rest_framework.urls')),
    url(r'^memoirs/$', views.MemoirsList.as_view()), 
    url(r'^memoirs/(?P<pk>[0-9]+)$', views.MemoirDetails),
]

urlpatterns = format_suffix_patterns(urlpatterns)

try:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
except ImproperlyConfigured:
    # it's on S3, nothing for us to do
    pass
