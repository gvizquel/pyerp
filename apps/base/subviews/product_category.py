# Librerias Django
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, UpdateView

# Librerias en carpetas locales
from ...base.models import PyProductCategory

""" BEGIN CATEGORY PRODUCT"""
CATEGORY_FIELDS = [
    {'string': 'Nombre', 'field': 'name'},
    {'string': 'Categoría Padre', 'field': 'parent_id'},
]

CATEGORY_FIELDS_SHORT = ['name','parent_id']


class ProductCategoryListView(ListView):
    model = PyProductCategory
    template_name = 'erp/list.html'

    def get_context_data(self, **kwargs):
        context = super(ProductCategoryListView, self).get_context_data(**kwargs)
        context['title'] = 'Categorías de Productos'
        context['detail_url'] = 'product-category-detail'
        context['add_url'] = 'product-category-add'
        context['fields'] = CATEGORY_FIELDS
        return context


class ProductCategoryDetailView(DetailView):
    model = PyProductCategory
    template_name = 'erp/detail.html'

    def get_context_data(self, **kwargs):
        context = super(ProductCategoryDetailView, self).get_context_data(**kwargs)
        context['title'] = context['object'].name
        context['breadcrumbs'] = [{'url': 'product-category', 'name': 'Categorias de Productos'}]
        context['update_url'] = 'product-category-update'
        context['delete_url'] = 'product-category-delete'
        context['fields'] = CATEGORY_FIELDS
        return context


class ProductCategoryCreateView(CreateView):
    model = PyProductCategory
    fields = CATEGORY_FIELDS_SHORT
    template_name = 'erp/form.html'

    def get_context_data(self, **kwargs):
        context = super(ProductCategoryCreateView, self).get_context_data(**kwargs)
        context['title'] = 'Crear Categoria de Productos'
        context['breadcrumbs'] = [{'url': 'product-category', 'name': 'Categoria de Producto'}]
        context['back_url'] = reverse('product-category')
        return context


class ProductCategoryUpdateView(UpdateView):
    model = PyProductCategory
    fields = CATEGORY_FIELDS_SHORT
    template_name = 'erp/form.html'

    def get_context_data(self, **kwargs):
        context = super(ProductCategoryUpdateView, self).get_context_data(**kwargs)
        context['title'] = context['object'].name
        context['breadcrumbs'] = [{'url': 'product-category', 'name': 'Categoria de Producto'}]
        context['back_url'] = reverse('product-category-detail', kwargs={'pk': context['object'].pk})
        return context


@login_required(login_url="/erp/login")
def DeleteProductCategory(self, pk):
    product_category = PyProductCategory.objects.get(id=pk)
    product_category.delete()
    return redirect(reverse('product-category'))


""" END CATEGORY PRODUCT """
