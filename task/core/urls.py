from django.urls import path
from .views import *

app_name = 'core'

urlpatterns = [
    path('', upload_file_view, name='upload-view'),
    path('data', get_data, name='data-view'),
]
