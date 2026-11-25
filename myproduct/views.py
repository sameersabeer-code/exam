from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from myproduct.models import Product
from myproduct.serializers import ProductSerializer

# Create your views here.
class ProductListCreateview(APIView):
    def get(self,request):
        products=Product.objects.all()
        serializer=ProductSerializer(products,many=True)
        return Response(serializer.data)
    def post(self,request):
        serializer=ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


class ProducRetriveupdateDelite(APIView):
    def get(self,request,pk):
        product=Product.objects.get(id=pk)
        serilaizer=ProductSerializer(product)
        return Response(serilaizer.data)
    def put(self,request,pk):
        product=Product.objects.get(id=pk)
        serializer=ProductSerializer(product,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
    def delete(self,request,pk):
        product=Product.objects.get(id=pk)
        product.delete()
        return Response({"message":"product deleted successfully"})
    