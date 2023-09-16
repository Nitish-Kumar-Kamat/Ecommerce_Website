from django.urls import path
from .import views

urlpatterns = [
    path('',views.home, name='home'),
    path('about',views.aboutus,name='about'),
    path('contact/',views.contact,name='contact'),
    path('allitems/',views.allitems, name='allitems'),
    path('surf/',views.surf, name='surf'),
    path('cart/',views.mycart,name='cart'),
    path('prodetail/<int:id>/',views.prodetail,name='prodetail'),
    path('surfTask/<int:pk>/',views.surfTask,name='surfTask'),
    path('mobile/',views.mobiledata, name='mobile'),
    path('mobileTask/<int:pk>/',views.mobileTask, name='mobileTask'),
    path('mysearch/',views.mysearch,name='mysearch'),
    path('delete/<int:id>/<cat>',views.deletecart,name='delete'),
    # path('update/<int:id>/<cat>',views.update,name='update'),
    # path('payment/',views.make_payment,name='payment'),
    path('afterclickplace/',views.afterclickplace,name='afterclickplace'),
    path('buy_now/<int:id>/<cat>/',views.buy_now,name='buy_now'),

    # Payment gateway url
    path('buypayment/',views.buypayment,name='buypayment'),
    path("itempayment/",views.item_payment,name='item_payment'),
    path("payment-Status/",views.payment_status,name='payment-status'),
    path("transactionData/",views.transactionData,name='transactionData'),

]



