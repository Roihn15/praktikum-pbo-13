from repositories import ProductRepository
from services import CartService, DebitCardPayment

class PosApp:
    def __init__(self, product_repo, cart_service, payment_processor):
        self.product_repo = product_repo
        self.cart_service = cart_service
        self.payment_processor = payment_processor

    def run(self):
        while True:
            print("\n1. Tambah Produk ke Keranjang")
            print("2. Checkout")
            print("3. Keluar")
            choice = input("Pilih menu: ")

            if choice == "1":
                product_id = int(input("Masukkan ID Produk: "))
                quantity = int(input("Jumlah: "))
                product = self.product_repo.get_product_by_id(product_id)
                if product:
                    self.cart_service.add_item(product, quantity)
                    print("Produk ditambahkan ke keranjang.")
                else:
                    print("Produk tidak ditemukan.")
            elif choice == "2":
                total = self.cart_service.calculate_total()
                print(f"Total belanja: Rp{total}")
                self.payment_processor.pay(total)
                break
            elif choice == "3":
                break
            else:
                print("Pilihan tidak valid.")


if __name__ == "__main__":
    product_repo = ProductRepository()
    cart_service = CartService()
    payment_method = DebitCardPayment()
    app = PosApp(product_repo, cart_service, payment_method)
    app.run()
