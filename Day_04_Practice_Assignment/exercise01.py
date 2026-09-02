def manage_bookstore_inventory(inventory,action,book_title,quantity):
    if action.lower() == "add":
        if book_title in inventory:
            inventory[book_title] += quantity
        else:
            inventory[book_title] = quantity
    elif action.lower() == "sell":
        if book_title in inventory:
            if inventory[book_title] - quantity < 0:
                print(f"Error: Insufficient stock for {book_title}. Available: {inventory[book_title]}.")
                return inventory
            elif inventory[book_title] - quantity == 0:
                inventory.pop(book_title)
                return inventory
            else:
                inventory[book_title] -= quantity
        elif book_title not in inventory:
            print(f"Error: Book {book_title} not found in inventory")
            return inventory
        else:
            pass
    elif action.lower() == "lookup":
        if book_title in inventory:
            return inventory[book_title]
        else:
            return 0
    else:
        print("Invalid Action Parameter")
    return inventory

# Initial Inventory
inventory = {"Python Basics": 10, "Learning AI": 5}
print(inventory)

# 1. Add Stock
inventory = manage_bookstore_inventory(inventory, "add", "Python Basics", 5)
print(inventory)
# Result: {"Python Basics": 15, "Learning AI": 5}

# 2. Sell Stock Safely (Missing Book)
inventory = manage_bookstore_inventory(inventory, "sell", "Data Science 101", 1)
# print(inventory)
# Console output: Error: Book 'Data Science 101' not found in inventory.

# 3. Sell Stock (Insufficient)
inventory = manage_bookstore_inventory(inventory, "sell", "Learning AI", 10)
# print(inventory)
# Console output: Error: Insufficient stock for 'Learning AI'. Available: 5.

# 4. Sell Stock (Exactly Zero Stock)
inventory = manage_bookstore_inventory(inventory, "sell", "Learning AI", 5)
print(inventory)
# Result: {"Python Basics": 15}
