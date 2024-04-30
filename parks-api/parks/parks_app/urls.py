from django.urls import path
from parks_app import views

urlpatterns = [
    path('', views.get_parks, name = "get_parks"),
    path('parks/<int:id>/',views.park_detail, name = "park_detail")
]
