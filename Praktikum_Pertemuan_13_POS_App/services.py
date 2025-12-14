from abc import ABC, abstractmethod
from models import CartItem

class IPaymentProcessor(ABC):
    @abstractmethod
    def pay(self, amount):
        pass


class CashPayment(IPaymentProcessor):
    def pay(self, amount):
        print(f"Pembayaran tunai sebesar Rp{amount} berhasil.")


class DebitCardPayment(IPaymentProcessor):
    def pay(self, amount):
        print(f"Pembayaran debit sebesar Rp{amount} berhasil.")


class CartService:
    def __init__(self):
        self.items = []

    def add_item(self, product, quantity):
        self.items.append(CartItem(product, quantity))

    def calculate_total(self):
        return sum(item.get_total_price() for item in self.items)
