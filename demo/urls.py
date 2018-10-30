"""demo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from django.conf.urls import url
# from django.contrib import admin
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    # url(r'^admin/', admin.site.urls),
    url(r'^$', TemplateView.as_view(template_name='base.html'), name='base'),
    url(r'^includes/',
        views.TranslateViaIncludes.as_view(),
        name='translation_as_include'),
    url(r'^inheritance/',
        views.TranslateViaInheritance.as_view(),
        name='translation_as_inheritance'),
    url(r'^template-tag/', views.TranslateViaTemplateTag.as_view(), name='translation_as_template_tag'),
]
