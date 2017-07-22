from django.views import generic

from .models import ProductAmount


class IndexView(generic.ListView):
    template_name = 'pages/home.html'
    context_object_name = 'product_list'

    def get_queryset(self):
        return ProductAmount.objects.order_by('product', 'amount')
