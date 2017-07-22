from django.shortcuts import render

from django.views import generic

from .models import Descripcion


class AboutView(generic.ListView):
    template_name = 'pages/about.html'
    context_object_name = 'description_list'

    def get_queryset(self):
        return Descripcion.objects.order_by('orden')

