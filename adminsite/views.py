from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .models import ProductCategory, Product, Profile, Brand
from .forms import ProductCategoryForm, ProductForm, ProfileForm, EditProductCategoryForm, BrandForm
from clientsite.models import RequestForQuotation, RequestForService, Order, OrderItem
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    context = {
        'orders' : Order.objects.order_by('id')[:6],
        'products' : Product.objects.order_by('id')[:6],
        'categories': ProductCategory.objects.order_by('id')[:6],
    }
    return render(request, 'adminsite/index.html', context)
@login_required
def category(request):
    prod_categories = ProductCategory.objects.all()
    context = {
        'prod_categories' : prod_categories
    }
    return render(request, 'adminsite/product-category.html', context)
@login_required
def addcategory(request):
    cat_form = ProductCategoryForm()
    if request.method == 'POST':
        cat_form = ProductCategoryForm(request.POST)
        if cat_form.is_valid:
            cat_form.save()
            messages.success(request, f'form submitted')
            return redirect('productcategory')
        else:
            messages.info(request, f'form not submitted')
    context = {
        'cat_form' : cat_form
    }
    return render(request, 'adminsite/add-category.html', context)
@login_required
def editcategory(request, id):
    category = ProductCategory.objects.get(id = id)
    cate_form = EditProductCategoryForm()
    if request.method == 'POST':
        cate_form = EditProductCategoryForm(request.POST, instance = category)
        if cate_form.is_valid:
            cate_form.save()
            messages.success(request, f'added succefully')
        else:
            messages.error(request, f'unable to add details')
    context = {
        'cate_form' : cate_form,
    }
    
    return render(request, 'adminsite/edit-category.html', context)
@login_required
def category_detail(request, id):
    category = ProductCategory.objects.get(id = id)
    context = {
        'category': category
    }
    return render(request, 'adminsite/category-detail.html', context)

@login_required
def deletecategory(request, id):
    prod_category = ProductCategory.objects.get(id = id)
    
    return redirect('productcategory')

#Brands
@login_required
def brand(request):
    brands = Brand.objects.all()
    context = {
        'brands' : brands
    }
    return render(request, 'adminsite/brands.html', context)

@login_required
def addbrand(request):
    brand_form = BrandForm()
    if request.method == 'POST':
        brand_form = BrandForm(request.POST)
        if brand_form.is_valid:
            brand_form.save()
            messages.success(request, f'form submitted')
            return redirect('brands')
        else:
            messages.info(request, f'form not submitted')
    context = {
        'brand_form' : brand_form
    }
    return render(request, 'adminsite/add-brand.html', context)

@login_required
def editbrand(request, id):
    category = Brand.objects.get(id = id)
    cate_form = EditProductCategoryForm()
    if request.method == 'POST':
        cate_form = EditProductCategoryForm(request.POST, instance = category)
        if cate_form.is_valid:
            cate_form.save()
            messages.success(request, f'added succefully')
        else:
            messages.error(request, f'unable to add details')
    context = {
        'cate_form' : cate_form,
    }
    
    return render(request, 'adminsite/edit-brand.html', context)

@login_required
def brand_detail(request, id):
    brand = Brand.objects.get(id = id)
    context = {
        'brand': brand
    }
    return render(request, 'adminsite/brand-detail.html', context)

@login_required
def deletebrand(request, id):
    prod_category = ProductCategory.objects.get(id = id)
    
    return redirect('brands')


@login_required
#
def products(request):
    context = {
        'products': Product.objects.all()
    }
    return render(request, 'adminsite/products.html', context)

@login_required
def product_detail(request, id):
    # product = Product.objects.get(id = id)
    # context = {
    #     'product': product
    # }
    return render(request, 'adminsite/product-detail.html')

@login_required
def orders(request):
    context = {
        'orders': Order.objects.all()
    }
    return render(request, 'adminsite/orders.html', context)

@login_required
def order_detail(request, id):
    order = Order.objects.get(id = id)
    order_items = order.items.all()
    context = {
        'order' : order,
        'order_items': order_items
    }
    return render(request, 'adminsite/order-detail.html', context)

@login_required
def requestsForServices(request):
    context = {
        'requests_s': RequestForService.objects.all()   
    }
    return render(request, 'adminsite/request-for-services.html', context)

@login_required
def requestsForServicesDetail(request, id):
    requestForService = RequestForService.objects.get(id = id)
    context = {
        'request_for_service' : requestForService
    }
    return render(request, 'adminsite/request-for-services-detail.html', context)

@login_required
def requestsForQuotation(request):
    context = {
        'requests_for_quotation' : RequestForQuotation.objects.all()
    }
    return render(request, 'adminsite/request-for-quotation.html', context)

@login_required
def requestsForQuotationDetail(request, id):
    context = {
        'request_for_quote' : RequestForQuotation.objects.get(id = id)
    }
    return render(request, 'adminsite/request-for-quotation-detail.html', context)

@login_required
def profile(request):
    return render(request, 'adminsite/profile.html')

@login_required
def editprofile(request):
    return render(request, 'adminsite/edit-profile.html')

def product_images(request):
    img_form = ProductForm()
    if request.method == 'POST':
        img_form = ProductForm(request.POST, request.FILES)
        if img_form.is_valid:
            img_form.save()
            messages.success(request, f'form submitted')
            return redirect('products')
        else:
            messages.info(request, f'form not submitted')
    context = {
        'img_form' : img_form
    }
    return render(request, 'adminsite/addimages.html', context)
@login_required
def logoutpage(request):
    logout(request)
    return redirect('login')