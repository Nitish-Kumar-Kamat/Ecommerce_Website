from django.contrib import admin
from .models import Items,SurfItems,mobile,Transaction,ItemModel
from django.contrib.sessions.models import Session
class SessionAdmin(admin.ModelAdmin):
    def _session_data(self, obj):
        return obj.get_decoded()
    list_display = ['session_key', '_session_data', 'expire_date']
admin.site.register(Session, SessionAdmin)

class proadmin(admin.ModelAdmin):
	list_display=('id','name','image','selling_price','price','quantity','available','desc')
admin.site.register(Items,proadmin)

class pro1admin(admin.ModelAdmin):
	list_display=('id','name','image','selling_price','price','quantity','available','desc')
admin.site.register(SurfItems,proadmin)

class Mobileadmin(admin.ModelAdmin):
    list_display=('id','name','image','selling_price','price','quantity','available','desc')
admin.site.register(mobile,Mobileadmin)


class TransactionAdmin(admin.ModelAdmin):
    list_display=('id','user','cat_id','purchased_quan','date')
admin.site.register(Transaction,TransactionAdmin)


@admin.register(ItemModel)
class RazorPayAdmin(admin.ModelAdmin):
    list_display=('id','user','amount','order_id','razorpay_payment_id','paid')