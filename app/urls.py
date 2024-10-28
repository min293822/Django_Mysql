from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('studentDetail/', views.studentDetail_view, name='studentDetail'),
  path('subjectDetails/', views.subjectDetails_view, name='subjectDetails'),
  path('testDetails/', views.testDetails_view, name='testDetails'),
  path('login/', views.login_view, name='login'),
  path('signup/', views.signup_view, name='signup'),
  path('logout/', views.logout_view, name='logout'),
  ]