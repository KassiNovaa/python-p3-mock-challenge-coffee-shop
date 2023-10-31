class Coffee:
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name ):
        if not hasattr (self, "_name "):
            if type(new_name) == str and len(new_name) >= 3:
                self._name = new_name

    @property
    def orders(self):
        return [ order for order in Order.all if order.coffee == self ]
    
        # this reads: for the orders in the Order.all instance if order.coffee == this order then return the order in this list
    
    def customers(self):
        return list({ orders.customer for orders in self.orders })
        
        # this reads: for the orders in self.orders method above which is a type of Order return a unique list of the orders for that specific (self) customer

    @property
    def num_orders(self):
        return len(self.orders)
        # this reads: the length of orders property method represented as self.orders (self is the specific instance of coffee) returns a total number the amount of time said (related to self) coffee has been ordered
    
    def average_price(self):
        # self.num_orders <-- this is the method we already have access to above that find the total number of specific coffee has been ordered
        sum_prices = sum([ orders.price for orders in self.orders ],0)
        # this reads: for the orders in self.orders (self = specific coffee) method return a list of the sum of the total price speant on that specific coffee 

        return sum_prices / self.num_orders
    

class Customer:
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, new_name ):
        if type(new_name) == str and 1 < len(new_name) >= 15:
            self._name = new_name
        
    @property
    def orders(self):
        return [ orders for orders in Order.all if orders.customer == self ]
    
        # this reads: for the orders in the Order.all instance if order.customer == this order then return the order in this list
    
    def coffees(self):
        return list({ orders.coffee for orders in self.orders })
        # this reads: for the orders in self.orders method above which is a type of Order return a unique list of the orders for that specific (self) coffee

    def create_order(self, coffee, price):
        return Order(self,coffee,price)
        # this reads: return a NEW Order instance that recieves self = customer instance, a coffee instance, and price num/float
    
class Order:
    all = []
    def __init__(self, customer, coffee, price):
        self.customer = customer
        self.coffee = coffee
        self.price = price
        Order.all.append(self)

    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self, new_price ):
        if not hasattr( self, "_price" ):
            if type(new_price) == float and 1.0 <= new_price >= 10.0:
                self.price = new_price

    @property
    def customer(self):
        return self._customer
    
    @customer.setter
    def customer( self, new_customer ):
        # The isinstance() function returns True if the specified object is of the specified type, otherwise False.
        if isinstance( new_customer , Customer ):
             self._customer = new_customer

    @property
    def coffee(self):
        return self._coffee
    
    @coffee.setter
    def coffee( self, new_coffee ):
        if isinstance( new_coffee, Coffee ):
            self._coffee = new_coffee

    