import json
from datetime import datetime

from customer import Customer
from invoice_item import InvoiceItem
from item import Item


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

    def _get_items_as_dict(self) -> dict:
        items_dict = {}
        for item_name, invoice_item in self.items.items():
            items_dict[item_name] = invoice_item.dict()
        return items_dict

    def dict(self) -> dict:
        """Returns dictionary representation of Cash Register"""
        cash_register = {
            "customer": self.customer.dict(),
            "items": self._get_items_as_dict(),
            "purchase_date": self.purchase_date.strftime("%B %d, %Y"),
            "invoice_total": self.get_invoice_total(),
        }
        return cash_register

    def toJSON(self) -> str:
        """Returns JSON formatted string of Cash Register"""
        return json.dumps(self.dict(), indent=4, sort_keys=True)
