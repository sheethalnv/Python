from . import views
from django.urls import path, include
app_name='cart'

urlpatterns = [
    path('add/<int:product_id>', views.add_cart,name='add_cart'),
    path('', views.cart_detail,name='cart_detail'),
    path('remove_cart/<int:product_id>',views.remove_cart,name='remove_cart'),
    path('full_remove/<int:product_id>',views.full_remove,name='full_remove'),

]