from datetime import datetime

inventory = {}


def add_product():
    product_id = input("Enter Product ID: ").strip()

    if product_id in inventory:
        print("❌ Product already exists.")
        return

    name = input("Enter product name: ").strip()
    category = input("Enter category: ").strip()

    try:
        price = float(input("Enter price: ₹"))
        quantity = int(input("Enter quantity: "))

        if price < 0 or quantity < 0:
            print("❌ Price and quantity cannot be negative.")
            return

    except ValueError:
        print("❌ Enter valid price and quantity.")
        return

    inventory[product_id] = {
        "name": name,
        "category": category,
        "price": price,
        "quantity": quantity,
        "added_on": datetime.now().strftime("%Y-%m-%d")
    }

    print("✅ Product added successfully!")


def display_inventory():
    if not inventory:
        print("\n📦 Inventory is empty.")
        return

    print("\n" + "=" * 75)
    print("                    INVENTORY")
    print("=" * 75)

    for product_id, product in inventory.items():
        value = product["price"] * product["quantity"]

        print(
            f"ID: {product_id} | "
            f"{product['name']} | "
            f"{product['category']} | "
            f"₹{product['price']:.2f} | "
            f"Qty: {product['quantity']} | "
            f"Value: ₹{value:.2f}"
        )


def update_stock():
    product_id = input("Enter Product ID: ").strip()

    if product_id not in inventory:
        print("❌ Product not found.")
        return

    try:
        change = int(
            input("Enter quantity to add/remove (+/-): ")
        )
    except ValueError:
        print("❌ Enter a valid number.")
        return

    new_quantity = inventory[product_id]["quantity"] + change

    if new_quantity < 0:
        print("❌ Stock cannot be negative.")
        return

    inventory[product_id]["quantity"] = new_quantity

    print("✅ Stock updated successfully!")


def search_product():
    keyword = input("Search product/category: ").lower().strip()

    found = False

    for product_id, product in inventory.items():

        if (
            keyword in product["name"].lower()
            or keyword in product["category"].lower()
        ):
            print(
                f"\nID: {product_id}\n"
                f"Name: {product['name']}\n"
                f"Category: {product['category']}\n"
                f"Price: ₹{product['price']:.2f}\n"
                f"Quantity: {product['quantity']}"
            )

            found = True

    if not found:
        print("❌ No matching product found.")


def low_stock_report():
    threshold = 5

    print("\n========== LOW STOCK ==========")

    found = False

    for product_id, product in inventory.items():

        if product["quantity"] <= threshold:
            print(
                f"{product_id} | "
                f"{product['name']} | "
                f"Stock: {product['quantity']}"
            )
            found = True

    if not found:
        print("✅ No products have low stock.")


def inventory_value():
    total = sum(
        product["price"] * product["quantity"]
        for product in inventory.values()
    )

    print(f"\n💰 Total Inventory Value: ₹{total:.2f}")


def delete_product():
    product_id = input("Enter Product ID to delete: ").strip()

    if product_id not in inventory:
        print("❌ Product not found.")
        return

    deleted = inventory.pop(product_id)

    print(f"✅ {deleted['name']} deleted successfully.")


def main():

    while True:

        print("\n")
        print("=" * 40)
        print("       📦 INVENTORY MANAGER")
        print("=" * 40)
        print("1. Add Product")
        print("2. Display Inventory")
        print("3. Update Stock")
        print("4. Search Product")
        print("5. Low Stock Report")
        print("6. Total Inventory Value")
        print("7. Delete Product")
        print("8. Exit")
        print("=" * 40)

        choice = input("Enter your choice: ")

        if choice == "1":
            add_product()

        elif choice == "2":
            display_inventory()

        elif choice == "3":
            update_stock()

        elif choice == "4":
            search_product()

        elif choice == "5":
            low_stock_report()

        elif choice == "6":
            inventory_value()

        elif choice == "7":
            delete_product()

        elif choice == "8":
            print("\n👋 Inventory Manager closed.")
            break

        else:
            print("❌ Invalid choice.")


if __name__ == "__main__":
    main()
