from django.urls import path
from website.api import views
from website.api.views import CartView
urlpatterns = [
    # path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('products/', views.product_list, name='product_list'),
    path('cart/', CartView.as_view(), name='cart'),
    path('products/<int:product_id>/', views.product_detail, name='product_detail'),
    path('session/', views.session_view, name='session'),
    path('admin/stats/', views.admin_stats, name='admin_stats'),
    path('me/', views.me, name='me'),
    path('change-password/', views.change_password, name='change_password'),
    # Admin-only
    path('admin/users/', views.admin_users, name='admin_users'),
    path('admin/users/<int:user_id>/', views.admin_user_detail, name='admin_user_detail'),
]