from django.urls import path
from WebApp import views

urlpatterns = [
            path('', views.Home_page, name="Home"),
            path('About_page/', views.About_page, name="About_page"),
            path('our_services/', views.our_services, name="our_services"),
            path('contact_page/', views.contact_page, name="contact_page"),
            path('save_contact/', views.save_contact, name="save_contact"),
            path('signup_page/', views.signup_page, name="signup_page"),
            path('save_signup/', views.save_signup, name="save_signup"),
            path('signin_page/', views.signin_page, name="signin_page"),
            path('save_signin/', views.save_signin, name="save_signin"),
            path('logout_page/', views.logout_page, name="logout_page"),
     path('filtered_services/<cat_name>/', views.filtered_services, name="filtered_services"),
    path('single_services/hair/<int:sid>/', views.single_services_hair, name="single_services_hair"),
    path('single_services/skin/<int:hid>/', views.single_services_skin, name="single_services_skin"),
    path('single_services/nail/<int:nid>/', views.single_services_nail, name="single_services_nail"),
    path('single_services/makeup/<int:mid>/', views.single_services_makeup, name="single_services_makeup"),
    path('single_services/body/<int:bid>/', views.single_services_body, name="single_services_body"),


path('save_booking/', views.save_booking, name="save_booking"),
path('bookingHair/<int:sid>', views.bookingHair, name="bookingHair"),
path('bookingSkin/<int:hid>', views.bookingSkin, name="bookingSkin"),
path('bookingNail/<int:nid>', views.bookingNail, name="bookingNail"),
path('bookingMakeup/<int:mid>', views.bookingMakeup, name="bookingMakeup"),
path('bookingBodycare/<int:bid>', views.bookingBodycare, name="bookingBodycare"),
path('Searchbarfind/', views.Searchbarfind, name="Searchbarfind"),
path('bookhistory/', views.bookhistory, name="bookhistory"),
path('booking_pdf/<int:booking_id>', views.booking_pdf, name="booking_pdf"),
path('payment_page/', views.payment_page, name="payment_page"),
path('productpage/', views.productpage, name="productpage"),
path('single_prod/<int:pid>', views.single_prod, name="single_prod"),
path('Cart_page/', views.Cart_page, name="Cart_page"),
path('save_cart_products/', views.save_cart_products, name="save_cart_products"),
path('payment_product_page/', views.payment_product_page, name="payment_product_page"),
path('delete_cart/<int:cartid>', views.delete_cart, name="delete_cart"),



]
