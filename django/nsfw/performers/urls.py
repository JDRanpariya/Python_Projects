from django.urls import path 
from . import views


urlpatterns = [
    path("", views.PerformerView.as_view(), name="PerformerView")
]
