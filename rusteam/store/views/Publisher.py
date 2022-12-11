from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from ..models import Publisher


class PublisherListView(ListView):
    model = Publisher
    template_name = 'Publisher/index.html'
    context_object_name = 'Publishers'


class PublisherDetailView(DetailView):
    model = Publisher
    template_name = 'Publisher/detail.html'
    context_object_name = 'Publisher'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class PublisherCreateView(CreateView):
    model = Publisher
    template_name = 'Publisher/create.html'
    context_object_name = 'Publisher'

    fields = ['name_publisher', 'developer_id']


class PublisherUpdateView(UpdateView):
    model = Publisher
    template_name = 'Publisher/edit.html'
    context_object_name = 'Publisher'

    fields = ['name_publisher', 'developer_id']


class PublisherDeleteView(DeleteView):
    model = Publisher
    template_name = 'Publisher/delete.html'
    context_object_name = 'Publisher'
    success_url = reverse_lazy('pub')
