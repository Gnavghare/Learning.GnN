from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'accounts'

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='courses:home'), name='logout'),
    path('profile/', views.profile, name='profile'),
    path('enroll/<int:course_id>/', views.enroll_course, name='enroll_course'),
    path('unenroll/<int:course_id>/', views.unenroll_course, name='unenroll_course'),
]