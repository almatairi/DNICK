from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # get cake from pk
    path('order-cake/<str:pk>/', views.orderCakeForm, name='order'),
    path('thank-you/<str:pk>/', views.finalStage, name='final'),
]
