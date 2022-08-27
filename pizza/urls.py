from django.urls import path, re_path, include
from rest_framework.routers import DefaultRouter
from .import views

urlpatterns = [
    path('', views.hellonew),
    path('orders', views.OrderCreateListView.as_view(), name='orders'),
    path('orders<int:order_id>', views.OrderDetailView.as_view(), name='orders-details'),
    path('update-orders', views.UpdateOrderStatus.as_view(), name='update-orders'),
    path('user/<int:user_id>/orders/',views.UserOrderView.as_view(), name='user-orders-detail'),
    path('user/<int:user_id>/orders/<int:order_id>', views.UserOrderDetail.as_view(), name='user-orders-details'),
]
