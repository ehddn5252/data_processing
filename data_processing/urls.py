

from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('',include('input_data.urls'),name='input_data'),
    path('admin/', admin.site.urls),
]
