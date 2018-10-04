from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'shop'

urlpatterns = [
    # product list urls
    path('', views.product_list, name='product_list'),
    # slug urls
    path('product_list/<slug:category_slug>/', views.product_list, name='product_list_by_category'),
    # product detail urls
    path('product_detail/(<int:id>)/(<slug:slug>)/', views.product_detail, name='product_detail'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
