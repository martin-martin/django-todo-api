"""auth_api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path, include
from rest_framework.documentation import include_docs_urls
from . import views  # the . is a shortcut for current App (here 'auth_api')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('docs/', include_docs_urls(title='Todo API',
                                    description='RESTful API for Todo items')),
    path('', views.api_root),
    # https://stackoverflow.com/questions/48608894/specifying-a-namespace-in-include-without-providing-an-app-name
    path('', include(('users.urls', 'users'), namespace='users')),
    path('', include(('todos.urls', 'todos'), namespace='todos')),
]
