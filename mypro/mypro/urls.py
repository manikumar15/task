from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include
from django.conf import settings
from django.views.static import serve
from myapp import views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',views.index),
    url(r'^index',views.index),
	url(r'^register',views.register),

	url(r'^homeView/', views.homeView),
    url(r'^create/', views.createView),
    url(r'^retrieve/', views.retrieveView),
    url(r'^update/', views.updateView),
    url(r'^delete/', views.deleteView),
	

]


