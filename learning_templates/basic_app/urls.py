from django.conf.urls import url
from django.urls import path, include
from basic_app import views
# OR: from . import views

# TEMPLATE TAGGING - Django automatically looks for app_name.
# This tells Django to look under 'basic_app' and find URLs
# that matches.
app_name = 'basic_app'
urlpatterns = [
    path('relative/', views.relative,name='relative'),
    path('other/', views.other, name='other'),
]
