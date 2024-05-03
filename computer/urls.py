from django.urls import path
from computer.views import ComputerView, ComputerDetailView, DownloadBookView

app_name = 'computer'

urlpatterns = [
    path('', ComputerView, name= 'list'),
    path('<int:pk>/', ComputerDetailView, name= 'detail'),
    path('download/<int:pk>/', DownloadBookView, name='download')
]