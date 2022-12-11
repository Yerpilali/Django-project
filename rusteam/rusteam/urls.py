"""rusteam URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from store import views

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^(?:index/?|)$', views.index),
    # Basket
    path('Basket/', views.BasketListView.as_view(), name='bas'),
    path('Basket/<int:pk>/', views.BasketDetailView.as_view(), name='detail_bas'),
    path('Basket/new/', views.BasketCreateView.as_view(), name='create_bas'),
    path('Basket/<int:pk>/edit/', views.BasketUpdateView.as_view(), name='edit_bas'),
    path('Basket/<int:pk>/delete/', views.BasketDeleteView.as_view(), name='delete_bas'),
    # Developer
    path('Developer/', views.DeveloperListView.as_view(), name='dev'),
    path('Developer/<int:pk>/', views.DeveloperDetailView.as_view(), name='detail_dev'),
    path('Developer/new/', views.DeveloperCreateView.as_view(), name='create_dev'),
    path('Developer/<int:pk>/edit/', views.DeveloperUpdateView.as_view(), name='edit_dev'),
    path('Developer/<int:pk>/delete/', views.DeveloperDeleteView.as_view(), name='delete_dev'),
    # Label
    path('Label/', views.LabelListView.as_view(), name='lab'),
    path('Label/<int:pk>/', views.LabelListView.as_view(), name='detail_lab'),
    path('Label/new/', views.LabelCreateView.as_view(), name='create_lab'),
    path('Label/<int:pk>/edit/', views.LabelUpdateView.as_view(), name='edit_lab'),
    path('Label/<int:pk>/delete/', views.LabelDeleteView.as_view(), name='delete_lab'),
    # Log
    path('Log/', views.LogListView.as_view(), name='log'),
    path('Log/<int:pk>/', views.LogListView.as_view(), name='detail_log'),
    path('Log/new/', views.LogCreateView.as_view(), name='create_log'),
    path('Log/<int:pk>/edit/', views.LogUpdateView.as_view(), name='edit_log'),
    path('Log/<int:pk>/delete/', views.LogDeleteView.as_view(), name='delete_log'),
    # Product
    path('Product/', views.ProductListView.as_view(), name='prod'),
    path('Product/<int:pk>/', views.ProductListView.as_view(), name='detail_prod'),
    path('Product/new/', views.ProductCreateView.as_view(), name='create_prod'),
    path('Product/<int:pk>/edit/', views.ProductUpdateView.as_view(), name='edit_prod'),
    path('Product/<int:pk>/delete/', views.ProductDeleteView.as_view(), name='delete_prod'),
    # PaymentDetails
    path('PaymentDetails/', views.PaymentDetailsListView.as_view(), name='pd'),
    path('PaymentDetails/<int:pk>/', views.PaymentDetailsListView.as_view(), name='detail_pd'),
    path('PaymentDetails/new/', views.PaymentDetailsCreateView.as_view(), name='create_pd'),
    path('PaymentDetails/<int:pk>/edit/', views.PaymentDetailsUpdateView.as_view(), name='edit_pd'),
    path('PaymentDetails/<int:pk>/delete/', views.PaymentDetailsDeleteView.as_view(), name='delete_pd'),
    # PaymentHistory
    path('PaymentHistory/', views.PaymentHistoryListView.as_view(), name='ph'),
    path('PaymentHistory/<int:pk>/', views.PaymentHistoryListView.as_view(), name='detail_ph'),
    path('PaymentHistory/new/', views.PaymentHistoryCreateView.as_view(), name='create_ph'),
    path('PaymentHistory/<int:pk>/edit/', views.PaymentHistoryUpdateView.as_view(), name='edit_ph'),
    path('PaymentHistory/<int:pk>/delete/', views.PaymentHistoryDeleteView.as_view(), name='delete_ph'),
    # Publisher
    path('Publisher/', views.PublisherListView.as_view(), name='pub'),
    path('Publisher/<int:pk>/', views.PublisherDetailView.as_view(), name='detail_pub'),
    path('Publisher/new/', views.PublisherCreateView.as_view(), name='create_pub'),
    path('Publisher/<int:pk>/edit/', views.PublisherUpdateView.as_view(), name='edit_pub'),
    path('Publisher/<int:pk>/delete/', views.PublisherDeleteView.as_view(), name='delete_pub'),
    # Role
    path('Role/', views.RoleListView.as_view(), name='rol'),
    path('Role/<int:pk>/', views.RoleDetailView.as_view(), name='detail_rol'),
    path('Role/new/', views.RoleCreateView.as_view(), name='create_rol'),
    path('Role/<int:pk>/edit/', views.RoleUpdateView.as_view(), name='edit_rol'),
    path('Role/<int:pk>/delete/', views.RoleDeleteView.as_view(), name='delete_rol'),
    # Statistic
    path('Statistic/', views.StatisticListView.as_view(), name='stat'),
    path('Statistic/<int:pk>/', views.StatisticDetailView.as_view(), name='detail_stat'),
    path('Statistic/new/', views.StatisticCreateView.as_view(), name='create_stat'),
    path('Statistic/<int:pk>/edit/', views.StatisticUpdateView.as_view(), name='edit_stat'),
    path('Statistic/<int:pk>/delete/', views.StatisticDeleteView.as_view(), name='delete_stat'),
    # Tag
    path('Tag/', views.TagListView.as_view(), name='tag'),
    path('Tag/<int:pk>/', views.TagDetailView.as_view(), name='detail_tag'),
    path('Tag/new/', views.TagCreateView.as_view(), name='create_tag'),
    path('Tag/<int:pk>/edit/', views.TagUpdateView.as_view(), name='edit_tag'),
    path('Tag/<int:pk>/delete/', views.TagDeleteView.as_view(), name='delete_tag'),
    # TypeKey
    path('TypeKey/', views.TypeKeyListView.as_view(), name='tk'),
    path('TypeKey/<int:pk>/', views.TypeKeyDetailView.as_view(), name='detail_tk'),
    path('TypeKey/new/', views.TypeKeyCreateView.as_view(), name='create_tk'),
    path('TypeKey/<int:pk>/edit/', views.TypeKeyUpdateView.as_view(), name='edit_tk'),
    path('TypeKey/<int:pk>/delete/', views.TypeKeyDeleteView.as_view(), name='delete_tk'),
    # User
    path('User/', views.UserListView.as_view(), name='use'),
    path('User/<int:pk>/', views.UserDetailView.as_view(), name='detail_use'),
    path('User/new/', views.UserCreateView.as_view(), name='create_use'),
    path('User/<int:pk>/edit/', views.UserUpdateView.as_view(), name='edit_use'),
    path('User/<int:pk>/delete/', views.UserDeleteView.as_view(), name='delete_use'),
    # WishList
    path('WishList/', views.WishListListView.as_view(), name='wl'),
    path('WishList/<int:pk>/', views.WishListDetailView.as_view(), name='detail_wl'),
    path('WishList/new/', views.WishListCreateView.as_view(), name='create_wl'),
    path('WishList/<int:pk>/edit/', views.WishListUpdateView.as_view(), name='edit_wl'),
    path('WishList/<int:pk>/delete/', views.WishListDeleteView.as_view(), name='delete_wl'),
]
