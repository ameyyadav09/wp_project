from django.shortcuts import render
from forms import UserDetailsForm, SongsForm
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response
from models import Userdetails, Admins, Songs
from django.template import RequestContext
from django.core.context_processors import csrf
from django.contrib import auth
from django.shortcuts import get_object_or_404
from django.views.generic.base import TemplateView

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
	try:
		user = Userdetails.objects.get(email=username)
	except Userdetails.DoesNotExist:
		return HttpResponseRedirect('/mymusic/home')
	if user is not None:
		if user.password == password:
			return render_to_response('logged.html',{'username' : username})
		else:
			html = "<html><body>Password Error</body></html>"
			return HttpResponse(html)
	else:
		html = "<html><body>username Errot</body></Html>"
		return HttpResponse(html)

def adminlogin(request):
	args = {}
	args.update(csrf(request))
	return render_to_response('adminlogin.html',args)

def admin_auth(request):
	username = request.GET.get('username','')
	password = request.GET.get('password','')
	try:
		user = Admins.objects.get(username=username)
	except Admins.DoesNotExist:
		return HttpResponseRedirect('/mymusic/home')
	if user is not None:
		if user.password == password:
			return render_to_response('adminpage.html',{'username':username})
		else:
			html = "<html><body>Password Error</body></html>"
			return HttpResponse(html)
	else:
		html = "<html><body>username Error</body></Html>"
		return HttpResponse(html)

def admin_logged_in(request):
	if 'username' in request.COOKIES:
		return render(request,'adminpage.html')

def logged_in(request):
	if 'username' in request.COOKIES:
		return render(request, 'logged.html')

def create(request):
	if request.POST:
		form = SongsForm(request.POST,request.FILES)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/mymusic/uploadsong')
	else:
		form = SongsForm()
	args = {}
	args.update(csrf(request))
	args['form'] = form
	return render_to_response('uploadsong.html', args)

def search(request):
	val = request.GET.get('search','')
	return render_to_response('result.html',
		{'songs':Songs.objects.filter(language=val),})

def playsong(request, song_id):
	return render_to_response('playsong.html', {'song':Songs.objects.get(id=song_id)})