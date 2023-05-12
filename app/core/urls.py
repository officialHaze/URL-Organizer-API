from django.contrib import admin
from django.urls import path, include, re_path
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    re_path(r'(?P<pid>\w+)/$', views.redirect_to_site)
]
