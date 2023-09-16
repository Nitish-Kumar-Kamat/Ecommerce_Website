from django.shortcuts import render,redirect
from .models import Items,SurfItems,mobile,Transaction,ItemModel
from django.http import HttpResponse
import razorpay
from django.views.decorators.csrf import csrf_exempt


def home(req):
	cart=req.session.get('cart')
	if cart==None:
		req.session['cart']={}
		#print(dict(req.session))
	data=Items.objects.all()
	return render(req,"product/index.html",{'data':data})


def aboutus(req):
	return render(req,"product/about.html")

def contact(req):
	return render(req,"product/contact.html")

def prodetail(req,id):
	if req.method=="POST":
		stock=int(req.POST.get('instock'))
		required=int(req.POST.get('req_quan'))
		Id=int(req.POST.get('id_product'))
		cat="alitt"
		print(type(stock))
		print(type(required))
		if required > stock:
			data=Items.objects.get(pk=id)
			msg='Inappropriate Choice'
			return render(req,"product/prodetail.html",{'data':data,'msg':msg,'Id':Id,'cat':cat})
		cat_id=cat+str(Id)
		cart=req.session.get('cart')
		old=cart.get(cat_id)
		print(cart)
		if old:
			cart[cat_id]=required+old
		else:
			cart[cat_id]=required
		req.session['cart']=cart
		# cart=req.session.get('cart')
		# print(cart)
		msgg='Item added to cart'
		data=Items.objects.get(pk=id)
		return render(req,"product/prodetail.html",{'data':data,'msgg':msgg,'cat':cat})
	cat="alitt"
	data=Items.objects.get(pk=id)
	return render(req,"product/prodetail.html",{'data':data,'cat':cat})

def allitems(req):
	if req.method=="POST" and req.POST.get('max') and req.POST.get('min'):
		max=int(req.POST.get('max'))
		min=int(req.POST.get('min'))
		data1=Items.objects.all()
		return render(req,"product/myfilter.html",{'data1':data1,'max':max,'min':min})
	data=Items.objects.all() 
	return render(req,"product/allitems.html",{'data':data})


def surf(req):
	if req.method=="POST" and req.POST.get('max') and req.POST.get('min'):
		max=int(req.POST.get('max'))
		min=int(req.POST.get('min'))
		data2=SurfItems.objects.all()
		return render(req,"product/myfilter.html",{'data2':data2,'max':max,'min':min})
	data=SurfItems.objects.all() 
	return render(req,"product/surf.html",{'data':data})


def surfTask(req,pk):
	if req.method=="POST":
		stock=int(req.POST.get('instock'))
		required=int(req.POST.get('req_quan'))
		Id=int(req.POST.get('id_product'))
		cat="surf"
		if required > stock:
			data=SurfItems.objects.get(pk=pk)
			msg='Inappropriate Choice'
			return render(req,"product/prodetail.html",{'data':data,'msg':msg,'Id':Id,'cat':cat})
		
		cat_id=cat+str(Id)
		cart=req.session.get('cart')  #local variable
		old=cart.get(cat_id)
		print(cart)
		if old:
			cart[cat_id]=required+old
		else:
			cart[cat_id]=required
		req.session['cart']=cart  #assign new value to cart
		msgg='Item added to cart'
		data=SurfItems.objects.get(pk=pk)
		return render(req,"product/prodetail.html",{'data':data,'msgg':msgg,'cat':cat})
	cat="surf"
	data=SurfItems.objects.get(pk=pk)
	return render(req,"product/prodetail.html",{'data':data,'cat':cat})

def mobiledata(req):
	if req.method=="POST" and req.POST.get('max') and req.POST.get('min'):
		max=int(req.POST.get('max'))
		min=int(req.POST.get('min'))
		data3=mobile.objects.all()
		return render(req,"product/myfilter.html",{'data3':data3,'max':max,'min':min})
	data=mobile.objects.all()
	return render(req,"product/mobile.html",{'data':data})

def mobileTask(req,pk):
	if req.method=="POST":
		stock=int(req.POST.get('instock'))
		required=int(req.POST.get('req_quan'))
		Id=int(req.POST.get('id_product'))
		cat="mobi"
		print(type(stock))
		print(type(required))
		if required > stock:
			data=mobile.objects.get(pk=pk)
			msg='Inappropriate Choice'
			return render(req,"product/prodetail.html",{'data':data,'msg':msg,'Id':Id,'cat':cat})
		
		cat_id=cat+str(Id)
		cart=req.session.get('cart')  #local variable
		old=cart.get(cat_id)
		print(cart)
		if old:
			cart[cat_id]=required+old
		else:
			cart[cat_id]=required
		req.session['cart']=cart  #assign new value to cart
		msgg='Item added to cart'
		data=mobile.objects.get(pk=pk)
		return render(req,"product/prodetail.html",{'data':data,'msgg':msgg,'cat':cat})
	cat="mobi"
	data=mobile.objects.get(pk=pk)
	return render(req,"product/prodetail.html",{'data':data,'cat':cat})


def mycart(req):
	data=req.session.get('cart')
	print(data)
	list_final=[]
	GT=0
	for i,j in data.items():
		if "alitt" in i:
			cat="alitt"
			id=int(i[5:])
			d1=Items.objects.get(pk=id)
			price=d1.price
			total=j*price
			lis=[d1,j,total,cat]
			list_final.append(lis)
			GT+=total

		if "surf" in i:  #surf2
			cat="surf"
			id=int(i[4:])
			d1=SurfItems.objects.get(pk=id)
			price=d1.price
			total=j*price
			lis=[d1,j,total,cat]
			list_final.append(lis)
			GT+=total
			
		if "mobi" in i:  #mobi2
			cat="mobi"
			id=int(i[4:])
			d1=mobile.objects.get(pk=id)
			price=d1.price
			total=j*price
			lis=[d1,j,total,cat]
			list_final.append(lis)
			GT+=total
	dcharge=GT+40
	return render(req,"product/mycart.html",{'list_final':list_final,'GT':GT,'dcharge':dcharge})



def mysearch(req):
	if req.method=="POST":
		search=req.POST.get('psearch')
		d1=Items.objects.filter(name__icontains=search)
		d2=SurfItems.objects.filter(name__icontains=search)
		d3=mobile.objects.filter(name__icontains=search)
		if d1 or d2 or d3:
			return render(req,"product/mysearch.html",{'d1':d1,'d2':d2,'d3':d3})
	
	msg="Sorry, no results found!"
	return render(req,"product/mysearch.html",{'msg':msg})


def afterclickplace(req):
	if req.user.is_authenticated:
		data=req.session.get('cart')
		print(data)
		list_final=[]
		GT=0
		for i,j in data.items():
			if "alitt" in i:
				id=int(i[5:])
				d1=Items.objects.get(pk=id)
				price=d1.price
				total=j*price
				lis=[d1,j,total]
				list_final.append(lis)
				GT+=total
				
			if "surf" in i:  #surf2
				id=int(i[4:])
				d1=SurfItems.objects.get(pk=id)
				price=d1.price
				total=j*price
				lis=[d1,j,total]
				list_final.append(lis)
				GT+=total
				
			if "mobi" in i:  #mobi2
				id=int(i[4:])
				d1=mobile.objects.get(pk=id)
				price=d1.price
				total=j*price
				lis=[d1,j,total]
				list_final.append(lis)
				GT+=total
		dcharge=GT+40
		return render(req,"product/afterclickplace.html",{'list_final':list_final,'GT':GT,'dcharge':dcharge})

	else:
		return redirect('/auth1/login/')


def buy_now(req,id,cat):
	global required
	global myid
	global total
	global price
	global name
	if req.method=="POST":
		if req.user.is_authenticated:
			stock=int(req.POST.get('instock'))
			required=int(req.POST.get('req_quan'))
			myid=id
			if cat=="alitt":
				if required > stock:
					data=Items.objects.get(pk=id)
					msg='Inappropriate Choice'
					return render(req,"product/prodetail.html",{'data':data,'msg':msg,'myid':myid,'cat':cat})
				data=Items.objects.get(pk=id)
				name=data.name
				price=data.price
				quan=data.quantity
				total=required*price+40
				mydata={
				'name':name,
				'requan':required,
				'price':price,
				'total':total,
				'cat':cat,
				}
				return render(req,"product/afterclickbuy.html",mydata)
				
			if cat=="surf":
				if required > stock:
					data=SurfItems.objects.get(pk=id)
					msg='Inappropriate Choice'
					return render(req,"product/prodetail.html",{'data':data,'msg':msg,'myid':myid,'cat':cat})
				data=SurfItems.objects.get(pk=id)
				name=data.name
				price=data.price
				quan=data.quantity
				total=required*price+40
				mydata={
				'name':name,
				'requan':required,
				'price':price,
				'total':total,
				'cat':cat,
				}
				return render(req,"product/afterclickbuy.html",mydata)

			if cat=="mobi":
				if required > stock:
					data=mobile.objects.get(pk=id)
					msg='Inappropriate Choice'
					return render(req,"product/prodetail.html",{'data':data,'msg':msg,'myid':myid,'cat':cat})
				data=mobile.objects.get(pk=id)
				name=data.name
				price=data.price
				quan=data.quantity
				total=required*price+40
				mydata={
				'name':name,
				'requan':required,
				'price':price,
				'total':total,
				'cat':cat,
				}
				return render(req,"product/afterclickbuy.html",mydata)
		else:
			return redirect('/auth1/login/')
	return render(req,"product/prodetail.html")


def buypayment(req):
	# def buypayment(req,cat):
	# if req.method=="POST":
	# 	user=req.user
	# 	insdata=Transaction(user=user,cat=cat,cat_id=myid,purchased_quan=required)
	# 	insdata.save()
	# return redirect('/')
	if req.method=="POST":
		user=req.user
		amount = total * 100
		client = razorpay.Client(auth=("rzp_test_YOZmSe3bpko5fp" , "uY7cDNZKy1MMyTNYNOPvw3uK" ))
		response_payment = client.order.create({'amount':amount, 'currency':'INR',
                              'payment_capture':'1' })
							  
		print(response_payment)
		order_status = response_payment['status']
		order_id = response_payment['id']
		
		if order_status=='created':
			product = ItemModel(user=user , amount =amount , order_id = response_payment['id'],)
			product.save()
			response_payment['user'] = user
		
			insdata=Transaction(user=user,cat_id=myid,purchased_quan=required)
			insdata.save()
			return render(req,'product/afterclickbuy.html',{'payment':response_payment,'name':name,'requan':required,'price':price,'total':total})
		return render(req,'product/afterclickbuy.html')





# def make_payment(req):
# 	if req.method=='POST':
# 		user=req.user
# 		data=req.session.get('cart')
# 		for i,j in data.items():
# 			if 'alitt' in i:
# 				cat='alitt'
# 				id=int(i[5:])
# 				quan=j
# 				ins=Transaction(user=user,cat=cat,cat_id=id,purchased_quan=quan)
# 				ins.save()

# 			if 'surf' in i:
# 				cat='surf'
# 				id=int(i[4:])
# 				quan=j
# 				ins=Transaction(user=user,cat=cat,cat_id=id,purchased_quan=quan)
# 				ins.save()

# 			if 'mobi' in i:
# 				cat='mobi'
# 				id=int(i[4:])
# 				quan=j
# 				ins=Transaction(user=user,cat=cat,cat_id=id,purchased_quan=quan)
# 				ins.save()
# 		req.session['cart']={}
# 		return redirect('/')




def deletecart(req,id,cat):
	if cat=="alitt":
		print('delete')
		data=req.session.get('cart')
		cat_id=cat+str(id)
		data.pop(cat_id)
		req.session['cart']=data

	if cat=="surf":
		print('delete')
		data=req.session.get('cart')
		cat_id=cat+str(id)
		data.pop(cat_id)
		req.session['cart']=data

	if cat=="mobi":
		print('delete')
		data=req.session.get('cart')
		cat_id=cat+str(id)
		data.pop(cat_id)
		req.session['cart']=data
	return redirect('/cart/')





# def update(req,id,cat):
# 	data=req.session.get('cart')
# 	if req.method=="POST":
# 		upd=req.POST['upquantity']
# 		cat=req.POST['pro_id']
# 		cart=req.session.get('cart')
# 		cat_id=cat+str(id)
# 		cart[cat_id]=upd
# 		req.session['cart'] = cart
# 	return redirect('/cart/')






def item_payment(req):
	if req.method=="POST":
		user=req.user
		data=req.session.get('cart')
		print(data)
		list_final=[]
		GT=0
		for i,j in data.items():
			if "alitt" in i:
				id=int(i[5:])
				d1=Items.objects.get(pk=id)
				price=d1.price
				total=j*price
				lis=[d1,j,total]
				list_final.append(lis)
				GT+=total
				
			if "surf" in i:  #surf2
				id=int(i[4:])
				d1=SurfItems.objects.get(pk=id)
				price=d1.price
				total=j*price
				lis=[d1,j,total]
				list_final.append(lis)
				GT+=total
				
			if "mobi" in i:  #mobi2
				id=int(i[4:])
				d1=mobile.objects.get(pk=id)
				price=d1.price
				total=j*price
				lis=[d1,j,total]
				list_final.append(lis)
				GT+=total
		dcharge=GT+40
		
		amount = dcharge * 100
		client = razorpay.Client(auth=("rzp_test_YOZmSe3bpko5fp" , "uY7cDNZKy1MMyTNYNOPvw3uK" ))
		response_payment = client.order.create({'amount':amount, 'currency':'INR',
                              'payment_capture':'1' })
							  
		print(response_payment)
		order_status = response_payment['status']
		order_id = response_payment['id']
		
		if order_status=='created':
			product = ItemModel(user=user , amount =amount , order_id = response_payment['id'],)
			product.save()
			response_payment['user'] = user

			data=req.session.get('cart')
			for i,j in data.items():
				if 'alitt' in i:
					cat='alitt'
					id=int(i[5:])
					quan=j
					ins=Transaction(user=user,cat=cat,cat_id=id,purchased_quan=quan)
					ins.save()
					
				if 'surf' in i:
					cat='surf'
					id=int(i[4:])
					quan=j
					ins=Transaction(user=user,cat=cat,cat_id=id,purchased_quan=quan)
					ins.save()
					
				if 'mobi' in i:
					cat='mobi'
					id=int(i[4:])
					quan=j
					ins=Transaction(user=user,cat=cat,cat_id=id,purchased_quan=quan)
					ins.save()

			req.session['cart']={}
			return render(req,'product/afterclickplace.html',{'payment':response_payment,'list_final':list_final,'GT':GT,'dcharge':dcharge})
		return render(req,'product/afterclickbuyplace.html')



@csrf_exempt
def payment_status(req):
    if req.method=='POST':	
        response = req.POST
        print(response)
        params_dict = {
            'razorpay_order_id': response['razorpay_order_id'],
            'razorpay_payment_id': response['razorpay_payment_id'],
            'razorpay_signature': response['razorpay_signature']
        }

        # client instance
        client = razorpay.Client(auth=("rzp_test_YOZmSe3bpko5fp" , "uY7cDNZKy1MMyTNYNOPvw3uK" ))

        try:
            status = client.utility.verify_payment_signature(params_dict)
            item = ItemModel.objects.get(order_id=response['razorpay_order_id'])
            item.razorpay_payment_id = response['razorpay_payment_id']
            item.paid = True
            item.save()
            return render(req, 'product/payment_status.html', {'status': True})
        except:
            return render(req, 'product/payment_status.html', {'status': False})
    return render(req, 'product/payment_status.html')



def transactionData(req):
	if req.user.is_authenticated:
		tran=ItemModel.objects.all()
		return render(req, 'product/tran.html',{'tran':tran})
	else:
		return redirect('/auth1/login/')