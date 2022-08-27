from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import generics,status
from django.shortcuts import get_object_or_404
from authentication.models import User
from .models import Order
from .serializers import OrderSerializer ,UpdateOrderSerializer
from django.contrib.auth import get_user_model
from rest_framework.decorators import api_view 
from rest_framework.parsers import MultiPartParser, FormParser
# Create your views here.

User = get_user_model()

def hellonew(request):
    return Response(data={"title":"Hello!"})


class OrderCreateListView(generics.GenericAPIView):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()


    def get(self, request, *args, **kwargs):
        orders = Order.objects.all()
        serializer = self.serializer_class(instance=orders, many=True)

        return Response(data=serializer.data)

    def post(self, request, *args, **kwargs):
        data = request.data
        user = request.user

        serializer = self.serializer_class(instance=data, many=True)
        if serializer.is_valid():
            serializer.save(customer=user)
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        return Response(data=serializer.data, status=status.HTTP_401_UNAUTHORIZED)  

    def get_parsers(self):
        if getattr(self, 'swagger_fake_view', False):
            return []
        return super().get_parsers()  


class OrderDetailView(generics.GenericAPIView):
    serializer_class = OrderSerializer  

    def get(self, request, order_id):

        order = Order.objects.get(pk=order_id)

        serializer = self.serializer_class(instance=order, many=True)

        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def put(self,request, order_id):
        data = request.data
        user = request.user

        serializers = self.serializer_class(instance=OrderSerializer, many=True)
        if serializers.is_valid():
            serializers.save(customer=user)
            return Response(data=serializers.data, status=status.HTTP_200_OK)
        return Response(data=data, status=status.HTTP_401_UNAUTHORIZED)

    def delete(self,request, order_id):
         order = Order.objects.get(Order, pk=order_id)

         order.delete()

         return Response(status=status.HTTP_200_OK)

    def get_parsers(self):
        if getattr(self, 'swagger_fake_view', False):
            return []
        return super().get_parsers()  

class UpdateOrderStatus(generics.GenericAPIView):

    serializer_class = UpdateOrderSerializer
    def put(self, request, order_id):
        order = Order.objects.get(Order, pk=order_id)

        data = request.data
        user = request.user

        serializer = self.serializer_class(instance=order, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)

        return Response(data=serializer.data , status=status.HTTP_201_CREATED) 

    def get_parsers(self):
        if getattr(self, 'swagger_fake_view', False):
            return []
        return super().get_parsers()    


class UserOrderView(generics.GenericAPIView):
    serializer_class = OrderSerializer

    def get(self, request, user_id):
        user = User.objects.get(pk=user_id)
        order = Order.objects.all.filter(customer=user)
        serializer = self.serializer_class(instance=order, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def get_parsers(self):
        if getattr(self, 'swagger_fake_view', False):
            return []
        return super().get_parsers()      

class UserOrderDetail(generics.GenericAPIView):

    serializer_class = OrderSerializer

    def get(self, request, user_id, order_id):
        user = User.objects.get(pk=user_id)
        order = Order.objects.all.filter(customer=user).get(pk=order_id)

        serializer = self.serializer_class(instance=order)
        data = serializer.data
        return Response(data, status=status.HTTP_200_OK)

    def get_parsers(self):
        if getattr(self, 'swagger_fake_view', False):
            return []
        return super().get_parsers()  