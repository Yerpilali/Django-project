from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from ..models import Product


class ProductListView(ListView):
    model = Product
    template_name = 'Product/index.html'
    context_object_name = 'Products'


class ProductDetailView(DetailView):
    model = Product
    template_name = 'Product/detail.html'
    context_object_name = 'Product'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class ProductCreateView(CreateView):
    model = Product
    template_name = 'Product/create.html'
    context_object_name = 'Product'

    fields = ['name', 'price', 'discount', 'publisher_id', 'typekey_id']


class ProductUpdateView(UpdateView):
    model = Product
    template_name = 'Product/edit.html'
    context_object_name = 'Product'

    fields = ['name', 'price', 'discount', 'publisher_id', 'typekey_id']


class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'Product/delete.html'
    context_object_name = 'Product'
    success_url = reverse_lazy('prod')
