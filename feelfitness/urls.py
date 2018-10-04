
"""Defines URL patterns for feelfitness"""
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

app_name = 'feelfitness'

urlpatterns = [
    # Home urls
    path('', views.index, name='index'),
    # sign urls
    path('sign/', views.sign, name='sign'),
    # about us urls
    path('about/', views.about, name='about'),
    # portfolio urls
    path('portfolio/', views.portfolio, name='portfolio'),
    # cancer awareness urls
    path('cancer_awareness/', views.cancer_awareness, name='cancer_awareness'),
    # product_promotion urls
    path('product_promotion/', views.product_promotion, name='product_promotion'),
    # u_me urls
    path('u_me/', views.u_me, name='u_me'),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


