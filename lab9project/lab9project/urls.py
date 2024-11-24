"""
URL configuration for lab9project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path
from lab9app import views
from lab9app.views import ProductListView, ProductDetailView,Product_Create,Product_Delete, sign_in, sign_up,edit_product,sign_out,chat_with_gpt, add_to_order,order_in_process,submit_order, chatbox,order_summary,order_history,complete_order,success_page

urlpatterns = [
    path("admin/", admin.site.urls),

    path('', ProductListView.as_view(), name='home'),  # Root URL redirects to product list
    path('products/', ProductListView.as_view(), name='product_list'),      #all products
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),    #product details
    path('products/new/', Product_Create, name='Product_Create'),  # New product creation
    path('product/delete/<int:product_id>/', Product_Delete, name='Product_Delete'), #delete function
    path('sign-in/', sign_in, name='sign_in'),             #user sign in
    path('signup/', sign_up, name='SignUp'),
    path('edit/<int:product_id>/', edit_product, name='edit_product'),
    path('sign-out/', sign_out, name='sign_out'),  # Sign Out URL
    path('api/chat/', chat_with_gpt, name='chat_with_gpt'),  # Chat with GPT endpoint
    path('chatbox/', chatbox, name='chatbox'),
    path('order-in-process/', order_in_process, name='order_in_process'),
    path('add-to-order/<int:product_id>/', add_to_order, name='add_to_order'),
    path('submit-order/', submit_order, name='submit_order'),
    path('order-summary/', order_summary, name='order_summary'),
    path('complete-order/', complete_order, name='complete_order'),
    path('order-history/', order_history, name='order_history'),
    path('success/', success_page, name='success_page'),
]
