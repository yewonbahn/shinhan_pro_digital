from rest_framework import mixins, generics
from .models import Product
from .serializers import ProductSerializer

class ProductListView(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    generics.GenericAPIView
):

    serializer_class = ProductSerializer
    def get_queryset(self):
        products = Product.objects.all()
        name = self.request.query_params.get('name')
        price = self.request.query_params.get('name')
        if name:
            products = products.filter(name__contains=name)
        if price:
            products = products.filter(price__lte=price)
        return products.order_by('-id')

    def get(self,request,*args,**kwargs):
        return self.list(request,args,kwargs)
    def post(self,request,*args,**kwargs):
        return self.create(request,args,kwargs)