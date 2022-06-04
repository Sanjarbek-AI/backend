from drf_spectacular.utils import extend_schema
from rest_framework.generics import ListAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from product.models import ProductModel


class ProductListView(ListAPIView):
    """ View to List all Products """
    permission_classes = [AllowAny, ]
    authentication_classes = []

    @extend_schema(
        operation_id="product",
        tags=["product"]
    )
    def __init__(self):
        super(ProductListView, self).__init__()
        self.response_data = dict()

    def get(self, request, *args, **kwargs):
        """ List all products """
        try:
            products = ProductModel.objects.all()
            self.response_data["success"] = True
            self.response_data["products"] = list()
            for product in products:
                self.response_data["products"].append({
                    'id': product.id,
                    'title': product.title,
                    'description': product.description,
                    'price': product.price,
                    'status': product.status,
                    'people_type': product.people_type,
                    'sizes': [size.title for size in product.sizes.all()],
                    'colors': [color.title for color in product.colors.all()],
                    'categories': [category.title for category in product.categories.all()],
                    'pictures': [picture.image.url for picture in product.images.all()]
                })

            return Response(self.response_data, status=200)
        except Exception as exc:
            print(exc)
            self.response_data["success"] = False
            self.response_data["detail"] = "Something getting wrong !"
            return Response(self.response_data, status=400)
