from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, DetailView
from django.http import JsonResponse
from .models import Products, Rating, GeneralMerchandise, FoodBeverage, Products, Orders, OrderItem, Payment, Delivery, User, Admin, Customer
from .forms import ProductForm, SignInForm, SignUpForm
import openai
import json
import datetime
from django.db import transaction
from django.utils.timezone import now
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.utils.timezone import now


# Configure your OpenAI API key
#openai.api_key = ''         

# Product List View (Class-Based)
class ProductListView(ListView):
    model = Products
    template_name = 'HomePage.html'
    context_object_name = 'products'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Add distinct brands to the context
        context['brands'] = self.model.objects.values_list('brand', flat=True).distinct()

        return context
    
    def get_queryset(self):
        queryset = super().get_queryset()
        # Get filter values from GET parameters
        category = self.request.GET.get('category', '')
        brand = self.request.GET.get('brand', '')
        rating = self.request.GET.get('rating', '')
        price_range = self.request.GET.get('price', '')
        keyword = self.request.GET.get('keyword', '')
        popular_item = self.request.GET.get('popular_item', '')

        # Map category values to match database fields
        category_mapping = {
            "General Merchandise": "GENERAL_MERCHANDISE",
            "Food Beverage": "FOOD_BEVERAGE",
        }

        # Apply filters to the queryset
        if category:
            db_category = category_mapping.get(category)
            if db_category:
                queryset = queryset.filter(category=db_category)

        if brand:
            queryset = queryset.filter(brand__icontains=brand)
        if rating:
            queryset = queryset.filter(rating__rate_score=rating)
        if price_range:
            min_price, max_price = map(int, price_range.split('-'))
            queryset = queryset.filter(price__gte=min_price, price__lte=max_price)
        if keyword:
            queryset = queryset.filter(
                Q(proname__icontains=keyword) | Q(prodescription__icontains=keyword)
            )
        if popular_item == "1":  # Popular Items only
            queryset = queryset.filter(popular_items=True)
        elif popular_item == "0":  # Non-popular Items only
            queryset = queryset.filter(popular_items=False)

        # Check if the request is an AJAX request
        if self.request.headers.get('x-requested-with') == 'XMLHttpRequest':
            # Serialize the filtered queryset into JSON
            products = list(
                queryset.values('product_id', 'proname', 'price', 'image', 'category', 'brand')
            )
            return JsonResponse({'products': products}, safe=False)
    
        return queryset

def get_star_range(rating_score):
    return range(1, rating_score + 1)

# Product Detail View (Class-Based)
class ProductDetailView(DetailView):
    model = Products
    template_name = 'ProductDetail.html'
    context_object_name = 'product'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        product_ratings = Rating.objects.filter(product=self.object)
        # Add pre-calculated star ranges to ratings
        ratings_with_stars = [
            {
                "comments": rating.comments,
                "rate_score": rating.rate_score,
                "stars": range(1, rating.rate_score + 1),
            }
            for rating in product_ratings
        ]

        context['product_ratings'] = ratings_with_stars

        # Dynamically set the quantity range based on quantity_available
        max_purchase_limit = 20  # Maximum limit for purchase
        quantity_available = self.object.quantity_available or 0  # Fallback to 0 if None
        context['quantity_range'] = range(1, min(max_purchase_limit, quantity_available) + 1)

        context['brands'] = self.model.objects.values_list('brand', flat=True).distinct()


        return context
    
    def get_queryset(self):
        queryset = super().get_queryset()
        # Get filter values from GET parameters
        category = self.request.GET.get('category', '')
        brand = self.request.GET.get('brand', '')
        rating = self.request.GET.get('rating', '')
        price_range = self.request.GET.get('price', '')
        keyword = self.request.GET.get('keyword', '')
        popular_item = self.request.GET.get('popular_item', '')

        # Map category values to match database fields
        category_mapping = {
            "General Merchandise": "GENERAL_MERCHANDISE",
            "Food Beverage": "FOOD_BEVERAGE",
        }

        # Apply filters to the queryset
        if category:
            db_category = category_mapping.get(category)
            if db_category:
                queryset = queryset.filter(category=db_category)

        if brand:
            queryset = queryset.filter(brand__icontains=brand)
        if rating:
            queryset = queryset.filter(rating__rate_score=rating)
        if price_range:
            try:
                min_price, max_price = map(int, price_range.split('-'))
                queryset = queryset.filter(price__gte=min_price, price__lte=max_price)
            except ValueError:
                pass  # Ignore invalid price range inputs
        if keyword:
            queryset = queryset.filter(
                Q(proname__icontains=keyword) | Q(prodescription__icontains=keyword)
            )
        if popular_item == "1":  # Popular Items only
            queryset = queryset.filter(popular_items=True)
        elif popular_item == "0":  # Non-popular Items only
            queryset = queryset.filter(popular_items=False)

        return queryset

    def render_to_response(self, context, **response_kwargs):
        # Handle AJAX requests and return JSON response
        if self.request.headers.get('x-requested-with') == 'XMLHttpRequest':
            products = list(self.get_queryset().values(
                'product_id', 'proname', 'price', 'image', 'brand', 'category'
            ))
            return JsonResponse({'products': products}, safe=False)
        return super().render_to_response(context, **response_kwargs)

# Product Create View
def Product_Create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            # Save the product to the database
            proname = form.cleaned_data['proname']
            brand = form.cleaned_data['brand']
            cost = form.cleaned_data['cost']
            price = form.cleaned_data['price']
            prodescription = form.cleaned_data['prodescription']
            category = form.cleaned_data['category']
            image = form.cleaned_data['image']
            quantity_available = form.cleaned_data['quantity_available']

            # Create the base product
            product = Products.objects.create(
                proname=proname,
                brand=brand,
                cost=cost,
                price=price,
                prodescription=prodescription,
                category=category,
                image=image,
                quantity_available=quantity_available,
            )

            # Save additional fields based on category
            if category == "GENERAL_MERCHANDISE":
                color = form.cleaned_data['color']
                GeneralMerchandise.objects.create(product=product, color=color)
            elif category == "FOOD_BEVERAGE":
                sell_by = form.cleaned_data['sell_by']
                FoodBeverage.objects.create(product=product, sell_by=sell_by)

            return redirect('product_list')
    else:
        form = ProductForm()

    return render(request, 'ProductCreate.html', {'form': form})

# Updated Product Delete View
def Product_Delete(request, product_id):
    if request.method == 'POST':
        # Get the product
        product = get_object_or_404(Products, pk=product_id)

        # Determine product category and delete from the respective table
        if product.category == 'food_beverage':
            FoodBeverage.objects.filter(product=product).delete()
        elif product.category == 'general_merchandise':
            GeneralMerchandise.objects.filter(product=product).delete()

        # Delete the product from the Products table
        product.delete()

        return JsonResponse({'success': True})

    return JsonResponse({'error': 'Invalid request'}, status=400)

def sign_in(request):
    """
    Handles user sign-in functionality. Identifies whether the user is an admin or customer
    and redirects them to the homepage while storing their role in the session.
    """
    if request.method == 'POST':
        form = SignInForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            try:
                # Authenticate user by checking username and password
                user = User.objects.get(email_address=email, password=password)

                # Determine the user's role
                user_role = 'customer' if Customer.objects.filter(user=user).exists() else 'admin'

                # Store user info in session
                request.session['user_id'] = user.user_id
                request.session['user_role'] = user_role
                request.session['user_name'] = user.user_name

                # Redirect to the next URL or home
                next_url = request.GET.get('next', 'home')  # Default to home if no next URL
                return redirect(next_url)

            except User.DoesNotExist:
                # Invalid username or password
                return render(request, 'SignIn.html', {
                    'form': form,
                    'errorMessage': 'Invalid username or password'
                })

        else:
            # Form validation errors
            return render(request, 'SignIn.html', {
                'form': form,
                'errorMessage': 'Please correct the errors below.'
            })

    else:
        # Handle GET request
        form = SignInForm()

    return render(request, 'SignIn.html', {'form': form})

def sign_up(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user_type = form.cleaned_data['userType']
            user_name = form.cleaned_data['User_Name']
            password = form.cleaned_data['Password']
            email = form.cleaned_data['Email_Address']
            phone = form.cleaned_data.get('Phone_Number', None)

            try:
                with transaction.atomic():  # Wrap the database operations in a transaction
                    # Create a new User
                    user = User.objects.create(
                        user_name=user_name,
                        password=password,
                        email_address=email,
                        phone_number=phone,
                    )

                    # Create Customer or Admin record
                    if user_type == 'customer':
                        bank_account = form.cleaned_data.get('Bank_Account', None)
                        home_address = form.cleaned_data.get('Home_Address', None)
                        Customer.objects.create(
                            user=user,
                            bank_account=bank_account,
                            home_address=home_address,
                        )
                    elif user_type == 'admin':
                        Admin.objects.create(user=user)

                    # Redirect to HomePage after successful sign-up
                    return redirect('home')

            except Exception as e:
                form.add_error(None, f"An error occurred: {str(e)}")
    else:
        form = SignUpForm()

    return render(request, 'SignUp.html', {'form': form})

def sign_out(request):
    """
    Clears the session data and redirects to the home page.
    """
    request.session.flush()  # Remove all session data
    return redirect('home')  # Redirect to the main page

def edit_product(request, product_id):
    product = get_object_or_404(Products, pk=product_id)
    food_beverage = None
    general_merchandise = None

    if product.category == "FOOD_BEVERAGE":
        food_beverage = FoodBeverage.objects.filter(product=product).first()
    elif product.category == "GENERAL_MERCHANDISE":
        general_merchandise = GeneralMerchandise.objects.filter(product=product).first()

    if request.method == 'POST':
        # Update product attributes
        product.proname = request.POST['proname']
        product.brand = request.POST['brand']
        product.cost = request.POST['cost']
        product.price = request.POST['price']
        product.prodescription = request.POST['prodescription']
        product.category = request.POST['category']
        product.save()

        # Update category-specific fields
        if product.category == "FOOD_BEVERAGE" and food_beverage:
            food_beverage.sell_by = request.POST['sell_by']
            food_beverage.save()
        elif product.category == "GENERAL_MERCHANDISE" and general_merchandise:
            general_merchandise.color = request.POST['color']
            general_merchandise.save()

        return redirect('home')  # Redirect back to the Home page

    return render(request, 'ProductEdit.html', {
        'product': product,
        'food_beverage': food_beverage,
        'general_merchandise': general_merchandise,
    })

def chatbox(request):
    return render(request, 'chat.html')

#Query in ChatGPT
@csrf_exempt
def chat_with_gpt(request):
    if request.method == "POST":
        try:
            # Ensure the user is authenticated
            user_id = request.session.get("user_id")
            if not user_id:
                return JsonResponse(
                    {"response": "Please log in first to start with the chat."},
                    status=200
                )

            
            # Determine user role dynamically
            is_customer = Customer.objects.filter(user_id=user_id).exists()
            is_admin = Admin.objects.filter(user_id=user_id).exists()
            user_role = "customer" if is_customer else "admin"

            data = json.loads(request.body)
            user_message = data.get("message", "").lower()

            if "get products" in user_message:
                products = Products.objects.all()
                if products.exists():
                    product_list = "\n".join([
                        f"- {product.proname} (${product.price})" for product in products
                    ])
                    return JsonResponse(
                        {"response": f"Here are the available products:\n{product_list}"},
                        status=200
                    )
                else:
                    return JsonResponse(
                        {"response": "No products are available at the moment."},
                        status=200
                    )

                    # Handle specific product queries
            
            if "get product" in user_message:
                product_name = user_message.replace("get product", "").strip()
                product = Products.objects.filter(proname__icontains=product_name).first()
                if product:
                    return JsonResponse(
                        {
                            "response": f"Product: {product.proname}\nPrice: ${product.price}\nDescription: {product.prodescription}"},
                        status=200
                    )
                else:
                    return JsonResponse(
                        {"response": f"No product found matching '{product_name}'."},
                        status=200
                    )

            print(f"Received message: {user_message}")  # Debugging statement

            # Handle "get all products with rating 5"
            if "get all products with rating over 3" in user_message:
                # Fetch products with a rating of 3
                products = Products.objects.filter(rating__rate_score__gt=3).distinct()
                if products.exists():
                    product_list = "\n".join([
                        f"- {product.proname} (${product.price})"
                        for product in products
                    ])
                    return JsonResponse(
                        {"response": f"Products with a rating over 3:\n{product_list}"},
                        status=200
                    )
                else:
                    return JsonResponse(
                        {"response": "No products found with a rating over 3."},
                        status=200
                    )

            # Admin-only queries
            admin_only_queries = [
                "get order history of user id:",
                "get the user information of user id:",
                "get all orders on",
                "get expired food and beverage products",
            ]

            # Check if the user is allowed to perform the requested action
            if any(query in user_message for query in admin_only_queries):
                if user_role != "admin":
                    return JsonResponse(
                        {"response": "You do not have permission to perform this action."},
                        status=403
                    )

            # Handle admin queries
            if "get order history of user id:" in user_message:
                try:
                    user_id_str = user_message.split("user id:")[1].strip()
                    target_user_id = int(user_id_str)
                except (IndexError, ValueError):
                    return JsonResponse(
                        {"response": "Invalid format. Use 'get order history of user id: <user_id>'."},
                        status=400
                    )

                orders = Orders.objects.filter(user_id=target_user_id).prefetch_related('orderitem_set__product')
                if orders.exists():
                    order_history = []
                    for order in orders:
                        items = order.orderitem_set.all()
                        item_details = "\n".join([
                            f"    - {item.product.proname} (Quantity: {item.quantity})"
                            for item in items
                        ])
                        order_history.append(
                            f"Order ID: {order.order_id}\nItems:\n{item_details}"
                        )
                    history = "\n\n".join(order_history)
                    return JsonResponse(
                        {"response": f"Here is the order history for user ID {target_user_id}:\n\n{history}"},
                        status=200
                    )
                else:
                    return JsonResponse(
                        {"response": f"No orders found for user ID {target_user_id}."},
                        status=200
                    )

            # Admin-specific query: Get expired food and beverage products
            if "get expired food and beverage products" in user_message:

                expired_products = FoodBeverage.objects.filter(sell_by__lt=now()).select_related('product')

                if expired_products.exists():
                    products_data = [
                        f"- {item.product.proname} (Brand: {item.product.brand}, Sell By: {item.sell_by})"
                        for item in expired_products
                    ]
                    response_message = "Here are the expired food and beverage products:\n" + "\n".join(products_data)
                else:
                    response_message = "No expired food and beverage products found."

                return JsonResponse({"response": response_message}, status=200)
            
            # Handle "get the user information of user id"
            if "get the user information of user id:" in user_message:
                # Extract the user ID after "user id:"
                try:
                    user_id_str = user_message.split("user id:")[1].strip()
                    user_id = int(user_id_str)
                except (IndexError, ValueError):
                    return JsonResponse(
                        {"response": "Invalid format. Use 'get the user information of user id: <user_id>'."},
                        status=400
                    )

                # Fetch user information
                try:
                    user = User.objects.get(user_id=user_id)
                    user_info = {
                        "User ID": user.user_id,
                        "Name": user.user_name,
                        "Email": user.email_address,
                        "Phone": user.phone_number,
                    }

                    # Check if the user is a customer
                    try:
                        customer = Customer.objects.get(user_id=user_id)
                        user_info["Home Address"] = customer.home_address
                    except Customer.DoesNotExist:
                        user_info["Home Address"] = "Not Applicable"

                    response = "\n".join([f"{key}: {value}" for key, value in user_info.items()])
                    return JsonResponse({"response": f"User Information:\n{response}"}, status=200)
                except User.DoesNotExist:
                    return JsonResponse(
                        {"response": f"No user found with ID {user_id}."},
                        status=200
                    )

            # Handle "get all orders on <date>" or variations
            if "get the all orders on" in user_message or "get all orders on" in user_message:
                # Extract the date from the message
                try:
                    if "get the all orders on" in user_message:
                        date_str = user_message.split("get the all orders on")[1].strip()
                    else:
                        date_str = user_message.split("get all orders on")[1].strip()

                    order_date = datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
                except (IndexError, ValueError):
                    return JsonResponse(
                        {"response": "Invalid format. Use 'get all orders on <YYYY-MM-DD>' to fetch orders."},
                        status=400
                    )

                # Fetch orders for the specified date
                orders = Orders.objects.filter(order_date__date=order_date).prefetch_related(
                    'orderitem_set__product')
                if orders.exists():
                    order_list = []
                    for order in orders:
                        items = order.orderitem_set.all()
                        item_details = "\n".join([
                            f"    - {item.product.proname} (Quantity: {item.quantity})"
                            for item in items
                        ])
                        order_list.append(
                            f"Order ID: {order.order_id}\nItems:\n{item_details}"
                        )

                    response = "\n\n".join(order_list)
                    return JsonResponse(
                        {"response": f"Orders on {order_date}:\n\n{response}"},
                        status=200
                    )
                else:
                    return JsonResponse(
                        {"response": f"No orders found on {order_date}."},
                        status=200
                    )


            # Handle other messages
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a helpful assistant."},
                    {"role": "user", "content": user_message},
                ]
            )
            gpt_response = response['choices'][0]['message']['content']
            return JsonResponse({"response": gpt_response}, status=200)

        except Exception as e:
            print(f"Error: {e}")  # Debugging statement
            return JsonResponse({"response": f"An error occurred: {str(e)}"}, status=500)

    return JsonResponse({"response": "Invalid request method."}, status=400)

def order_history(request):
    user_role = request.session.get('user_role')
    user_id = request.session.get('user_id')

    if not user_role or not user_id:
        return redirect('sign_in')

    # Fetch orders based on the user's role
    if user_role == 'admin':
        orders = Orders.objects.select_related('user').all()
    elif user_role == 'customer':
        orders = Orders.objects.filter(user_id=user_id).select_related('user')
    else:
        return redirect('sign_in')

    # Prepare orders for the template
    order_details = []
    for order in orders:
        items = OrderItem.objects.filter(order=order).select_related('product')
        payment = Payment.objects.filter(order=order).first()
        delivery = Delivery.objects.filter(order=order).first()
        customer = Customer.objects.filter(user=order.user).first()

        order_details.append({
            'user_id': order.user.user_id,
            'user_name': order.user.user_name,
            'order_id': order.order_id,
            'items': [{'product_name': item.product.proname, 'quantity': item.quantity} for item in items],
            'order_date': order.order_date,
            'payment_id': payment.payment_id if payment else 'N/A',
            'total_amount': payment.total_amount if payment else 0,
            'bank_account': customer.bank_account if customer else 'N/A',
            'delivery_id': delivery.delivery_id if delivery else 'N/A',
            'delivery_address': delivery.delivery_address if delivery else 'N/A',
            'delivery_method': delivery.delivery_method if delivery else 'N/A',
        })

    context = {'orders': order_details}
    return render(request, 'order_history.html', context)

def add_to_order(request, product_id):
    if request.method == "POST":
        # Retrieve quantity from the form
        quantity = int(request.POST.get("quantity", 1))  # Default to 1 if no quantity is provided
        user_id = request.session.get('user_id')  # Retrieve user_id from session
        
        print(f"Product ID: {product_id}, Quantity: {quantity}, User ID: {user_id}")

        if not user_id:
            return redirect('/sign-in/?next=' + request.path)  # Redirect to sign-in if user is not authenticated

        # Check if the user has an in-progress order
        order, created = Orders.objects.get_or_create(user_id=user_id, order_status='in_progress')

        # Add or update the product in the order
        order_item, created = OrderItem.objects.get_or_create(
            order_id=order.order_id,
            product_id=product_id,
            defaults={'quantity': quantity}  # Use the selected quantity when creating the item
        )
        if not created:
            # If the item already exists in the order, increment the quantity
            order_item.quantity += quantity
            order_item.save()

        return redirect('order_in_process')  # Redirect to the order-in-process page

    return redirect('home')  # Redirect to home if the method is not POST

def order_in_process(request):
    user_id = request.session.get('user_id')  # Retrieve user_id from session
    try:
        order = Orders.objects.get(user_id=user_id, order_status='in_progress')
        items = OrderItem.objects.filter(order_id=order.order_id).select_related('product')
        for item in items:
            item.total_price = item.quantity * item.product.price
    except Orders.DoesNotExist:
        order = None
        items = []

    context = {
        'order': order,
        'items': items,
    }
    return render(request, 'order_in_process.html', context)

def submit_order(request):
    if request.method == "POST":
        # user = request.user
        user_id = request.session.get('user_id')  # Retrieve user_id from session
        try:
             # Use transaction to ensure atomicity
            with transaction.atomic():
                # Update the order status to 'completed'
                order = Orders.objects.get(user_id=user_id, order_status='in_progress')
                customer = Customer.objects.get(user_id=user_id)

                 # Retrieve all items in the order
                order_items = OrderItem.objects.filter(order_id=order.order_id).select_related('product')

                # Calculate the total price of the order
                total_price = sum(item.quantity * item.product.price for item in order_items)

                # Update product quantities and save them
                for item in order_items:
                    product = item.product
                    
                    # Ensure there is enough stock
                    if product.quantity_available is None or product.quantity_available < item.quantity:
                        return JsonResponse({"success": False, "message": f"Insufficient stock for product {product.proname}!"})
                    
                    # Update product stock and sold quantities
                    product.quantity_available -= item.quantity
                    product.quantity_sold = (product.quantity_sold or 0) + item.quantity
                    product.save()

                # Update the order status and set the new order date
                order.order_status = 'completed'
                order.order_date = now() # Set the current date and time as the new order_date
                order.total_price = total_price  # Save the calculated total price
                order.save()

                # Create a payment record in the Payment table
                Payment.objects.create(
                    order_id=order.order_id,
                    user_id=user_id,
                    order_date=order.order_date,
                    total_amount=total_price
                )

                # Create a delivery record in the Delivery table
                Delivery.objects.create(
                    order_id=order.order_id,
                    user_id=user_id,
                    delivery_address=customer.home_address
                )

            return JsonResponse({"success": True})
        
        except Orders.DoesNotExist:
            return JsonResponse({"success": False, "message": "No in-progress order found!"})

    return JsonResponse({"success": False, "message": "Invalid request!"})

def order_summary(request):
    user_id = request.session.get('user_id')
    
    # Fetch Payment, Delivery, and Customer details for the current user
    payment = Payment.objects.filter(user_id=user_id).latest('order_date')  # Get the latest payment
    delivery = Delivery.objects.filter(user_id=user_id).first()
    customer = Customer.objects.get(user_id=user_id)
    user = User.objects.get(user_id=user_id)

    context = {
        'payment': payment,
        'delivery': delivery,
        'customer': customer,
        'user': user
    }
    return render(request, 'order_summary.html', context)

def complete_order(request):
    if request.method == "POST":
        user_id = request.session.get('user_id') # Retrieve user ID from session
        delivery_method = request.POST.get('delivery_method') # Get the selected delivery method

        if not user_id:
            return JsonResponse({"success": False, "message": "User not logged in!"})

        try:
            # Fetch the latest delivery record for the user
            delivery = Delivery.objects.filter(user_id=user_id).latest('delivery_id')
            delivery.delivery_method = delivery_method
            delivery.save()

            # Redirect to the success page after completing the order
            return redirect('success_page')
        
        except Delivery.DoesNotExist:
            return JsonResponse({"success": False, "message": "No delivery record found!"})

        except Exception as e:
            return JsonResponse({"success": False, "message": f"Error: {str(e)}"})

    return JsonResponse({"success": False, "message": "Invalid request!"})

def success_page(request):
    return render(request, 'success.html', {'message': 'Payment successful!'})
