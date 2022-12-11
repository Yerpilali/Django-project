from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from ..models import Developer


class DeveloperListView(ListView):
    model = Developer
    template_name = 'Developer/index.html'
    context_object_name = 'Developers'


class DeveloperDetailView(DetailView):
    model = Developer
    template_name = 'Developer/detail.html'
    context_object_name = 'Developer'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class DeveloperCreateView(CreateView):
    model = Developer
    template_name = 'Developer/create.html'
    context_object_name = 'Developer'

    fields = ['name_developer']


class DeveloperUpdateView(UpdateView):
    model = Developer
    template_name = 'Developer/edit.html'
    context_object_name = 'Developer'

    fields = ['name_developer']


class DeveloperDeleteView(DeleteView):
    model = Developer
    template_name = 'Developer/delete.html'
    context_object_name = 'Developer'
    success_url = reverse_lazy('dev')
