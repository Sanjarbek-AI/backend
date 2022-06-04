from django.urls import path

from order.views import OrderView, OrderListView, OrderDetailView
from product.views import ProductListView
from user.views.login import LoginView
from user.views.logout import LogoutView, LogoutAllView
from user.views.register import RegisterView
from user.views.resend_otp import ResendOtpView
from user.views.verify_otp import VerifyOTPView

urlpatterns = [
    # "User application"
    path('user/register', RegisterView.as_view(), name='register'),
    path('user/login', LoginView.as_view(), name='login'),
    path('user/logout', LogoutView.as_view(), name='logout'),
    path('user/logout-all', LogoutAllView.as_view(), name='logout-all'),
    path('user/verify/otp', VerifyOTPView.as_view(), name='verify-otp'),
    path('user/resend/otp', ResendOtpView.as_view(), name='resend-otp'),

    # Products
    path('products/list', ProductListView.as_view(), name='products-list'),
    path('orders', OrderView.as_view(), name='order-create'),
    path('orders/list', OrderListView.as_view(), name='order-list'),
    path('orders/<int:order_id>', OrderDetailView.as_view(), name='order-detail'),
]
