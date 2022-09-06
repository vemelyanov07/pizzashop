from django.urls import path
from . import views


urlpatterns = [
    # http://localhost:8000/pages/
    path('', views.PizzaListView.as_view(), name='main'),
]
