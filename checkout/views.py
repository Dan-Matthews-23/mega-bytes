
from django.shortcuts import render, redirect, reverse, get_object_or_404, HttpResponse
from django.http import JsonResponse, HttpResponseBadRequest
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.db.models import Prefetch
from django.contrib import messages
from django.conf import settings
from django import forms
import stripe
import json
import uuid
import logging
from basket.models import Basket
from checkout.models import OrderLineItem, Orders
from products.models import Products
from accounts.models import UserProfile
from .forms import BasketForm



logger = logging.getLogger(__name__)  # Set up basic logging


@login_required(login_url=settings.LOGIN_URL)
def render_basket_form(request):
    try:
        if request.user.is_authenticated:
            profile = request.user.userprofile  # Access connected UserProfile
            form = BasketForm(instance=profile)  # Pre-populate the form
            print("User is authenticated")
        else:
            form = BasketForm()
            print("User is NOT authenticated")
            #orders = profile.orders.all()
    except Exception as e:  # Add appropriate exception handling
        logger.error(f"Error processing order: {e}")
        # Handle errors gracefully, e.g., redirect with error message
    
    
    template = 'checkout/checkout.html'
    context = {
                        'form': form,
                        #'basket': basket_session,         
                    }
                   
    return render(request, template, context)
















def process_checkout(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY
    if request.method == 'POST':

        # Attempt to get posted form data. If failed, redirect to previous page
       
        form_data = {
            'full_name': request.POST['full_name'],
            'email': request.POST['email'],
            'phone_number': request.POST['phone_number'],            
            'postcode': request.POST['postcode'],
            'town_or_city': request.POST['town_or_city'],
            'street_address1': request.POST['street_address1'],
            'street_address2': request.POST['street_address2'],
            'county': request.POST['county'],                        
            }
        print(form_data)
        
        
        #Attempt to get Order Data
        get_order_data = request.session.get('order_items')
        if get_order_data:  # Check if order items exist
            order_data = []  # Create a list to hold individual order items
            for product_id, product_details in get_order_data.items():
                #print(f"The product_id is {product_id}")
                get_product = Products.objects.get(product_id=product_id)
                order_item = {
                        'product_id': int(product_id),  # Use the iterated product_id
                        'product_quantity': int(product_details['quantity']),
                        'price': float(product_details['cost']),
                        'product_name':  get_product.product_name,            
                    }
                order_data.append(order_item)              
            logger.debug(f"Received order_data: {order_data}")            
           
            if order_data is None or len(order_data) == 0:
                logger.debug(f"Received order_data: {order_data}")
                messages.error(request, "Your basket is empty.")
                logger.info("Empty order data detected")                   
                return redirect('prepacked_sandwiches')              
            else:
                order_number =  uuid.uuid4().hex.upper()
                for order in order_data:
                    order['order_number'] = order_number  # Same number for all                                                         
                request.session['basket'] = order_data
                basket_session = request.session['basket']
                    
        
        
        # Attempt to get Basket Items
        
        basket = request.session.get('basket', {})         
                
        
        # Attempt to get Stripe infomation
        profile = get_object_or_404(UserProfile, user=request.user)
        form = BasketForm(request.POST, instance=profile)
        stripe_id = request.POST.get('client_secret').split('_secret')[0]
        form.stripe_stripe_id = stripe_id
        
        
        # Attempt to create an order
        order_number=""
        total = 0.00
        order_total = 0 
        order = Orders(
                user_profile=profile, 
                full_name=form_data['full_name'],
                email=form_data['email'],
                phone_number = form_data['phone_number'],
                postcode = form_data['postcode'],
                town_or_city = form_data['town_or_city'],
                street_address1 = form_data['street_address1'],
                street_address2 = form_data['street_address2'],
                county = form_data['county'],
                stripe_id =  stripe_id, 
            )            
        order.save()
        request.session['order_number'] = order.order_number
        order_number = request.session['order_number']     
        
        for item in basket:
            product = Products.objects.get(product_id=item['product_id'])
            line_item_total = float(product.product_price) * int(item['product_quantity'])
            order_total += line_item_total                        
            order_line_item = OrderLineItem(
                            order=order,
                            product=product,
                            quantity=item['product_quantity'],
                            order_total=line_item_total 
                        )
            order_line_item.save()
            order.order_total = order_total                        
            order.save()
        total = sum(float(item['price']) for item in basket)
        stripe_total = round(total * 100)
        stripe.api_key = stripe_secret_key
        
        
        # Attempt to assign final Stripe variables
        intent = stripe.PaymentIntent.create(
                        amount=stripe_total,
                        currency=settings.STRIPE_CURRENCY,
                    )
        template = 'checkout/order_confirmed.html'
        context = {
        #'order_form': order_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
        }
        return render(request, template, context)
    else:
        template = 'checkout/checkout.html'
        context = {
        #'order_form': order_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
        }
        return render(request, template, context)
                   

                



        
        
        

            
                
        
        
        
               
        
        #if not form.is_valid():
            #messages.error(request, ('There was an error with your form. '
                                    
        #else:            
            #form.save()     
            
           
                        
            
                        
                
            
            
            
            
            
            
         
            
            
            
         
            
        
        
  

    

    























def checkout_success(request):
    """
    Handle successful checkouts
    """
    request.session.get('save_info')
    order_number = request.session['order_number']
    form = get_object_or_404(Orders, order_number=order_number)

    if request.user.is_authenticated:
        profile = UserProfile.objects.get(user=request.user)
        # Attach the user's profile to the form
        form.user_profile = profile
        form.save()

        # Save the user's info
        if save_info:
            profile_data = {
                'default_phone_number': form.phone_number,
                'default_country': form.country,
                'default_postcode': form.postcode,
                'default_town_or_city': form.town_or_city,
                'default_street_address1': form.street_address1,
                'default_street_address2': form.street_address2,
                'default_county': form.county,
            }
            user_profile_form = UserProfileForm(profile_data, instance=profile)
            if user_profile_form.is_valid():
                user_profile_form.save()

    messages.success(request, f'Order successfully processed! \
        Your form number is {order_number}. A confirmation \
        email will be sent to {form.email}.')
    del request.session['order_items']
    del request.session['basket']

    #if 'basket' in request.session:
        #del request.session['basket']

    template = 'checkout/order_confirmed.html'
    context = {
        'form': form,
    }

    return render(request, template, context)





@require_POST
def cache_checkout_data(request):
    try:
        secret_id = request.POST.get('client_secret').split('_secret')[0]
        stripe.api_key = settings.STRIPE_SECRET_KEY
        
        stripe.PaymentIntent.modify(
            secret_id, metadata={            
            'save_info': request.POST.get('save_info'),
            'username': request.user,
        })
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(request, 'There was an error while processing your payment. Please try again in a few minutes.')
        return HttpResponse(content=e, status=400)