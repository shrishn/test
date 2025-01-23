# Function to add items to the shopping cart
def add_to_cart(cart, item, fixed_price, quantity):
    if item not in cart:
        # Add item to cart if it's not already there 
        cart[item] = {'price': fixed_price, 'quantity': quantity}
        return "Item added to the cart"
    else:
        # Update quantity if the item is already in the cart
        cart[item]['quantity'] += quantity
        return f"Quantity updated for {item} in the cart"

# Function to view the shopping cart
def view_cart(cart):
    if not cart:
        return "No items in the cart"
    cart_details = "Items in the Cart:\n"
    for item, details in cart.items():
        cart_details += f"{item}: {details['quantity']} x Rs.{details['price']} each\n"
    return cart_details.strip()

# Function to calculate the total price of items in the cart
def calculate_total(cart):
    total_price = sum(details['price'] * details['quantity'] for details in cart.values())
    return total_price

def main():
    # Predefined items and their fixed prices
    items_and_prices = {
        'Laptop': 48000.0,
        'Mouse': 1000.0,
        'Keyboard': 35000.0,
        'Headphones': 2000.0,
        'Printer': 15000.0
    }
    
    # Initialize an empty shopping cart
    cart = {}

    while True:
        # Display menu options
        print("\nItems: Laptop, Mouse, Keyboard, Headphones, Printer")
        print("1. Add item to cart")
        print("2. View cart")
        print("3. Calculate total")
        print("4. Exit")
        
        # Get user's choice
        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            # Add item to cart
            item_name = input("Enter the item name: ")
            quantity = int(input("Enter the quantity: "))
            
            # Check if the item is valid
            if item_name in items_and_prices:
                fixed_price = items_and_prices[item_name]
                result = add_to_cart(cart, item_name, fixed_price, quantity)
                print(result)
            else:
                print("Invalid item name. Item not added to the cart")

        elif choice == '2':
            # View the cart
            result = view_cart(cart)
            print(result)

        elif choice == '3':
            # Calculate total
            total_price = calculate_total(cart)
            print(f"Total Price: Rs. {total_price:.2f}")

        elif choice == '4':
            # Exit the program
            print("Thank you!")
            break

        else:
            # Handle invalid choice
            print("Invalid choice")

if __name__ == "__main__":
    main()