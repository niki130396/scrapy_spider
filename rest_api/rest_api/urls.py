"""rest_api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path, re_path
from rest_framework.schemas import get_schema_view
from django.views.generic import TemplateView

from parliment_api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('list/', views.ParliamentData.as_view(), name='home'),
    re_path('search/', views.FilterParliamentData.as_view(), name='filtered_data'),
    path('mp/<int:pk>/', views.ParliamentDataById.as_view(), name='mp_by_id'),
    path('apischema/', get_schema_view(
        title='Parliament Data',
        description='API that lets developers use parliament data',
    ), name='api_schema'),
    path('docs/', TemplateView.as_view(
        template_name='documentation.html',
        extra_content={'schema_url': 'api_schema'}
    ), name='swagger-ui'),
]
