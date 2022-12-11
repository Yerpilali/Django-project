from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from ..models import Role


class RoleListView(ListView):
    model = Role
    template_name = 'Role/index.html'
    context_object_name = 'Roles'


class RoleDetailView(DetailView):
    model = Role
    template_name = 'Role/detail.html'
    context_object_name = 'Role'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class RoleCreateView(CreateView):
    model = Role
    template_name = 'Role/create.html'
    context_object_name = 'Role'

    fields = ['name', 'time_entry', 'dogovor', 'user_id']


class RoleUpdateView(UpdateView):
    model = Role
    template_name = 'Role/edit.html'
    context_object_name = 'Role'

    fields = ['name', 'time_entry', 'dogovor', 'user_id']


class RoleDeleteView(DeleteView):
    model = Role
    template_name = 'Role/delete.html'
    context_object_name = 'Role'
    success_url = reverse_lazy('rol')
