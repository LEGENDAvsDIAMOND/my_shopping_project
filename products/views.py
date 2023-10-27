from rest_framework import viewsets
from products.models import Products
from products.serializers import ProductsSerializer
from django.http import JsonResponse
from django.utils.timezone import now
from products.models import Products
from django.db.models import Count

def best_selling_product(request):
    best_selling = Products.objects.annotate(total_sales=Count('items')).order_by('-total_sales').first()

    if best_selling:
        data = {
            'product_id': best_selling.id,
            'product_name': best_selling.name,
            'total_sales': best_selling.total_sales
        }
    else:
        data = {
            'product_id': None,
            'product_name': None,
            'total_sales': 0
        }

    return JsonResponse(data)

def expired_products(request):
    expired_products = Products.objects.filter(end_date__lt=now())
    data = {'expired_products': list(expired_products.values())}
    return JsonResponse(data)

def total_product_amount(request):
    total_amount = Products.objects.count()
    data = {'total_amount': total_amount}
    return JsonResponse(data)

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer