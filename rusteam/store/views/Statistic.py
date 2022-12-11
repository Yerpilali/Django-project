from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from ..models import Statistic


class StatisticListView(ListView):
    model = Statistic
    template_name = 'Statistic/index.html'
    context_object_name = 'Statistics'


class StatisticDetailView(DetailView):
    model = Statistic
    template_name = 'Statistic/detail.html'
    context_object_name = 'Statistic'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class StatisticCreateView(CreateView):
    model = Statistic
    template_name = 'Statistic/create.html'
    context_object_name = 'Statistic'

    fields = ['name', 'amount_product', 'basket_id']


class StatisticUpdateView(UpdateView):
    model = Statistic
    template_name = 'Statistic/edit.html'
    context_object_name = 'Statistic'

    fields = ['name', 'amount_product', 'basket_id']


class StatisticDeleteView(DeleteView):
    model = Statistic
    template_name = 'Statistic/delete.html'
    context_object_name = 'Statistic'
    success_url = reverse_lazy('stat')
