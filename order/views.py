from django.views.decorators.csrf import csrf_exempt
from drf_spectacular.utils import extend_schema
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from order.models import OrderModel, OrderStatus, OrderItemModel
from order.serializers import OrderSerializer
from product.models import ProductModel


class OrderView(APIView):
    """View for creating an Order API"""
    permission_classes = (IsAuthenticated,)
    serializer_class = OrderSerializer

    @extend_schema(
        operation_id="order",
        tags=["order"]
    )
    @csrf_exempt
    def post(self, request, *args, **kwargs):
        serializer = OrderSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        validated_data = serializer.validated_data
        # try:
        try:
            if validated_data:
                new_order = OrderModel(
                    user_id=int(request.user.id),
                    description=validated_data['description'],
                    total_price=0,
                    total_product=0,
                    status=OrderStatus.ACCEPTED
                )
                new_order.save()
                for data in validated_data['data']:
                    product = ProductModel.objects.get(id=int(data['product_id']))

                    OrderItemModel.objects.create(
                        order_id=new_order.id,
                        product_id=int(data['product_id']),
                        product_price=float(product.price),
                        quantity=int(data['quantity'])
                    )

            response_data = {
                'success': True,
                'detail': 'Order successfully created',
            }
            return Response(response_data, status=201)

        except Exception as exc:
            print(exc)
            response_data = {
                'success': False,
                'detail': 'Order not created',
            }
        return Response(response_data, status=406)


class OrderListView(ListAPIView):
    """ View to List all Products """
    permission_classes = (IsAuthenticated,)

    @extend_schema(
        operation_id="order",
        tags=["order"]
    )
    def __init__(self):
        super(OrderListView, self).__init__()
        self.response_data = dict()

    def get(self, request, *args, **kwargs):
        """ List all products """
        try:
            orders = OrderModel.objects.filter(user_id=request.user.id)
            self.response_data["success"] = True
            self.response_data["orders"] = list()
            for order in orders:
                items = OrderItemModel.objects.filter(order_id=order.id)
                self.response_data["orders"].append({
                    'id': order.id,
                    'description': order.description,
                    'total_product': len(items)
                })

            return Response(self.response_data, status=200)
        except Exception as exc:
            print(exc)
            self.response_data["success"] = False
            self.response_data["detail"] = "Something getting wrong !"
            return Response(self.response_data, status=400)
