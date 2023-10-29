from . import views
from django.urls import path, include
app_name='searchapp'

urlpatterns = [

    path('', views.SearchResult,name='SearchResult'),

]