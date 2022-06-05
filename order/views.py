from django.views.decorators.csrf import csrf_exempt
from drf_spectacular.utils import extend_schema
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from order.models import OrderModel, OrderStatus, OrderItemModel
from order.serializers import OrderSerializer
from product.models import ProductModel, ProductImageModel


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
                total_product = 0
                total_price = 0
                for data in validated_data['data']:
                    product = ProductModel.objects.get(id=int(data['product_id']))
                    total_product += 1
                    total_price += int(data['quantity']) * product.price

                    OrderItemModel.objects.create(
                        order_id=new_order.id,
                        product_id=int(data['product_id']),
                        product_price=float(product.price),
                        quantity=int(data['quantity'])
                    )
                new_order.total_price = total_price
                new_order.total_product = total_product
                new_order.save()

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


class OrderListView(APIView):
    """ View to List all Products """
    permission_classes = (IsAuthenticated,)

    def __init__(self):
        super(OrderListView, self).__init__()
        self.response_data = list()

    @extend_schema(
        operation_id="order",
        tags=["order"]
    )
    def get(self, request, *args, **kwargs):
        """ List all products """
        try:
            orders = OrderModel.objects.filter(user_id=request.user.id)

            for order in orders:
                self.response_data.append({
                    'id': order.id,
                    'description': order.description,
                    'total_product': order.total_product,
                    'total_price': order.total_price,
                    'ordered_date': str(order.created_date)[:10]
                })

            return Response(self.response_data, status=200)
        except Exception as exc:
            print(exc)
            response_data = {
                'success': False,
                'detail': 'Order not created',
            }
            return Response(response_data, status=400)


class OrderDetailView(APIView):
    """ View to List all Products """
    permission_classes = (IsAuthenticated,)

    def __init__(self):
        super(OrderDetailView, self).__init__()
        self.response_data = dict()

    @extend_schema(
        operation_id="order",
        tags=["order"]
    )
    def get(self, request, order_id, *args, **kwargs):
        """ List all products """
        try:
            order = OrderModel.objects.get(id=order_id)
            order_items = OrderItemModel.objects.filter(order_id=order_id)
            items_list = list()
            total_price = 0
            for item in order_items:
                total_price += item.product_price * item.quantity
                images = ProductImageModel.objects.filter(product_id=item.product_id)
                items_list.append({
                    'product_id': item.product_id,
                    'price': item.product_price,
                    'total_price': item.product_price * item.quantity,
                    'quantity': item.quantity,
                    'images': [picture.image.url for picture in images]
                })
            self.response_data = {
                'order_id': order.id,
                'description': order.description,
                'total_products': len(order_items),
                'total_price': total_price,
                'items': items_list
            }

            return Response(self.response_data, status=200)
        except Exception as exc:
            print(exc)
            self.response_data["success"] = False
            self.response_data["detail"] = "Something getting wrong !"
            return Response(self.response_data, status=400)
