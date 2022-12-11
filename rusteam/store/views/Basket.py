from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from ..models import Basket


class BasketListView(ListView):
    model = Basket
    template_name = 'Basket/index.html'
    context_object_name = 'Baskets'


class BasketDetailView(DetailView):
    model = Basket
    template_name = 'Basket/detail.html'
    context_object_name = 'Basket'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class BasketCreateView(CreateView):
    model = Basket
    template_name = 'Basket/create.html'
    context_object_name = 'Basket'

    fields = ['price', 'sale', 'user_id', 'product_id']


class BasketUpdateView(UpdateView):
    model = Basket
    template_name = 'Basket/edit.html'
    context_object_name = 'Basket'

    fields = ['price', 'sale', 'user_id', 'product_id']


class BasketDeleteView(DeleteView):
    model = Basket
    template_name = 'Basket/delete.html'
    context_object_name = 'Basket'
    success_url = reverse_lazy('bas')
