from django.urls import path, include
from . import views

app_name = 'user'
urlpatterns = [
	path('accounts/profile', views.ProfileView.as_view(), name='profile'),
	path('accounts/profile/new', views.NewProfileView.as_view(), name='new_profile'),
    path('accounts/profile/change/<slug:slug>', views.ProfileUpdateView.as_view(), name='update_profile'),
	path('account/', include('django.contrib.auth.urls')),
    path('account/create', views.SignUpView.as_view(), name='signup'),
]