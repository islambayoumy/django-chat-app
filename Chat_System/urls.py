from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth.views import login, logout
from chat_app.views import AuthView, MessengerView, RestAPIView
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    url(r'^$', AuthView.login_redirect, name='login_redirect'),
    url(r'^admin/', admin.site.urls),
    url(r'^messenger/$', MessengerView.index),
    url(r'^login/$', login, {'template_name':'chat_app/login.html'}, name='login'),
    url(r'^logout/$', logout, {'template_name':'chat_app/logout.html'}, name='logout'),
    url(r'^signup/$', AuthView.signup, name='signup'),

    url(r'^api/users_list/$', RestAPIView.UsersList.as_view(), name='users_list'),
    
]

urlpatterns = format_suffix_patterns(urlpatterns)
