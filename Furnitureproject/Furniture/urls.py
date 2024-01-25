from . import views
from django.urls import path
app_name='Furniture'
urlpatterns = [
      path('',views.AllProductCategory,name='AllProductCategory'),
      path('<slug:c_slug>/',views.AllProductCategory,name='Product_by_Category'),
      path('<slug:c_slug>/<slug:product_slug>/',views.ProductDetail,name='ProductDetail'),
]