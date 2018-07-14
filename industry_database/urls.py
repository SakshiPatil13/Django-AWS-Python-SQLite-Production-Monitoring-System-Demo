"""industry_database URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
# from app_industry import views


admin.site.site_header = 'LMTech Admin'
admin.site.index_title = 'Production Monitoring System'
admin.site.site_title = 'LMTech'


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # Using site url i.e. 127.0.0.1:8000
    url(r'^', include('app_industry.urls')),
]
