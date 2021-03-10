from django.urls import path
from infoProduct import views

urlpatterns = [
    path('infoproduct/<int:id>/', views.InfoProduct.as_view()),
    path('infoproducts/', views.InfoProducts.as_view()),
]