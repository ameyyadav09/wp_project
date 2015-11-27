from django.shortcuts import render
from forms import UserDetailsForm
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response
from models import Userdetails
from django.template import RequestContext
from django.core.context_processors import csrf
from django.contrib import auth
from django.shortcuts import get_object_or_404

# Create your views here.

def home(request):
	return render(request,'home.html')

def signup(request):
	form = UserDetailsForm()
	if request.POST:
		form = UserDetailsForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/mymusic/home')
		else:
			temp = "<html><boby>Email-id or the mobile number already exists</body></html>"
			return HttpResponse(temp)
	return render_to_response('signup.html',{'form':form}, context_instance=RequestContext(request))

def signin(request):
	args = {}
	args.update(csrf(request))
	return render_to_response('signin.html',args)

def auth_view(request):
	username = request.GET.get('username','')
	password = request.GET.get('password','')
	# user = Userdetails.objects.get(email=username)
	try:
		user = Userdetails.objects.get(email=username)
	except Userdetails.DoesNotExist:
		return HttpResponseRedirect('/mymusic/home')
	if user is not None:
		if user.password == password:
			# auth.login(request, user)
			return HttpResponseRedirect('/mymusic/home')
		else:
			html = "<html><body>Password Error</body></html>"
			return HttpResponse(html)
	else:
		html = "<html><body>username Errot</body></Html>"
		return HttpResponse(html)

