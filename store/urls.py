from django.urls import path
from django.urls import re_path

from .views import (category_list, featured_product, product_retrieve,
                    products_list)

urlpatterns =[
    path('category',category_list,name='Category list'),
    path('featured-products',featured_product,name="Featured Product List"),
    path('products',products_list,name="Products List"),
    # path('products/<slug:slug>',product_retrieve, name="Product Retrieve")
    re_path(r'^products/(?P<slug>[\u0600-\u06FF-a-zA-Z0-9]+)$',product_retrieve,name="Product Retreive")
]

    # re_path(r'^store/(?P<slug>[\u0600-\u06FF-a-zA-Z0-9]+)$', ProductRetrieveView.as_view(),name="store-product-retrieve"),
