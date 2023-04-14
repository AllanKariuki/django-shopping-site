from django.urls import path
from . import views
from adminsite import views as admin_views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('blog/', views.blog, name='blog'),
    path('contact-us/', views.contact_us, name = 'contact-us'),
    path('about-us/', views.about_us, name = 'about-us'),
    path('shop/', views.shop, name = 'shop'),
    path('product-category/<str:category_name>/', views.product_category, name = 'product-category'),
    path('product-category/<str:brand_name>/', views.product_brands, name = 'product-brand'),
    path('product-detail/<id>/', views.product_detail, name= 'product-detail'),
    path('wishlist', views.wishlist, name='wishlist'),
    #The Blogs
    path('request-for-service/', views.request_for_service, name= 'request-for-service'),
    path('request-for-quotation/', views.request_for_quotation, name= 'request-for-quotation'),
    path('simplest-ways/', views.simplest_ways, name= 'blog1'),
    path('influence-of-typewriters/', views.influence_of_typewriters, name='blog2'),
    path('basic-it-skills/', views.basic_it_skills, name='blog3'),
    path('why-konica-minolta/', views.why_konica_minolta, name= 'blog4'),
    path('discover-6-ways/', views.discover_6_ways, name='blog5'),
    path('reasons-to-choose-ricoh', views.reasons_to_choose_ricoh, name='blog6'),
    path('january-blues-2022/', views.january_blues_2022, name='blog7'),
    path('easy-work-from-home/', views.easy_work_from_home, name='blog8'),
    path('must-have-equipment/', views.must_have_equipment, name= 'blog9'),
    path('opportunities-in-printing', views.opportunities_in_printing, name= 'blog10'),
    
    #Cart urls
    path('cart', views.cart, name='cart'),
    path('add-to-cart/<product_id>/', views.add_to_cart, name = 'add-to-cart'),
    path('cart-update/<cart_item_id>/<quantity>', views.cart_update, name='cart_update'),
    path('remove-item/<cart_item_id>/', views.cart_remove, name='cart-remove'),
    path('order_detail/', views.order_detail, name= 'order_detail'),
    path('checkout/', views.checkout, name='checkout'),
    
    #login and register
    path('login/', views.loginpage, name= 'loginpage'),
    path('register/', views.registerpage, name= 'registerpage'),
    
    path('dashboard/', admin_views.index, name='admin-dashboard')
]
