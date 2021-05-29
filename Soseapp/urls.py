"""dbProject URL Configuration

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
from django.urls import path
from . import views

app_name = 'Soseapp'
urlpatterns = [
    path('', views.codeInput, name = 'codeInput'),
    path('serviceAgree', views.serviceAgreePage, name = 'serviceAgree'),
    path('survey', views.surveyPage, name = 'survey'),
    path('mbti', views.mbtiSelect, name = 'mbti'),
    path('main', views.mainPage, name = 'main'),
    path('video', views.videoPage, name = 'video'),
    path('quest1', views.toQuest1, name = 'quest1'),
    path('video2', views.video2Page, name = 'video2'),
    path('quest2', views.toQuest2, name = 'quest2'),
    path('video3', views.video3Page, name = 'video3'),
    path('result', views.toResult, name = 'result')

]
