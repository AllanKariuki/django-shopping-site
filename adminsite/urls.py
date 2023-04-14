from . import views
from django.urls import path
from clientsite import views as client_views

urlpatterns = [
    path('admin-dashboard/', views.index, name= 'admindashboard'),
    path('add-category/', views.addcategory, name= 'addcategory'),
    path('category/', views.category, name = 'productcategory'),
    path('category-view/<id>/', views.category_detail, name = 'categoryDetail'),
    path('edit-category/<id>/', views.editcategory, name = 'editcategory'),
    path('delete-category/<id>/', views.deletecategory, name = 'deletecategory'),
    path('add-brand/', views.addbrand, name= 'addbrand'),
    path('brand/', views.brand, name = 'brands'),
    path('brand-view/<id>/', views.brand_detail, name = 'brandDetail'),
    path('edit-brand/<id>/', views.editbrand, name = 'editbrand'),
    path('delete-brand/<id>/', views.deletebrand, name = 'deletebrand'),
    path('products/', views.products, name= 'products'),
    path('product-view/<id>/', views.product_detail, name = 'productDetail'),
    path('orders/', views.orders, name = 'orders'),
    path('order-detail/<id>/',  views.order_detail, name = 'orderDetail'),
    path('requests-for-services/', views.requestsForServices, name = 'requestsForServices'),
    path('requests-for-services-detail/<id>/', views.requestsForServicesDetail, name = 'requestsForServicesDetail'),
    path('requests-for-qotations/', views.requestsForQuotation, name= 'requestsForQuotation'),
    path('requests-for-qotations-detail/<id>/', views.requestsForQuotationDetail, name= 'requestsForQuotationDetail'),
    path('addproducts/', views.product_images, name= 'add-prod'),
    path('logout/', views.logoutpage, name='logoutpage'),
    path('login', client_views.loginpage, name='login')
]
