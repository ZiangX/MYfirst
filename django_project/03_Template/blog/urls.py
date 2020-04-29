from . import views
from django.urls import path

urlpatterns = [
	# The 'blog-home' is the name for our url pattern, if we reference it, we actually reference to this route. When the url path change,
	# 	it will automatically update for all references with that unique name 
	path('', views.home, name = 'blog-home'),
	path('about/', views.about, name='blog-about')
]