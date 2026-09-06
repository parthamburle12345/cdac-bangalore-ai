"""
DELIMITED FLAT-FILE CATALOG MANAGEMENT SYSTEM
(Refactored Version -- Function signatures match PDF specification)
"""

FILE_PATH = "books.txt"

catalog = [
    {"id": 1, "title": "Python Programming", "author": "John Zelle",
     "genre": "Technical", "price": 650.00, "copies": 15},

    {"id": 2, "title": "Clean Code", "author": "Robert Martin",
     "genre": "Technical", "price": 950.00, "copies": 8},

    {"id": 3, "title": "The Great Gatsby", "author": "F. Scott Fitzgerald",
     "genre": "Fiction", "price": 350.00, "copies": 20},

    {"id": 4, "title": "Sapiens", "author": "Yuval Noah Harari",
     "genre": "History", "price": 550.00, "copies": 12},

    {"id": 5, "title": "Cosmos", "author": "Carl Sagan",
     "genre": "Science", "price": 480.00, "copies": 6}
]

#=================================================================

def menu() -> int:
    print("\n*** LIBRARY BOOK MANAGEMENT SYSTEM ***")
    print("======================================")
    print("1. Add Book")
    print("2. View Catalog")
    print("3. Search Books")
    print("4. Update Details")
    print("5. Delete Book")
    print("6. Save to File")
    print("7. Load from File")
    print("8. Exit")

    try:
        choice = int(input("Enter your choice: "))
        if choice < 1 or choice > 8:
            choice = -1
    except ValueError:
        choice = -1

    return choice

#=================================================================

def add_book_entry(catalog: list, next_id: int) -> int:
    """
    Prompts user for book details, validates input, appends a new
    book dict to catalog, and returns the updated next_id.
    """
    try:
        title = input("Enter title: ").strip()
        if title == "":
            print("Title cannot be empty.")
            return next_id

        author = input("Enter author: ").strip()
        if author == "":
            print("Author cannot be empty.")
            return next_id

        genre = input("Enter genre: ").strip()
        if genre == "":
            print("Genre cannot be empty.")
            return next_id

        price = float(input("Enter price: "))
        if price <= 0:
            print("Price must be greater than 0.")
            return next_id

        copies = int(input("Enter copies: "))
        if copies < 0:
            print("Copies must be greater than or equal to 0.")
            return next_id

        next_id += 1

        book = {
            "id": next_id,
            "title": title,
            "author": author,
            "genre": genre,
            "price": price,
            "copies": copies
        }

        catalog.append(book)
        print("Book added successfully.")
        return next_id

    except ValueError:
        print("Invalid numerical value. Please try again.")
        return next_id

#=================================================================

def print_one_book(b: dict) -> None:
    print("----------------------------------------")
    print(f"ID       : {b['id']}")
    print(f"Title    : {b['title']}")
    print(f"Author   : {b['author']}")
    print(f"Genre    : {b['genre']}")
    print(f"Price    : {b['price']:.2f}")
    print(f"Copies   : {b['copies']}")
    print("----------------------------------------")

#=================================================================

def print_many_books(book_list: list) -> None:
    print("-" * 90)
    print(
        f"{'ID':^5}"
        f"{'Title':<25}"
        f"{'Author':<25}"
        f"{'Genre':<15}"
        f"{'Price':>10}"
        f"{'Copies':>8}"
    )
    print("-" * 90)

    for b in book_list:
        print(
            f"{b['id']:^5}"
            f"{b['title']:<25}"
            f"{b['author']:<25}"
            f"{b['genre']:<15}"
            f"{b['price']:>10.2f}"
            f"{b['copies']:>8}"
        )

    print("-" * 90)

#=================================================================

def render_catalog(catalog: list) -> None:
    """Displays all books in the catalog."""
    if len(catalog) == 0:
        print("No books available.")
        return

    if len(catalog) == 1:
        print_one_book(catalog[0])
    else:
        print_many_books(catalog)

#=================================================================

def query_books(catalog: list, search_term: str) -> list:
    """
    Searches catalog by ID (if search_term is numeric) or by
    Title/Author substring (case-insensitive).
    Returns a list of matching book dicts (empty if none found).
    """
    if search_term.isdigit():
        book_id = int(search_term)
        result = [b for b in catalog if b["id"] == book_id]
        if not result:
            print(f"No book found with id {book_id}.")
        else:
            print_one_book(result[0])
        return result

    term = search_term.lower()
    result = [
        b for b in catalog
        if term in b["title"].lower() or term in b["author"].lower()
    ]

    if not result:
        print("No matching books found.")
    elif len(result) == 1:
        print_one_book(result[0])
    else:
        print_many_books(result)

    return result

#=================================================================

def search_books_menu(catalog: list) -> None:
    """Interactive sub-menu that drives query_books()."""
    print("\n1. Search by ID")
    print("2. Search by Title/Author")

    try:
        choice = int(input("Enter choice: "))

        if choice == 1:
            book_id = input("Enter book id: ").strip()
            query_books(catalog, book_id)

        elif choice == 2:
            search_term = input("Enter title or author: ").strip()
            if search_term == "":
                print("Search value cannot be empty.")
                return
            query_books(catalog, search_term)

        else:
            print("Invalid choice.")

    except ValueError:
        print("Invalid value. Please try again.")

#=================================================================

def modify_book_details(catalog: list, book_id: int) -> bool:
    """
    Finds the book with book_id in catalog, prompts for new price
    and copies, updates in-place.
    Returns True if updated, False if book not found.
    """
    book = None
    for b in catalog:
        if b["id"] == book_id:
            book = b
            break

    if book is None:
        print(f"No book found with id {book_id}.")
        return False

    print_one_book(book)

    price_input = input(f"Enter new price ({book['price']}): ").strip()
    if price_input == "":
        price = book["price"]
    else:
        try:
            price = float(price_input)
            if price <= 0:
                print("Invalid price. Price remains unchanged.")
                price = book["price"]
        except ValueError:
            print("Invalid price. Price remains unchanged.")
            price = book["price"]

    copies_input = input(f"Enter new copies ({book['copies']}): ").strip()
    if copies_input == "":
        copies = book["copies"]
    else:
        try:
            copies = int(copies_input)
            if copies < 0:
                print("Invalid copies. Copies remain unchanged.")
                copies = book["copies"]
        except ValueError:
            print("Invalid copies. Copies remain unchanged.")
            copies = book["copies"]

    book["price"] = price
    book["copies"] = copies
    print("Book updated successfully.")
    return True

#=================================================================

def update_book_menu(catalog: list) -> None:
    """Interactive wrapper that drives modify_book_details()."""
    try:
        book_id = int(input("Enter book id to update: "))
        modify_book_details(catalog, book_id)
    except ValueError:
        print("Invalid book id. Please enter an integer.")

#=================================================================

def delete_book(catalog: list) -> None:
    """
    Prompts for a book ID, confirms deletion, removes it from catalog.
    """
    try:
        book_id = int(input("Enter book id to delete: "))

        book = None
        for b in catalog:
            if b["id"] == book_id:
                book = b
                break

        if book is None:
            print(f"No book found with id {book_id}.")
            return

        print_one_book(book)

        answer = input(
            "Are you sure you want to delete this book? (y/n): "
        ).lower()

        if answer == "y":
            catalog.remove(book)
            print("Book deleted successfully.")
        else:
            print("Delete operation cancelled.")

    except ValueError:
        print("Invalid book id. Please enter an integer.")

#=================================================================

def sync_catalog_to_file(filepath: str, catalog: list) -> None:
    """
    Saves catalog to a pipe-delimited flat file at filepath.
    Overwrites existing content.
    """
    try:
        with open(filepath, "w") as file:
            for b in catalog:
                line = (
                    f"{b['id']}|"
                    f"{b['title']}|"
                    f"{b['author']}|"
                    f"{b['genre']}|"
                    f"{b['price']:.2f}|"
                    f"{b['copies']}\n"
                )
                file.write(line)
        print("Catalog saved successfully.")

    except Exception:
        print("Error while saving catalog.")

#=================================================================

def load_catalog_from_file(filepath: str) -> list:
    """
    Reads a pipe-delimited flat file and returns a list of book dicts.
    Returns an empty list on any error.
    """
    new_catalog = []

    try:
        with open(filepath, "r") as file:
            for line in file:
                data = line.strip().split("|")
                book = {
                    "id": int(data[0]),
                    "title": data[1],
                    "author": data[2],
                    "genre": data[3],
                    "price": float(data[4]),
                    "copies": int(data[5])
                }
                new_catalog.append(book)
        print("Catalog loaded successfully.")

    except FileNotFoundError:
        print(f"'{filepath}' file not found.")
    except ValueError:
        print(f"Invalid data found in '{filepath}'.")
    except Exception:
        print("Error while loading catalog.")

    return new_catalog

#=================================================================

def main():
    global catalog

    next_id = max(b["id"] for b in catalog) if catalog else 0

    while True:
        choice = menu()

        match choice:

            case 1:
                next_id = add_book_entry(catalog, next_id)

            case 2:
                render_catalog(catalog)

            case 3:
                search_books_menu(catalog)

            case 4:
                update_book_menu(catalog)

            case 5:
                delete_book(catalog)

            case 6:
                sync_catalog_to_file(FILE_PATH, catalog)

            case 7:
                loaded = load_catalog_from_file(FILE_PATH)
                if loaded:
                    catalog = loaded
                    next_id = max(b["id"] for b in catalog)

            case 8:
                print("Exiting program...")
                break

            case _:
                print("Invalid choice. Please retry.")


if __name__ == "__main__":
    main()
