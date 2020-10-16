from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, ListView, DetailView
from .forms import CustomUserCreationForm, ProfileForm, CustomUserChangeForm, ProfileUpdateForm
from .models import CustomUser, Profile
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('user:login')
    template_name = 'registration/signup.html'

class UpdateUserView(LoginRequiredMixin, UpdateView):
    form_class = CustomUserChangeForm
    template_name = 'update.html'

class NewProfileView(LoginRequiredMixin, CreateView):
    form_class = ProfileForm
    template_name = 'user/new_profile.html'
    success_url = reverse_lazy('user:profile')

    def get_initial(self):
        initial = super().get_initial()
        initial['owner'] = self.request.user.username
        return initial

class ProfileView(LoginRequiredMixin, ListView):
    template_name = 'user/profile.html'
    context_object_name = 'profile'

    def get_queryset(self):
        qs = Profile.objects.all().filter(owner=self.request.user)
        return qs


class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    form_class = ProfileUpdateForm
    template = 'user/update_profile.html'
    success_url = reverse_lazy('qanda:ask')

    def get_queryset(self):
        return Profile.objects.all()