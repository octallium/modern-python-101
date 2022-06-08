"""
Cash Register:
--------------
Louis is starting a new store in Zortan and wants to create a cash
register to keep a record of sales.
"""
from datetime import datetime


class Customer:
    """Customer Details"""

    def __init__(self, first_name: str, last_name: str) -> None:
        self.first_name = first_name
        self.last_name = last_name

    def __repr__(self) -> str:
        return "<class 'Customer'>"

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"


class Item:
    """Simple Item for cash register"""

    def __init__(self, id: int, name: str, price: float, measurement_unit: str) -> None:
        self.id = id
        self.name = name
        self.price = price
        self.measurement_unit = measurement_unit  # E.g -> Kg or ml

    def __str__(self):
        return f"{self.name}: ${self.price}/{self.measurement_unit}"

    def __repr__(self) -> str:
        return "<class 'Item'>"


class InvoiceItem:
    """Line Item for cash register with purchase quantity & discount"""

    def __init__(self, item: Item, qty: int, discount: float = 0) -> None:
        self.item = item
        self.qty = qty
        self.discount = discount
        # Private Member
        self._sub_total = (item.price * qty) - discount

    def __repr__(self) -> str:
        return "<class 'InvoiceItem'>"

    def __str__(self) -> str:
        return (
            f"Item => {self.item}, Qty: {self.qty}, Discount: ${self.discount},"
            f" Sub Total: {self.get_sub_total():.2f}"
        )

    def get_sub_total(self) -> float:
        """Returns the sub-total"""
        return self._sub_total


class CashRegister:
    """Cash Register for each customer"""

    def __init__(self, customer: Customer) -> None:
        self.customer = customer
        self.items: dict[str, InvoiceItem] = {}
        self.purchase_date = datetime.now()
        # Private Member
        self._invoice_total: float = 0

    def __repr__(self) -> str:
        return "<class 'CashRegister'>"

    def __str__(self) -> str:
        return f"Customer: {self.customer}, Total Items: {len(self.items)}"

    def _inc_invoice_total(self, item: InvoiceItem) -> None:
        """Increment the total invoice value each time an item is added"""
        self._invoice_total += item.get_sub_total()

    def _dec_invoice_total(self, item: InvoiceItem) -> None:
        """Decrement the total invoice value each time when an item is removed or updated"""
        self._invoice_total -= item.get_sub_total()

    def add_item(self, item: Item, qty: int = 1, discount: float = 0) -> None:
        """Add's an item to cash register"""
        if item.name not in self.items:
            new_item = InvoiceItem(item, qty, discount)
            self.items[item.name] = new_item
            self._inc_invoice_total(new_item)
        else:
            print(f"{item.name} already in cart, update instead?")

    def update_item(self, item: Item, qty: int, discount: float) -> None:
        """Updates an existing item"""
        if item.name in self.items:
            old_item = self.items[item.name]
            self._dec_invoice_total(old_item)

            new_item = InvoiceItem(item, qty, discount)
            self.items[item.name] = new_item
            self._inc_invoice_total(new_item)
        else:
            print(f"{item.name} not in cart, purchase instead?")

    def remove_item(self, item: Item) -> None:
        """Removes item from cash register"""
        if item.name in self.items:
            old_item = self.items[item.name]
            self._dec_invoice_total(old_item)

            del self.items[item.name]

    def get_invoice_total(self) -> float:
        """Returns invoice total"""
        return self._invoice_total

    def display_invoice(self) -> None:
        print()
        print("+" * 70)
        print(self)
        print(f"Date: {self.purchase_date.strftime('%B %d, %Y')}")
        print("-" * 70)
        for item in self.items.values():
            print(item)
        print("-" * 70)
        print(f"Total Price: ${self.get_invoice_total():.2f}")
        print("+" * 70)


milk = Item(100, "Milk", 4.5, "Litre")
egg = Item(101, "Egg", 0.99, "Piece")
rice = Item(102, "Rice", 4, "Kg")
apple = Item(103, "Apple", 5.67, "Kg")

customer1 = Customer("Louis", "Zappa")

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

customer2 = Customer("Chiko", "Neutron")
cr2 = CashRegister(customer2)
cr2.add_item(milk, qty=4, discount=10)
cr2.add_item(egg, qty=25)
cr2.update_item(egg, qty=48, discount=12)
cr2.add_item(apple, qty=8, discount=2)
cr2.display_invoice()
