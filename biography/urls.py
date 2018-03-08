from django.core.exceptions import ImproperlyConfigured
from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views




urlpatterns = [
    url('api/bio/<username>/', views.BiographyByUserList.as_view()), # get user's Bio by username
    # url('^api/periods/(?P<username>.+)/$', views.PeriodByUserList.as_view()), # get user's Periods by username
    # url('^api/memoirs/(?P<username>.+)/$', views.MemoirsByUserList.as_view()),
    # # get user's Memoirs by username
    # url('^api/contentatom/(?P<username>.+)/$', views.ContentAtomByUserList.as_view()),
    #  # get user's Content Atoms by username
]

urlpatterns = format_suffix_patterns(urlpatterns)

try:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
except ImproperlyConfigured:
    # it's on S3, nothing for us to do
    pass
