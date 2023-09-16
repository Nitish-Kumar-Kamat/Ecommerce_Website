from django.urls import path
from .import views

urlpatterns=[
   path('signup/',views.sign_up, name='signup'),
   path('login/',views.log_in, name='login'),
   path('logout/',views.log_out, name='logout'),

   #For Password reset
   path('pass_reset/',views.pass_reset, name='pass_reset'),
   path('pass_reset_confirm/',views.mySetPass, name='pass_reset_confirm'),
]