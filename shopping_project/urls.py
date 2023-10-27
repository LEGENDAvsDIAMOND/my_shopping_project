"""
URL configuration for shopping_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include
from main_cus.views import MainCusListCreateView, MainCusRetrieveUpdateDestroyView
from django.urls import include, path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from shopcart.views import purchase_history
from shopcart.views import purchase_history, check_purchase_total
from products.views import total_product_amount, expired_products, best_selling_product

schema_view = get_schema_view(
    openapi.Info(
        title="Shopping Project API",
        default_version="v1",
        description="API documentation for the Shopping Project",
        terms_of_service="https://www.example.com/terms/",
        contact=openapi.Contact(email="contact@example.com"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('api/main_cus/', MainCusListCreateView.as_view(), name='main_cus-list-create'),
    path('api/main_cus/<int:pk>/', MainCusRetrieveUpdateDestroyView.as_view(), name='main_cus-retrieve-update-destroy'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('swagger.json', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('api/purchase-history/', purchase_history, name='purchase-history'),
    path('api/purchase-history/<int:user_id>/', purchase_history, name='purchase-history-user'),
    path('api/check-purchase-total/<int:customer_id>/', check_purchase_total, name='check_purchase_total'),
    path('api/total-product-amount/', total_product_amount, name='total_product_amount'),
    path('api/expired-products/', expired_products, name='expired_products'),
    path('api/best-selling-product/', best_selling_product, name='best_selling_product'),
]