from django.urls import path
from . import views

app_name="product"
urlpatterns=[
    path("<int:pk>",views.ProductDetailView.as_view(),name="product_detail"),
    path("navbar",views.NavbarPartialView.as_view(),name="navbar"),
    path("category",views.CategoryStyle.as_view(),name="category"),
    path("list",views.ProductListView.as_view(),name="list")
]