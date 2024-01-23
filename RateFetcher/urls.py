from django.urls import path
from . import views

app_name = 'RateFetcher'

urlpatterns = [
    path('get-current-usd/', views.get_current_usd, name='get-current-usd'),
]
