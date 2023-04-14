from django.shortcuts import get_object_or_404, redirect, render
from adminsite.models import Product, ProductCategory, Brand
from .models import Order, OrderItem, CartItem
from django.contrib.auth import authenticate, login, logout
from .forms import RegisterForm, CartAddProductForm
from django.contrib.auth.models import User
from django.contrib import messages
# Create your views here.

def index(request):
    products = Product.objects.all()
    context = {
        'products': products
    }
    return render(request, 'clientsite/index.html', context)

def blog(request):
    return render(request, 'clientsite/blog.html')

def contact_us(request):
    return render(request, 'clientsite/contact-us.html')

def about_us(request):
    return render(request, 'clientsite/about-us.html')

def shop(request):
    products = Product.objects.all()
    product_categories = ProductCategory.objects.all()
    brands = Brand.objects.all()
    context = {
        'products' : products,
        'product_categories' : product_categories,
        'brands' : brands
    }
    print(product_categories)
    return render(request, 'clientsite/shop.html', context)

def product_category(request, category_name):
    products = Product.objects.get(category_name = category_name)
    context = {
        'products' : products
    }
    return render(request, 'clientsite/product-category.html', context)

def product_brands(request, brand_name):
    products = Product.objects.get(brand_name = brand_name)
    context = {
        'products' : products
    }
    return render(request, 'clientsite/product-category.html', context)

def product_detail(request, id):
    product = Product.objects.get(id = id)
    context = {
        'product' : product
    }
    return render(request, 'clientsite/product-detail.html', context)

def refund_return(request):
    return render(request, 'clientsite/refund_return.html')

def wishlist(request):
    return render(request, 'clientsite/wishlist.html')

def request_for_service(request):
    return render(request, 'clientsite/request-for-service.html')

def request_for_quotation(request):
    return render(request, 'clientsite/request-for-quotation.html')

# blogs
def simplest_ways(request):
    return render(request, 'clientsite/blog/simple-ways-to-stay-safe-online.html')

def influence_of_typewriters(request):
    return render(request, 'clientsite/blog/the-influence-of-typewriters.html')

def basic_it_skills(request):
    return render(request, 'clientsite/blog/basic-it-skills.html')

def why_konica_minolta(request):
    return render(request, 'clientsite/blog/why-konica-minolta.html')

def discover_6_ways(request):
    return render(request, 'clientsite/blog/discover-6-ways.html')

def reasons_to_choose_ricoh(request):
    return render(request, 'clientsite/blog/reasons-to-choose-ricoh.html')

def january_blues_2022(request):
    return render(request, 'clientsite/blog/january-blues-2022.html')

def easy_work_from_home(request):
    return render(request, 'clientsite/blog/easy-work-from-home.html')

def must_have_equipment(request):
    return render(request, 'clientsite/blog/must-have-equipment.html')

def opportunities_in_printing(request):
    return render(request, 'clientsite/blog/opportunities-in-printing.html')



#Cart
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart_item, created = CartItem.objects.get_or_create(
        # user=request.user,
        product=product
    )
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    return redirect('cart')

def cart(request):
    cart_items = CartItem.objects.all()
    # total_cost = sum(item.product.price * item.quantity for item in cart_items)
    total_cost = 0
    for item in cart_items:
        item.subtotal = item.product.price * item.quantity
        total_cost += item.subtotal
    context = {
        'cart_items': cart_items,
        'total_cost' : total_cost
    }
    return render(request, 'clientsite/cart/cart.html', context)

def cart_remove(request, cart_item_id):
    cart = CartItem.objects.get(id = cart_item_id)
    cart.delete()
    return redirect('cart')

def cart_update(request, cart_item_id, quantity):
    cart_item = CartItem.objects.get(id=cart_item_id)
    if cart_item:
        cart_item.quantity = quantity
        cart_item.save()
    return redirect('cart')

def order_detail(request):
    cart_items = CartItem.objects.all()
    # total_cost = sum(item.product.price * item.quantity for item in cart_items)
    total_cost = 0
    for item in cart_items:
        item.subtotal = item.product.price * item.quantity
        total_cost += item.subtotal
    context = {
        'cart_items': cart_items,
        'total_cost' : total_cost
    }
    return render(request, 'clientsite/cart/checkout.html', context)

def checkout(request):
    cart_items = CartItem.objects.all()
    total_cost = 0
    
    first_name = request.POST.get('first_name')
    last_name = request.POST.get('last_name')
    location = request.POST.get('location')
    phone = request.POST.get('phone')
    email = request.POST.get('email')
    additional_information = request.POST.get('additional_information')
    
    order = Order.objects.create(
        first_name = first_name,
        last_name = last_name,
        location = location,
        phone = phone ,
        email = email,
        additional_information = additional_information
    )
    for item in cart_items:
        item.subtotal = item.product.price * item.quantity
        total_cost += item.subtotal
        order_item = OrderItem.objects.create(
            order=order,
            product=item.product,
            quantity=item.quantity,
            subtotal=item.subtotal,
        )
    order.total_cost = total_cost
    order.save()
    cart_items.delete()
    #redirect to the checkout page
    return redirect('index')


def registerpage(request):
    if request.method == 'POST':    
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        
        user = User.objects.create_user(
            username = username,
            email = email,
            password = password, 
        )
        user = authenticate(request, username=username, email=email, password=password)
        login(request, user)
        redirect('admin-dashboard')
    else:
        return render(request, 'clientsite/register.html')

def loginpage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username = username, password = password)
        if user is not None:
            login(request, user)
            messages.success(request, f'login successful')
            return redirect('admin-dashboard')
        else: 
            messages.error(request, f'login unsuccessful')

    return render(request, 'clientsite/login.html')