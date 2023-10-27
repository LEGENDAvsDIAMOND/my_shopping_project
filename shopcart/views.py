import os
import pandas as pd
from django.http import JsonResponse, HttpResponse
from django.db.models import Sum
from rest_framework.viewsets import ModelViewSet
from .models import ShopCart
from .serializers import ShopCartSerializer
import xlsxwriter

class ShopCardViewSet(ModelViewSet):
    queryset = ShopCart.objects.all()
    serializer_class = ShopCartSerializer

def purchase_history(request, user_id=None):
    queryset = ShopCart.objects.all()
    if user_id:
        queryset = queryset.filter(owner_id=user_id)
    serializer = ShopCartSerializer(queryset, many=True)
    data = serializer.data

    df = pd.DataFrame(data)

    path = 'C:/Users/User/Music/purchase_history.xlsx'


    writer = pd.ExcelWriter(path, engine='xlsxwriter')
    df.to_excel(writer, index=False)
    writer.book.close()

    response = JsonResponse({'excel_file_url': '/media/purchase_history.xlsx'})
    response['Content-Disposition'] = 'attachment; filename="purchase_history.xlsx"'
    return response

def check_purchase_total(request, customer_id=None):
    total_purchase = ShopCart.objects.filter(owner_id=customer_id).aggregate(total=Sum('total_price'))['total']
    is_over_1000000 = total_purchase > 1000000 if total_purchase else False
    data = {'is_over_1000000': is_over_1000000}
    return JsonResponse(data)
