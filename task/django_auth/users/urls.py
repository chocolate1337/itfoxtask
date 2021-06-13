from django.urls import re_path, include, path
from rest_framework.routers import DefaultRouter
from .views import RegistrationAPIView
from .views import LoginAPIView
from .views import NewsAPIView


urlpatterns = [
    re_path(r'^registration/?$', RegistrationAPIView.as_view(), name='user_registration'),
    re_path(r'^auth/?$', LoginAPIView.as_view(), name='user_login'),
    re_path(r'^news/?$', NewsAPIView.as_view(), name='news_login'),
]