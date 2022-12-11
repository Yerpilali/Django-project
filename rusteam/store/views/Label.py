from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from ..models import Label


class LabelListView(ListView):
    model = Label
    template_name = 'Label/index.html'
    context_object_name = 'Labels'


class LabelDetailView(DetailView):
    model = Label
    template_name = 'Label/detail.html'
    context_object_name = 'Label'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class LabelCreateView(CreateView):
    model = Label
    template_name = 'Label/create.html'
    context_object_name = 'Label'

    fields = ['tag_id', 'product_id']


class LabelUpdateView(UpdateView):
    model = Label
    template_name = 'Label/edit.html'
    context_object_name = 'Label'

    fields = ['tag_id', 'product_id']


class LabelDeleteView(DeleteView):
    model = Label
    template_name = 'Label/delete.html'
    context_object_name = 'Label'
    success_url = reverse_lazy('lab')
