from django.urls import path
from .views import index, results

app_name = 'chart'

urlpatterns = [
    path('', index, name='index'),
    path('results', results, name='results'),

]
