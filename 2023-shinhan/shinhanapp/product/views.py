from django.shortcuts import render, redirect
from django.http.response import JsonResponse
from .models import Product

# Create your views here.

def main(request):
    products = Product.objects.all().order_by('-id')
    return render(request, 'product.html', { 'products': products })

def write(request):
    if not request.user.is_authenticated:
        return redirect('/member/login/')

    if request.method == 'POST':
        product = Product(
            user=request.user,
            title=request.POST.get("title"),
            content=request.POST.get("content"),
            price=request.POST.get("price"),
            location=request.POST.get("location"),
            image=request.FILES.get('image')
        )
        # print(product.id) # 에러!
        product.save()
        return redirect('/')

    return render(request, 'product_write.html')

def detail(request, pk):

    product = Product.objects.get(pk=pk)
    ret = {
        'username': product.user.username,
        'title': product.title,
        'content': product.content,
        'price': product.price,
        'location': product.location,
        'image': '/static/bg.jpg',
    }
    if product.image:
        ret['image'] = product.image.url

    return JsonResponse(ret)