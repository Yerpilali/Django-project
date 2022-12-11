from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from ..models import WishList


class WishListListView(ListView):
    model = WishList
    template_name = 'WishList/index.html'
    context_object_name = 'WishLists'


class WishListDetailView(DetailView):
    model = WishList
    template_name = 'WishList/detail.html'
    context_object_name = 'WishList'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class WishListCreateView(CreateView):
    model = WishList
    template_name = 'WishList/create.html'
    context_object_name = 'WishList'

    fields = ['user_id', 'product_id']


class WishListUpdateView(UpdateView):
    model = WishList
    template_name = 'WishList/edit.html'
    context_object_name = 'WishList'

    fields = ['user_id', 'product_id']


class WishListDeleteView(DeleteView):
    model = WishList
    template_name = 'WishList/delete.html'
    context_object_name = 'WishList'
    success_url = reverse_lazy('wl')
