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
from django.urls import include, path
from rest_framework.urlpatterns import format_suffix_patterns
from biography import views


urlpatterns = [
    path('admin/', admin.site.urls),
    # path('api/', include(biography.urls)),
    url('api/bio/(?P<username>.+)/', views.BiographyByUserList.as_view()), # get user's Bio by username
    url('^api/periods/(?P<username>.+)/$', views.PeriodByUserList.as_view()), # get user's Periods by username
    url('^api/memoirs/(?P<username>.+)/$', views.MemoirsByUserList.as_view()),
    # get user's Memoirs by username
    url('^api/contentatom/(?P<username>.+)/$', views.ContentAtomByUserList.as_view()),
     # get user's Content Atoms by username
]

urlpatterns = format_suffix_patterns(urlpatterns)

try:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
except ImproperlyConfigured:
    # it's on S3, nothing for us to do
    pass
