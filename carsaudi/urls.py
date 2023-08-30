from django.urls import path

from carsaudi.apps import CarsaudiConfig
from carsaudi.views import IndexView, CategoryListView, ProductDetailView, ProductListView, ContactView, \
    ConnectionView, StoreView, PrivacyView

app_name = CarsaudiConfig.name

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('categorys/', CategoryListView.as_view(), name='categorys'),
    path('<int:pk>/products/', ProductListView.as_view(), name='category_product'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('contacts/', ContactView.as_view(), name='contacts'),
    path('connections/', ConnectionView.as_view(), name='connections'),
    path('store/', StoreView.as_view(), name='store'),
    path('privacy/', PrivacyView.as_view(), name='privacy'),
]