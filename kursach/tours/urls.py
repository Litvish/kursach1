from django.urls import path
from . import views


urlpatterns = [
    path('', views.tours_home, name='tours_home'),
    path('create', views.create, name='create'),
    path('<int:pk>', views.ToursDetailView.as_view(), name='tours-detail')
]
