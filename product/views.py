from drf_spectacular.utils import extend_schema
from rest_framework.generics import ListAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from product.models import CategoryModel, ProductModel, StoreModel


class ProductListView(ListAPIView):
    """ View to List all Products """
    permission_classes = [AllowAny, ]
    authentication_classes = []

    def __init__(self):
        super(ProductListView, self).__init__()
        self.response_data = dict()

    @extend_schema(
        operation_id="product",
        tags=["product"]
    )
    def get(self, request, *args, **kwargs):
        """ List all products """
        try:
            self.response_data['products'] = list()
            products = ProductModel.objects.all()
            for product in products:
                self.response_data['products'].append({
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
            response_data = {
                "success": False,
                "detail": "Something getting wrong !"
            }
            return Response(response_data, status=400)


class ProductByBrand(APIView):
    """ View to List all Products """
    permission_classes = (AllowAny,)

    def __init__(self):
        super(ProductByBrand, self).__init__()
        self.response_data = dict()

    @extend_schema(
        operation_id="product",
        tags=["product"]
    )
    def get(self, request, brand_id, *args, **kwargs):
        """ List all products """
        try:
            self.response_data['products'] = list()
            products = ProductModel.objects.filter(store_id=brand_id)

            for product in products:
                self.response_data['products'].append({
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
            response_data = {
                "success": False,
                "detail": "Something getting wrong !"
            }
            return Response(response_data, status=400)


class ProductByCategory(APIView):
    """ View to List all Products """
    permission_classes = (AllowAny,)

    def __init__(self):
        super(ProductByCategory, self).__init__()
        self.response_data = dict()

    @extend_schema(
        operation_id="product",
        tags=["product"]
    )
    def get(self, request, category_id, *args, **kwargs):
        """ List all products """
        try:
            self.response_data['products'] = list()
            products = ProductModel.objects.filter(categories=category_id)

            for product in products:
                self.response_data['products'].append({
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
            response_data = {
                "success": False,
                "detail": "Something getting wrong !"
            }
            return Response(response_data, status=400)


class CategoryListView(APIView):
    """ View to List all Products """
    permission_classes = [AllowAny, ]
    authentication_classes = []

    def __init__(self):
        super(CategoryListView, self).__init__()
        self.response_data = dict()

    @extend_schema(
        operation_id="category",
        tags=["category"]
    )
    def get(self, request, *args, **kwargs):
        """ List all products """
        try:
            data = self.request.query_params
            gender = data.get("type")
            categories = CategoryModel.objects.filter(gender=gender)
            self.response_data['categories'] = list()
            for category in categories:
                self.response_data['categories'].append({
                    'id': category.id,
                    'title': category.title,
                    'image': category.image.url,
                    'gender': category.gender
                })

            return Response(self.response_data, status=200)
        except Exception as exc:
            print(exc)
            response_data = {
                "success": False,
                "detail": "Something getting wrong !"
            }
            return Response(response_data, status=400)


class BrandListView(APIView):
    """ View to List all Products """
    permission_classes = [AllowAny, ]
    authentication_classes = []

    def __init__(self):
        super(BrandListView, self).__init__()
        self.response_data = dict()

    @extend_schema(
        operation_id="brand",
        tags=["brand"]
    )
    def get(self, request, *args, **kwargs):
        """ List all products """
        try:
            data = self.request.query_params
            gender = data.get("type")
            brands = StoreModel.objects.filter(gender=gender)
            self.response_data['brands'] = list()
            for brand in brands:
                self.response_data['brands'].append({
                    'id': brand.id,
                    'name': brand.name,
                    'logo': brand.logo.url,
                    'gender': brand.gender
                })

            return Response(self.response_data, status=200)
        except Exception as exc:
            print(exc)
            response_data = {
                "success": False,
                "detail": "Something getting wrong !"
            }
            return Response(response_data, status=400)


class ProductSearchView(APIView):
    """ View to List all Products """
    permission_classes = [AllowAny, ]
    authentication_classes = []

    def __init__(self):
        super(ProductSearchView, self).__init__()
        self.response_data = dict()

    @extend_schema(
        operation_id="product",
        tags=["product"]
    )
    def get(self, request, *args, **kwargs):
        """ List all products """
        try:
            data = self.request.query_params
            title = data.get("q")
            products = ProductModel.objects.filter(title__icontains=title)
            self.response_data['products'] = list()
            for product in products:
                self.response_data['products'].append({
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
            response_data = {
                "success": False,
                "detail": "Something getting wrong !"
            }
            return Response(response_data, status=400)


class BrandsListWithView(APIView):
    """ View to List all Products """
    permission_classes = [AllowAny, ]
    authentication_classes = []

    def __init__(self):
        super(BrandsListWithView, self).__init__()
        self.response_data = dict()

    @extend_schema(
        operation_id="brands",
        tags=["brands"]
    )
    def get(self, request, *args, **kwargs):
        """ List all products """
        try:
            brands = StoreModel.objects.all()
            self.response_data['brands'] = list()
            for brand in brands:
                self.response_data['brands'].append({
                    'id': brand.id,
                    'name': brand.name,
                    # 'logo': brand.logo.url,
                    'gender': brand.gender,
                    'location': brand.location,
                    'location_link': brand.location_link,
                    'description': brand.description,
                })

            return Response(self.response_data, status=200)
        except Exception as exc:
            print(exc)
            response_data = {
                "success": False,
                "detail": "Something getting wrong !"
            }
            return Response(response_data, status=400)
