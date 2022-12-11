from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from ..models import Tag


class TagListView(ListView):
    model = Tag
    template_name = 'Tag/index.html'
    context_object_name = 'Tags'


class TagDetailView(DetailView):
    model = Tag
    template_name = 'Tag/detail.html'
    context_object_name = 'Tag'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class TagCreateView(CreateView):
    model = Tag
    template_name = 'Tag/create.html'
    context_object_name = 'Tag'

    fields = ['name_tag']


class TagUpdateView(UpdateView):
    model = Tag
    template_name = 'Tag/edit.html'
    context_object_name = 'Tag'

    fields = ['name_tag']


class TagDeleteView(DeleteView):
    model = Tag
    template_name = 'Tag/delete.html'
    context_object_name = 'Tag'
    success_url = reverse_lazy('tag')
