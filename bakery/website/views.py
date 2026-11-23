from decimal import Decimal

from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from django.db import transaction

from .models import Category, Product, Order, OrderItem


# Home page
def welcome(request):
    categories = Category.objects.filter(is_active=True)
    products = Product.objects.filter(
        is_available=True
    ).order_by('-id')[:8]

    return render(request, 'welcome.html', {
        'categories': categories,
        'products': products,
    })


# Category products page
def category_detail(request, slug):
    category = get_object_or_404(
        Category,
        slug=slug,
        is_active=True
    )

    products = Product.objects.filter(
        category=category,
        is_available=True
    )

    return render(request, 'category.html', {
        'category': category,
        'products': products,
    })


# Add product to cart
@require_POST
def add_to_cart(request, product_id):
    product = get_object_or_404(
        Product,
        id=product_id,
        is_available=True
    )

    cart = request.session.get('cart', {})
    product_id = str(product.id)

    quantity = int(cart.get(product_id, 0))
    cart[product_id] = quantity + 1

    request.session['cart'] = cart
    request.session.modified = True

    return redirect('cart')


# Cart page
def cart_view(request):
    cart = request.session.get('cart', {})
    cart_items = []
    total = Decimal('0.00')

    for product_id, quantity in cart.items():
        product = Product.objects.filter(
            id=product_id,
            is_available=True
        ).first()

        if product:
            quantity = int(quantity)
            line_total = product.price * quantity

            cart_items.append({
                'product': product,
                'quantity': quantity,
                'line_total': line_total,
            })

            total += line_total

    return render(request, 'cart.html', {
        'cart_items': cart_items,
        'total': total,
    })


# Update product quantity
@require_POST
def update_cart(request, product_id):
    cart = request.session.get('cart', {})

    quantity = int(request.POST.get('quantity', 1))

    if str(product_id) in cart:
        if quantity > 0:
            cart[str(product_id)] = min(quantity, 99)
        else:
            cart.pop(str(product_id))

    request.session['cart'] = cart
    request.session.modified = True

    return redirect('cart')


# Remove product from cart
@require_POST
def remove_from_cart(request, product_id):
    cart = request.session.get('cart', {})

    cart.pop(str(product_id), None)

    request.session['cart'] = cart
    request.session.modified = True

    return redirect('cart')


# Checkout page
def checkout(request):
    cart = request.session.get('cart', {})
    cart_items = []
    total = Decimal('0.00')

    for product_id, quantity in cart.items():
        product = Product.objects.filter(
            id=product_id,
            is_available=True
        ).first()

        if product:
            quantity = int(quantity)
            line_total = product.price * quantity

            cart_items.append({
                'product': product,
                'quantity': quantity,
                'line_total': line_total,
            })

            total += line_total

    if not cart_items:
        return redirect('cart')

    if request.method == 'POST':
        customer_name = request.POST.get(
            'customer_name', ''
        ).strip()

        phone = request.POST.get('phone', '').strip()
        address = request.POST.get('address', '').strip()

        if (
                not customer_name
                or not phone.isdigit()
                or len(phone) != 10
                or not address
        ):
            return render(request, 'checkout.html', {
                'cart_items': cart_items,
                'total': total,
                'error': 'Please enter valid customer details.',
            })

        with transaction.atomic():
            order = Order.objects.create(
                customer_name=customer_name,
                phone=phone,
                address=address,
                total=total,
                status='Pending'
            )

            for item in cart_items:
                OrderItem.objects.create(
                    order=order,
                    product=item['product'],
                    product_name=item['product'].name,
                    quantity=item['quantity'],
                    price=item['product'].price,
                    line_total=item['line_total'],
                )

        request.session['cart'] = {}
        request.session.modified = True

        return redirect('order_success', order_id=order.id)

    return render(request, 'checkout.html', {
        'cart_items': cart_items,
        'total': total,
    })


# Order confirmation page
def order_success(request, order_id):
    order = get_object_or_404(Order, id=order_id)

    return render(request, 'order_success.html', {
        'order': order,
    })
