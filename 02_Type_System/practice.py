"""
Louis wants to open a Pizza 🍕 Shop and needs to write
a program for accepting orders.

Tip -
-----
Always Visualize First, Then Start Coding.
"""

# -----------------------------------------------
# Variable Declaration
# -----------------------------------------------
 
customer = "Cece"
customer: str = "Prasanth Kannan"
customer: str = "Prasanth Kannan"
customer: str = "Prasanth Kannan"
customer: str = "Prasanth Kannan"
customer: str = "Prasanth Kannan"
customer: str = "Prasanth Kannan"
customer: str = "Prasanth"

pizza_base: str = "Thin"
pizza_base: str = "Large"
pizza_size: int = 12
pizza_size: int = 22
topping: str = "Olives"
topping: str = "Pepperoni"
extra_cheese: bool = True
extra_cheese: bool = False
price: float = 8.99
price: float = 12.99

# -----------------------------------------------
# Alternative 1 - Using Print Function
# -----------------------------------------------

print(f"Received order from: {customer}")
print(f"Pizza Base: {pizza_base}, Size: {pizza_size} inches, Topping: {topping}")
print(f"Is Extra Cheese required: {extra_cheese}")
print(f"Bill Amount: ${price}")


# -----------------------------------------------
# Alternative 1.1 - Using Formatted String
# -----------------------------------------------
 

# -----------------------------------------------
# Alternative 2 - Using Formatted String
# -----------------------------------------------

order_details: str = f"""
Received order from: {customer}
Pizza Base: {pizza_base}, Size: {pizza_size} inches, Topping: {topping}
Is Extra Cheese required: {extra_cheese}
Bill Amount: ${price}
"""

print(order_details)

# -------------------------------------------------
# Alternative 2.1 - Using Formatted String
# -------------------------------------------------

OrderDetails: str = f"""Received order from: {customer},   Pizza Base: {pizza_base}, Size: {pizza_size} inches, Topping: {topping}, Is Extra Cheese required: {extra_cheese}, Bill Amount: ${price} """

print(OrderDetails)

# -------------------------------------------------
# Alternative 3 - Using Formatted String in `print`
# -------------------------------------------------

print(
    f"""
Received order from: {customer}
Pizza Base: {pizza_base}, Size: {pizza_size} inches, Topping: {topping}
Is Extra Cheese required: {extra_cheese}
Bill Amount: ${price}
"""
)

