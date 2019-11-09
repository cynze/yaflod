from django.urls import path
from . import views

urlpatterns = [
    path('families/', views.family_list),
    path('families/<int:pk>', views.family_detail)
]