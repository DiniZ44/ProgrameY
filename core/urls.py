from django.urls import path, include
from . import views

urlpatterns = [
    path('core/', include('core.urls')),
    path('', views.Index, name='Index.html'),
]
