from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from ..models import PaymentHistory


class PaymentHistoryListView(ListView):
    model = PaymentHistory
    template_name = 'PaymentHistory/index.html'
    context_object_name = 'PaymentHistorys'


class PaymentHistoryDetailView(DetailView):
    model = PaymentHistory
    template_name = 'PaymentHistory/detail.html'
    context_object_name = 'PaymentHistory'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class PaymentHistoryCreateView(CreateView):
    model = PaymentHistory
    template_name = 'PaymentHistory/create.html'
    context_object_name = 'PaymentHistory'

    fields = ['paysum', 'name', 'payday', 'priceback', 'user_id', 'product_id']


class PaymentHistoryUpdateView(UpdateView):
    model = PaymentHistory
    template_name = 'PaymentHistory/edit.html'
    context_object_name = 'PaymentHistory'

    fields = ['paysum', 'name', 'payday', 'priceback', 'user_id', 'product_id']


class PaymentHistoryDeleteView(DeleteView):
    model = PaymentHistory
    template_name = 'PaymentHistory/delete.html'
    context_object_name = 'PaymentHistory'
    success_url = reverse_lazy('ph')
