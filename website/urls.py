from django.urls import path
from website.views import *

app_name = 'blog'

urlpatterns = [
    path('', index_view  ),
    
]
