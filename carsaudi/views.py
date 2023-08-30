

from django.views.generic import TemplateView, ListView, DetailView, CreateView

from carsaudi.models import Category, Product



class IndexView(TemplateView):
    template_name = 'carsaudi/index.html'
    extra_context = {
        'title': 'Автомобильный салон - Главная',
        'lending': 'Кредитование - Мечтайте смелее',
        'Online': 'Покупка онлайн',
        'description': 'Cведения, представленные на сайте, носят информационный характер и не являются публичной офертой',
        'Search': 'Поиск'
    }


    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['object_list'] = Category.objects.all()[:0]
        return context_data



class CategoryListView(ListView):
    model = Category
    extra_context = {
        'description': 'Машина должна быть частью тебя, а ты — её составной частью. Только так можно стать единственным в своем роде. Лучшая машина — новая машина!'
    }

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['object_list'] = Category.objects.all()
        return context_data


class ProductListView(ListView):
    model = Product

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(category_id=self.kwargs.get('pk'))[:4]

        return queryset

    def get_context_data(self, *args, **kwargs):
        context_data =super().get_context_data(*args, **kwargs)

        category_item = Category.objects.get(pk=self.kwargs.get('pk'))
        context_data['title'] = f'Модель автомобиля - {category_item.name}'

        return context_data


class ProductDetailView(DetailView):
    model = Product
    template_name = 'carsaudi/includes/inc_product.html'
    context_object_name = 'object'
    pk_url_kwarg = 'pk'

class ContactView(TemplateView):
     template_name = 'carsaudi/contacts.html'
     extra_context = {
         'title': 'Контакты'
     }


class ConnectionView(TemplateView):
    template_name = 'carsaudi/connection.html'
    extra_context = {
        'title': 'Обратная связь'
    }

    def get_context_data(self, **kwargs):
        if self.request.method == 'POST':
            name = self.request.POST.get('name')
            email = self.request.POST.get('email')
            message = self.request.POST.get('message')
            print(f'You have new message from {name}({email}): {message}')
        return super().get_context_data(**kwargs)


class StoreView(TemplateView):
    template_name = 'carsaudi/store.html'

class PrivacyView(TemplateView):
    template_name = 'carsaudi/privacy.html'

