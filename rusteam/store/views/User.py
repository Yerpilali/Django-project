from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from ..models import User


class UserListView(ListView):
    model = User
    template_name = 'User/index.html'
    context_object_name = 'Users'


class UserDetailView(DetailView):
    model = User
    template_name = 'User/detail.html'
    context_object_name = 'User'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class UserCreateView(CreateView):
    model = User
    template_name = 'User/create.html'
    context_object_name = 'User'

    fields = ['Nickname', 'Full_name', 'login', 'password', 'email', 'RegistrationDate', 'paymentdetails_id']


class UserUpdateView(UpdateView):
    model = User
    template_name = 'User/edit.html'
    context_object_name = 'User'

    fields = ['Nickname', 'Full_name', 'login', 'password', 'email', 'RegistrationDate', 'paymentdetails_id']


class UserDeleteView(DeleteView):
    model = User
    template_name = 'User/delete.html'
    context_object_name = 'User'
    success_url = reverse_lazy('use')
