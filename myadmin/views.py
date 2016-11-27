from django.shortcuts import render, render_to_response
import django.apps
from django.http import HttpResponse, HttpResponseRedirect
import json

from django.views.generic import ListView, DetailView, DeleteView, UpdateView, CreateView
from django.utils import timezone

from django.views.decorators.http import require_http_methods

from django.core.urlresolvers import reverse_lazy

from myadmin.models import *

# VERY IMPORTANT
# HERE IS THE LIST OF MODELS "REGISTERED" IN ADMIN PANEL
models = ["Model1", "Person", "Book"]

def get_model(model_name):
    tmp = django.apps.apps.get_models()
    return [obj for obj in tmp if obj.__name__ == model_name][0]

def myadmin_home(request):
    model_list = []
    for obj in MyAdmin.objects.all():
        model_list.append(obj.name)
    return render(request, 'myadmin/myadmin_home.html',
        context = {'model_list': model_list})

@require_http_methods(['GET', 'POST'])
def myadmin_add(request):
    print(request.POST)
    response = json.dumps(request.POST)
    success_url = reverse_lazy('myadmin-home')
    model_list = django.apps.apps.get_models()
    chosen_model = [obj.__name__ for obj in model_list if obj.__name__ in request.POST.values()]
    print(chosen_model)
    if MyAdmin.objects.filter(name = chosen_model[0]).exists():
        return HttpResponse("Model {} already exists in database".format(chosen_model[0]))
    elif chosen_model:
        a = MyAdmin()
        a.name = chosen_model[0]
        a.save()

    return HttpResponseRedirect(success_url)

def myadmin_delete(request, model_name):
    success_url = reverse_lazy('myadmin-home')
    model = MyAdmin.objects.get(name = model_name)
    print(request.method, request.POST)
    if request.method == "POST" and "delete" in request.POST:
        model.delete()
        return HttpResponseRedirect(success_url)
    else:
        return HttpResponse("Not implemented")


def myadmin_all(request):
    model_list = django.apps.apps.get_models()
    model_list = [obj.__name__ for obj in model_list if obj.__name__ in models]
    return render(request, 'myadmin/myadmin_list.html',
        context = {'model_list': model_list})


# PARTICUAL OBJECT RELATED VIEWS
def myadmin_object_list(request, model_name):
    view = ListView
    view.model = get_model(model_name)
    view.template_name = "myadmin/object_list.html"

    def get_context_data(self, **kwargs):
        context = super(view, self).get_context_data(**kwargs)
        context['model_name'] = model_name
        return context

    view.get_context_data = get_context_data
    return view.as_view()(request)


def myadmin_detail(request, model_name, pk):
    from collections import OrderedDict
    detail = DetailView
    detail.model = get_model(model_name)
    detail.template_name = "myadmin/object_detail.html"
    obj = detail.model.objects.get(id = pk)
    def get_model_fields(model):
        f_name = [f.name for f in detail.model._meta.get_fields()]
        a = []
        for f in f_name:
            a.append(getattr(obj, f))

        my_list = zip(f_name, a)
        return my_list

    detail.model.get_model_fields = get_model_fields

    def get_context_data(self, **kwargs):
        context = super(detail, self).get_context_data(**kwargs)
        context['model_name'] = model_name
        return context

    detail.get_context_data = get_context_data
    return detail.as_view()(request, pk=pk)

def myadmin_object_delete(request, model_name, pk):
    deletator = DeleteView
    deletator.model = get_model(model_name)
    deletator.success_url = reverse_lazy('myadmin-object-list',
        kwargs={'model_name': model_name},)
    def get_template_names(instance):
        return ['myadmin/delete_confirm.html']

    deletator.get_template_names = get_template_names
    return deletator.as_view()(request, pk=pk)

def myadmin_object_update(request, model_name, pk):
    updator = UpdateView
    updator.model = get_model(model_name)
    updator.success_url = reverse_lazy('myadmin-object-list',
        kwargs={'model_name': model_name})

    updator.fields = '__all__'
    def get_template_names(instance):
        return ['myadmin/object_update.html']

    updator.get_template_names = get_template_names
    return updator.as_view()(request, pk=pk)

def myadmin_object_create(request, model_name):
    creator = CreateView

    creator.model = get_model(model_name)
    creator.fields = '__all__'
    creator.success_url = reverse_lazy('myadmin-object-list', kwargs={'model_name': model_name})

    def get_template_names(instance):
        return ['myadmin/object_create.html']

    creator.get_template_names = get_template_names

    return creator.as_view()(request)
