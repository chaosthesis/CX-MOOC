from django.conf.urls import patterns, url
from CXMOOC_Account import views

urlpatterns = patterns('',
    url(r'signup/',views.signup_view),
    url(r'login/', views.login_view),
    url(r'logout/', views.logout_view),
    url(r'update/', views.update_view),
)