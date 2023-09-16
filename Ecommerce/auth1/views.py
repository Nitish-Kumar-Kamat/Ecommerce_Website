from django.shortcuts import render,redirect
from .forms import SignupForm,LoginForm,MyPasswordResetForm,MySetpasswordForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout

def sign_up(req):
	if req.method=="POST":
		fm=SignupForm(req.POST)  #You can do explicitily mention
		if fm.is_valid():
			fm.save()
			messages.success(req,"Signup successful")
			return redirect('/auth1/login/')
			# return render(req,'auth1/signup.html',{'fm':fm})
	else:
		fm=SignupForm()
	return render(req,'auth1/signup.html',{'fm':fm})

def log_in(req):
	if req.method=="POST":
		fm=LoginForm(request=req,data=req.POST)
		if fm.is_valid():
			a=fm.cleaned_data['username']
			b=fm.cleaned_data['password']
			user=authenticate(username=a,password=b)
			if user is not None:
				login(req,user)
				messages.success(req,"Login Successful")
				fm=LoginForm()
				return render(req,"auth1/login.html",{'fm':fm})
		else:
			msg="Invalid Username/Password"
			fm=LoginForm()
			return render(req,"auth1/login.html",{'fm':fm,'msg':msg})
	else:
		fm=LoginForm()
	return render(req,"auth1/login.html",{'fm':fm})

def log_out(req):
	logout(req)
	messages.success(req,"Logout successful")
	fm=LoginForm()
	return render(req,'auth1/login.html',{'fm':fm})

def pass_reset(req):
	fm=MyPasswordResetForm()
	return render(req,"auth1/pass_reset.html",{'fm':fm})
	
def mySetPass(req):
	pass
