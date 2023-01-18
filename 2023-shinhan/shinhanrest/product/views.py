from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Product

class ProductListView(APIView):
    def post(self,request,*args,**kwargs):
        print(request.data)

        product = Product (
        
            name=request.data.get('name'),
            price=request.data.get('price'),
            product_type=request.data.get('product_type'),
        )
        # print(product.id) # 에러!
        product.save() #primary key 가 이때 만들어짐!
        return Response({
                    'id': product.id,
                    'name': product.name,
                    'price': product.price,
                    'product_type': product.product_type,
                
        },status=status.HTTP_201_CREATED)

    def get(self,request,*args,**kwargs):

        result=[]
        products = Product.objects.all()
        if 'price' in request.query_params:
            price = request.query_params['price']
            products = products.filter(price__lte=price)


        if 'name' in request.query_params:
            name = request.query_params['name']
            products = products.filter(name__contains=name)
            print("PPP",products)
        products = products.order_by('id')

        for product in products:
            print(product)
            ret = {
                    'id': product.id,
                    'name': product.name,
                    'price': product.price,
                    'product_type': product.product_type,
                
            }
            result.append(ret)
        return Response(result)



class ProductDetailView(APIView):
    def get(self,request,pk,*args,**kwargs):
        try:
            product = Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        ret = {
                'name': product.name,
                'price': product.price,
                'product_type': product.product_type,
            
        }
        return Response(ret)

    def delete(self,request,pk,*args,**kwargs):
        if Product.objects.filter(pk=pk).exists():
            product = Product.objects.get(pk=pk)
            product.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self,request,pk,*args,**kwargs):

        try:
            product = Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        # if request.data.get('name'):
        #     product.name=request.data.get('name')
        # if request.data.get('price'):
        #     product.price=request.data.get('price')
        # if request.data.get('product_type'):
        #     product.product_type=request.data.get('product_type')
        dirty = False
        for field,value in request.data.items():
            if field not in [f.name for f in product._meta.get_fields()]:
                continue
            dirty = dirty | (value != getattr(product,field))
            setattr(product,field,value)
        if dirty:
            product.save()
        return Response("OK")