
from django.urls import path
from django.conf.urls import url
from . import views
urlpatterns = [

    path('about',views.about,name='about'),
    path('home',views.home,name='home'),
    path('sign_up', views.sign_up, name='sign_up'),
    path('activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})',
        views.activate, name='activate'),
    path('login',views.loginIn,name='login'),
    path('insertPgDetails',views.insertPgDetails,name='insertPgDetails'),
    path('searchForPg',views.searchForPg,name='searchForPg'),
    path('updatePgDetails',views.updatePgDetails,name='updatePgDetails'),
    path('viewPgAllDetails',views.viewPgAllDetails,name='viewPgAllDetails'),
    path('logOut', views.logOut, name='logOut'),

]
