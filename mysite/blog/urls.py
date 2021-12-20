from django.conf.urls import url
from django.contrib.auth import views as auth_views
from django.urls import path, include
from . import views
from .views import register
from blog.views import CustomLoginView  
from blog.forms import LoginForm

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    url(r'^post/(?P<pk>\d+)/comment/$', views.add_comment_to_post, name='add_comment_to_post'),
    url(r'^comment/(?P<pk>\d+)/approve/$', views.comment_approve, name='comment_approve'),
    url(r'^comment/(?P<pk>\d+)/remove/$', views.comment_remove, name='comment_remove'),
    path('post/<pk>/remove/', views.post_remove, name='post_remove'),
    path('register/', register, name="register"),
    path('login/', CustomLoginView.as_view(redirect_authenticated_user=True, template_name='blog/login.html',authentication_form=LoginForm), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='blog/logout.html'), name='logout'),

]
