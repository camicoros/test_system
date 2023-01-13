from django.shortcuts import render
from django.views.generic import ListView

from testing_app.models import TestSet


class IndexView(ListView):
    model = TestSet
    template_name = 'testing_app/index.html'
    context_object_name = 'tests'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
