from django.shortcuts import render
from django.views.generic import DetailView,TemplateView,ListView
from .models import Product,Category
# Create your views here.



class ProductDetailView(DetailView):
    template_name = "product/product_detail.html"
    model = Product


class NavbarPartialView(TemplateView):
    template_name = 'includes/navbar.html'

    def get_context_data(self, **kwargs):
        context=super(NavbarPartialView,self).get_context_data()
        context['categories']=Category.objects.all()
        return context

class CategoryStyle(TemplateView):
    template_name = 'category.html'


    def get_context_data(self, **kwargs):
        context = super(CategoryStyle,self).get_context_data()#مقدار داخل پرایتز سوپر اختیاریه
        context['categories'] = Category.objects.all()
        return context


class ProductListView(ListView):
    template_name = 'product/product_list.html'
    # model = Product
    # context_object_name = 'products'
    # paginate_by = 4
    queryset = Product.objects.all()

    def get_context_data(self, **kwargs):
        request=self.request
        color=request.GET.getlist('color')
        size=request.GET.getlist('size')
        min_price=request.GET.get('min_price')
        max_price=request.GET.get('max_price')
        queryset=Product.objects.all()
        if color:
            queryset=queryset.filter(color__title__in=color).distinct()
        if size:
            queryset=queryset.filter(size__title__in=size).distinct()
        if max_price and min_price:
            queryset=queryset.filter(price__lte=max_price,price__gte=min_price)
        context = super(ProductListView,self).get_context_data()#مقدار داخل پرایتز سوپر اختیاریه
        context['object_list'] = queryset
        return context