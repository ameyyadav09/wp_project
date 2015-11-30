from django.conf.urls import  patterns, include, url 

urlpatterns = patterns('',
	url(r'^home/$','mymusic.views.home'),
	url(r'^signup/$','mymusic.views.signup'),
	url(r'^signin/$','mymusic.views.signin'),
	url(r'^auth/$', 'mymusic.views.auth_view'),
	url(r'^logged/$', 'mymusic.views.logged_in'),
	url(r'^admin_auth/$', 'mymusic.views.admin_auth'),
	url(r'^adminpage/$', 'mymusic.views.admin_logged_in'),
	url(r'^adminlogin/$','mymusic.views.adminlogin'),
	url(r'^create/$', 'mymusic.views.create'),
	url(r'^uploadsong/$','mymusic.views.create'),
	url(r'^search/$', 'mymusic.views.search'),
	url(r'^play/(?P<song_id>\d+)/$', 'mymusic.views.playsong'),
	)