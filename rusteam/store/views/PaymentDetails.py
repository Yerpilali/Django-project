from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from ..models import PaymentDetails


class PaymentDetailsListView(ListView):
    model = PaymentDetails
    template_name = 'PaymentDetails/index.html'
    context_object_name = 'PaymentDetailss'


class PaymentDetailsDetailView(DetailView):
    model = PaymentDetails
    template_name = 'PaymentDetails/detail.html'
    context_object_name = 'PaymentDetails'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class PaymentDetailsCreateView(CreateView):
    model = PaymentDetails
    template_name = 'PaymentDetails/create.html'
    context_object_name = 'PaymentDetails'

    fields = ['Owners_name', 'Card', 'CVV_code', 'CloseDate']


class PaymentDetailsUpdateView(UpdateView):
    model = PaymentDetails
    template_name = 'PaymentDetails/edit.html'
    context_object_name = 'PaymentDetails'

    fields = ['Owners_name', 'Card', 'CVV_code', 'CloseDate']


class PaymentDetailsDeleteView(DeleteView):
    model = PaymentDetails
    template_name = 'PaymentDetails/delete.html'
    context_object_name = 'PaymentDetails'
    success_url = reverse_lazy('pd')
