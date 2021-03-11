from django.urls import path
from infoProduct import views

urlpatterns = [
    path('infoproduct/<int:id>/', views.InfoProduct.as_view()),
    path('infoproducts/', views.InfoProducts.as_view()),

    path('incrementStock/<int:id>/<int:qty>/', views.IncrementQuantity.as_view()),
    path('decrementStock/<int:id>/<int:qty>/', views.DecrementQuantity.as_view()),

    path('putonsale/<int:id>/<str:newprice>/', views.SetSale.as_view()),
    path('removesale/<int:id>/', views.RemoveSale.as_view()),
]