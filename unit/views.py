# from django.shortcuts import render
# from rest_framework.response import Response
# from rest_framework.decorators import api_view
# from .models import Operation

# @api_view(['POST'])
# def converter(request):
#     data = request.data
#     value = data.get('value')
#     to_unit = data.get('to_unit')

#     factors = {'kg': 0.001, 'ton': 0.000001}

#     if to_unit not in factors:
#         return Response('please enter a valid unit', status=400)

#     converted_value = value * factors[to_unit]

#     operation = Operation(value=value, converted_value=converted_value, to_unit=to_unit)
#     operation.save()

#     return Response({
#         "value": value,
#         "unit": to_unit,
#         "converted_value": converted_value
#     })
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['POST'])
def convert_grams(request):
    # دریافت مقدار گرم از پارامتر ورودی
    grams = request.data.get("value")

    if grams is None:
        return Response({"error": "لطفاً مقدار گرم را وارد کنید."}, status=400)

    try:
        grams = float(grams)
    except ValueError:
        return Response({"error": "مقدار گرم باید یک عدد باشد."}, status=400)

    # تبدیل گرم به کیلوگرم و تن
    kilograms = grams / 1000
    tons = grams / 1000000

    # برگرداندن نتیجه به عنوان JSON
    return Response({
        "grams": grams,
        "kilograms": kilograms,
        "tons": tons,
    })

@api_view(['GET'])
def hello_world(request):
    return Response({"message": "سلام دنیا! این API با CORS کار می‌کند."})