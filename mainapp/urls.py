from django.urls import path, include

from mainapp.views import (
    index, addProduct, editProduct, deleteProduct
)

urlpatterns = [
    path('', index, name = '/'),
    path('add-product', addProduct, name = 'add-prod'),
    path('edit-product/<str:pk>', editProduct, name="edit-prod"),
    path('delete-product/<str:pk>', deleteProduct, name="delete-prod")
]