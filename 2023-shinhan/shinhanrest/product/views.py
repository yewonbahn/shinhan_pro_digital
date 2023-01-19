from rest_framework import mixins, generics
from .models import Product,Comment
from .serializers import ProductSerializer,CommentSerializer
from .paginations import ProductLargePagination

class ProductListView(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    generics.GenericAPIView
):

    serializer_class = ProductSerializer
    pagination_class = ProductLargePagination
    def get_queryset(self):
        if self.request.user.is_authenticated:
            products = Product.objects.all()

            
        name = self.request.query_params.get('name')
        price = self.request.query_params.get('price')
        if name:
            products = products.filter(name__contains=name)
        if price:
            products = products.filter(price__lte=price)
        return products.order_by('-id')

    def get(self,request,*args,**kwargs):
        print(request.user)
        return self.list(request,args,kwargs)
    def post(self,request,*args,**kwargs):
        return self.create(request,args,kwargs)

class ProductDetailView(
    mixins.DestroyModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    generics.GenericAPIView,
):
    serializer_class=ProductSerializer

    def get_queryset(self):
        return Product.objects.all().order_by('id')

    def get(self,request,*args,**kwargs):
        return self.retrieve(request,args,kwargs)

    def delete(self,request,*args,**kwargs):
        return self.destroy(request,args,kwargs)

    def put(self,request,*args,**kwargs):
        return self.partial_update(request,args,kwargs)

class CommentListView(
    mixins.ListModelMixin,
    generics.GenericAPIView
):
    serializer_class = CommentSerializer
    def get_queryset(self):
        comments = Comment.objects.all()
        return comments.order_by('-id')
    def get(self,request,*args,**kwargs):
        return self.list(request,args,kwargs)


class CommentDetailView(
    mixins.DestroyModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    generics.GenericAPIView,
):
    serializer_class=CommentSerializer

    def get_queryset(self):
        product_id=self.kwargs.get('product_id')
        if product_id:
            return Comment.objects.filter(product_id=product_id).order_by('-id')
        return Comment.objects.none()

    def get(self,request,*args,**kwargs):
        return self.retrieve(request,args,kwargs)