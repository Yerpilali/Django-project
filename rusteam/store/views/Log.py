from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from ..models import Log


class LogListView(ListView):
    model = Log
    template_name = 'Log/index.html'
    context_object_name = 'Logs'


class LogDetailView(DetailView):
    model = Log
    template_name = 'Log/detail.html'
    context_object_name = 'Log'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class LogCreateView(CreateView):
    model = Log
    template_name = 'Log/create.html'
    context_object_name = 'Log'

    fields = ['time_out', 'time_entry', 'user_id']


class LogUpdateView(UpdateView):
    model = Log
    template_name = 'Log/edit.html'
    context_object_name = 'Log'

    fields = ['time_out', 'time_entry', 'user_id']


class LogDeleteView(DeleteView):
    model = Log
    template_name = 'Log/delete.html'
    context_object_name = 'Log'
    success_url = reverse_lazy('log')
