from cash_register import CashRegister
from customer import Customer as MyCustomer  # NOTE: Can create an alias
from item import Item

milk = Item(100, "Milk", 4.5, "Litre")
egg = Item(101, "Egg", 0.99, "Piece")
rice = Item(102, "Rice", 4, "Kg")
apple = Item(103, "Apple", 5.67, "Kg")

customer1 = MyCustomer("Louis", "Zappa")

cr1 = CashRegister(customer1)

cr1.add_item(milk)
cr1.add_item(egg, 12, 0.5)
cr1.update_item(egg, 10, 1)
cr1.add_item(rice, 3, 0.75)
cr1.add_item(rice, 3, 0.75)
cr1.update_item(apple, 10, 0)

cr1.display_invoice()

cr1.remove_item(egg)
cr1.display_invoice()

customer2 = MyCustomer("Chiko", "Neutron")
cr2 = CashRegister(customer2)
cr2.add_item(milk, qty=4, discount=10)
cr2.add_item(egg, qty=25)
cr2.update_item(egg, qty=48, discount=12)
cr2.add_item(apple, qty=8, discount=2)
cr2.display_invoice()

print(cr2.toJSON())
