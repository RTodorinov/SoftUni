import os
import django


# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

from django.db.models import Count, Avg, Min, Max, Sum, Value, Q, F
from main_app.models import Product, Category, Customer, Order, OrderProduct


# Create and run queries
# def add_records_to_database():
#     # Categories
#     food_category = Category.objects.create(name='Food')
#     drinks_category = (Category.objects.create(name='Drinks'))
#
#     # Food
#     product1 = Product.objects.create(name='Pizza', description='Delicious pizza with toppings', price=10.99, category=food_category, is_available=False)
#     product2 = Product.objects.create(name='Burger', description='Classic burger with cheese and fries', price=7.99, category=food_category, is_available=False)
#     product3 = Product.objects.create(name='Apples', description='A bag of juicy red apples', price=3.99, category=food_category, is_available=True)
#     product4 = Product.objects.create(name='Bread', description='A freshly baked loaf of bread', price=2.49, category=food_category, is_available=True)
#     product5 = Product.objects.create(name='Pasta and Sauce Bundle', description='Package containing pasta and a jar of pasta sauce', price=6.99, category=food_category, is_available=False)
#     product6 = Product.objects.create(name='Tomatoes', description='A bundle of ripe, red tomatoes', price=2.99, category=food_category, is_available=True)
#     product7 = Product.objects.create(name='Carton of Eggs', description='A carton containing a dozen fresh eggs', price=3.49, category=food_category, is_available=True)
#     product8 = Product.objects.create(name='Cheddar Cheese', description='A block of aged cheddar cheese', price=7.99, category=food_category, is_available=False)
#     product9 = Product.objects.create(name='Milk', description='A gallon of fresh cow milk', price=3.49, category=food_category, is_available=True)
#
#     # Drinks
#     product10 = Product.objects.create(name='Coca Cola', description='Refreshing cola drink', price=1.99, category=drinks_category, is_available=True)
#     product11 = Product.objects.create(name='Orange Juice', description='Freshly squeezed orange juice', price=2.49, category=drinks_category, is_available=False)
#     product12 = Product.objects.create(name='Bottled Water', description='A 12-pack of purified bottled water', price=4.99, category=drinks_category, is_available=True)
#     product13 = Product.objects.create(name='Orange Soda', description='A 6-pack of carbonated orange soda', price=5.49, category=drinks_category, is_available=True)
#     product14 = Product.objects.create(name='Bottled Green Tea', description='A bottled green tea', price=3.99, category=drinks_category, is_available=False)
#     product15 = Product.objects.create(name='Beer', description='A bottled craft beer', price=5.49, category=drinks_category, is_available=True)
#
#     # Customers
#     customer1 = Customer.objects.create(username='john_doe')
#     customer2 = Customer.objects.create(username='alex_alex')
#     customer3 = Customer.objects.create(username='peter132')
#     customer4 = Customer.objects.create(username='k.k.')
#     customer5 = Customer.objects.create(username='peter_smith')
#
#     # Orders
#     order1 = Order.objects.create(customer=customer1)
#     order_product1 = OrderProduct.objects.create(order=order1, product=product3, quantity=2)
#     order_product2 = OrderProduct.objects.create(order=order1, product=product6, quantity=1)
#     order_product3 = OrderProduct.objects.create(order=order1, product=product7, quantity=5)
#     order_product4 = OrderProduct.objects.create(order=order1, product=product13, quantity=1)
#
#     order2 = Order.objects.create(customer=customer3)
#     order_product5 = OrderProduct.objects.create(order=order2, product=product3, quantity=2)
#     order_product6 = OrderProduct.objects.create(order=order2, product=product9, quantity=1)
#
#     order3 = Order.objects.create(customer=customer1)
#     order_product5 = OrderProduct.objects.create(order=order3, product=product12, quantity=4)
#     order_product6 = OrderProduct.objects.create(order=order3, product=product7, quantity=3)
#     return "All data entered!"


# Run and print your queries
# print(add_records_to_database())


# print('All Products:')
# print(Product.objects.all())
# print()
# print('All Available Products:')
# print(Product.objects.available_products())
# print()
# print('All Available Food Products:')
# print(Product.objects.available_products_in_category("Food"))

# safe filter-tricks to ask for specific objects from db
# searched_products = Product.objects.all().only('name', 'price')
# for p in searched_products:
#     print(p.name, p.price)

# searched_products = Product.objects.all().values('name', 'price')
# print(searched_products)

# all_products = Product.objects.all().count()
# print(all_products)

# all_products = Product.objects.aggregate(products_count=Count('id'))
# print(all_products)

# all_products = Product.objects.filter(price__gte=5).aggregate(Count('id'))
# print(all_products)

# all_products = Product.objects.filter(price__gte=3).aggregate(
#     average_price=Avg('price'),
#     min_price=Min('price'),
#     max_price=Max('price'),
# )
# print(all_products)

# def product_quantity_ordered():
#     result = []
#     orders = Product.objects.annotate(
#         total=Sum('orderproduct__quantity')
#     ).values('name', 'total').order_by('-total')
#
#     for order in orders:
#         result.append(f"Quantity ordered of {order['name']}: {order['total']}")
#     return '\n'.join(result)


def product_quantity_ordered():
    total_products_ordered = (
        Product.objects.annotate(total_ordered_quantity=Sum('orderproduct__quantity'))
        .exclude(total_ordered_quantity=None)
        .order_by('-total_ordered_quantity'))
    result = []
    for product in total_products_ordered:
        result.append(f"Quantity ordered of {product.name}:{product.total_ordered_quantity}")
    return "\n".join(result)


# print(product_quantity_ordered())

# just example of concatenate and annotate
# employees = Employee.objects.all().values('first_name', 'last_name').annotate(
#     full_name=Count('first_name', Value(' '), 'last_name', output_field=CharField(max_length=40))
# )
#
# for e in employees:
#     print(e['full_name'])

# def ordered_products_per_customer():
#     orders = Order.objects.prefetch_related('orderproduct_set__product__category').order_by('id')
#     result = []
#     for order in orders:
#         result.append(f'Order ID: {order.id}, Customer: {order.customer.username}')
#         for ordered_product in order.orderproduct_set.all():
#             result.append(f' - Product: {ordered_product.product.name}, Category: {ordered_product.product.category.name}')
#
#     return '\n'.join(result)
#
#
# print(ordered_products_per_customer())

def ordered_products_per_customer():
    prefetched_orders = Order.objects.prefetch_related('orderproduct_set__product__category').order_by('id')
    result = []
    for order in prefetched_orders:
        result.append(f"Order ID: {order.id}, Customer: {order.customer.username}")
        for order_product in order.orderproduct_set.all():
            result.append(f"- Product: {order_product.product.name}, Category: {order_product.product.category.name}")

    return "\n".join(result)


# print(ordered_products_per_customer())

# example for Q objects
# from users.models import Employee, City, Car
#
# employees = Employee.objects.filter(Q(city__name__icontains="P") | Q(salary__gte=4000))
# for e in employees:
#     print(f'{e.first_name} {e.last_name} {e.salary}')
# '''
# and = &
# OR = |
# NOT = ~
# '''

# employees = Employee.objects.filter(Q(salary__gte=4000) & ~Q(city__name='Pernik')).order_by('-salary', 'city_name')
# for e in employees:
#     print(f'{e.first_name} {e.last_name} {e.salary} {e.city.name}')

# def filter_products():
#     products = Product.objects.filter(Q(is_available=True) & Q(price__gt=3.00)).order_by('-price', 'name')
#     result = []
#     for product in products:
#         result.append(f"{product.name}: {product.price}lv.")
#     return "\n".join(result)


def filter_products():
    query = Q(is_available=True) & Q(price__gt=3.00)
    products = Product.objects.filter(query).order_by('-price', 'name')
    result = []
    for product in products:
        result.append(f"{product.name}: {product.price}lv.")
    return "\n".join(result)

# print(filter_products())


def give_discount():
    reduction = F('price') * 0.7
    query = Q(is_available=True) & Q(price__gt=3.00)
    Product.objects.filter(query).update(price=reduction)
    all_available_products = (Product.objects.filter(is_available=True).order_by('-price', 'name'))
    result = []
    for product in all_available_products:
        result.append(f"{product.name}: {product.price}lv.")
    return "\n".join(result)


# print(give_discount())


# examples of updates in db:
# from users.models import Employee, City, Car
#
# employees = Employee.objects.first()
# employee.salary *= 0.1
# employee.save()

# employees = Employee.objects.all()
# for e in employees:
#     e.salary *= 1.1
#     e.save()
#
# employees = Employee.objects.all().update(salary=F('salary') + 300)
