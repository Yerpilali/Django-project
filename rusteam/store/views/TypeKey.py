from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from ..models import TypeKey


class TypeKeyListView(ListView):
    model = TypeKey
    template_name = 'TypeKey/index.html'
    context_object_name = 'TypeKeys'


class TypeKeyDetailView(DetailView):
    model = TypeKey
    template_name = 'TypeKey/detail.html'
    context_object_name = 'TypeKey'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class TypeKeyCreateView(CreateView):
    model = TypeKey
    template_name = 'TypeKey/create.html'
    context_object_name = 'TypeKey'

    fields = ['name']


class TypeKeyUpdateView(UpdateView):
    model = TypeKey
    template_name = 'TypeKey/edit.html'
    context_object_name = 'TypeKey'

    fields = ['name']


class TypeKeyDeleteView(DeleteView):
    model = TypeKey
    template_name = 'TypeKey/delete.html'
    context_object_name = 'TypeKey'
    success_url = reverse_lazy('tk')
