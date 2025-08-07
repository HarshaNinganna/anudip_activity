import csv
from datetime import datetime

class Item:
    def __init__(self, name, quantity, price):
        self.name = name
        self.quantity = quantity
        self.price = price
        self.total = quantity * price

class Invoice:
    def __init__(self):
        self.items = []

    def add_item(self, name, quantity, price):
        item = Item(name, quantity, price)
        self.items.append(item)
        print(f" Added {quantity} x {name} @ ₹{price} each")

    def view_invoice(self):
        if not self.items:
            print(" No items in the invoice.")
            return

        print("\n Invoice Summary:")
        subtotal = 0
        for item in self.items:
            print(f"- {item.name} x{item.quantity} = ₹{item.total}")
            subtotal += item.total

        gst = round(subtotal * 0.18, 2)
        grand_total = round(subtotal + gst, 2)

        print(f"\nSubtotal: ₹{subtotal}")
        print(f"GST (18%): ₹{gst}")
        print(f"Grand Total: ₹{grand_total}")

    def export_csv(self):
        if not self.items:
            print(" No items to export.")
            return

        now = datetime.now().strftime("%Y_%m_%d_%H%M%S")
        filename = f"invoice_{now}.csv"

        with open(filename, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["Item", "Quantity", "Price", "Total"])

            subtotal = 0
            for item in self.items:
                writer.writerow([item.name, item.quantity, item.price, item.total])
                subtotal += item.total

            gst = round(subtotal * 0.18, 2)
            grand_total = round(subtotal + gst, 2)

            writer.writerow([])
            writer.writerow(["", "", "Subtotal", subtotal])
            writer.writerow(["", "", "GST 18%", gst])
            writer.writerow(["", "", "Grand Total", grand_total])

        print(f" Invoice exported to: {filename}")

def main():
    invoice = Invoice()

    while True:
        print("\n--- QuickBill Menu ---")
        print("1. Add Item")
        print("2. View Invoice")
        print("3. Export Invoice to CSV")
        print("4. Exit")

        choice = input("Enter your choice (1–4): ")

        if choice == "1":
            name = input("Enter item name: ")
            try:
                qty = int(input("Enter quantity: "))
                price = float(input("Enter price per item: "))
                invoice.add_item(name, qty, price)
            except ValueError:
                print(" Invalid input. Please enter numbers for quantity and price.")
        
        elif choice == "2":
            invoice.view_invoice()

        elif choice == "3":
            invoice.export_csv()

        elif choice == "4":
            print(" Exiting QuickBill. Thank you!")
            break

        else:
            print(" Invalid choice. Please select from 1 to 4.")

if __name__ == "__main__":
    main()
