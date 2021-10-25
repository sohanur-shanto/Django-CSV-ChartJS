from django.urls import path
from .views import *

app_name = 'core'

urlpatterns = [
    path('', upload_file_view, name='upload-view'),
    path('data', get_data, name='get_data'),
    path('download-csv', d_csv, name='d_csv'),
    path('download-pdf', some_view, name='some_view'),
]
