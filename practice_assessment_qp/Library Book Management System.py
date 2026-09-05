"""
DELIMITED FLAT-FILE CATALOG MANAGEMENT SYSTEM
"""

books = [
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

counter = len(books)

#=================================================================

def menu():
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

def add_book():
    global counter

    try:
        title = input("Enter title: ").strip()

        if title == "":
            print("Title cannot be empty.")
            return

        author = input("Enter author: ").strip()

        if author == "":
            print("Author cannot be empty.")
            return

        genre = input("Enter genre: ").strip()

        if genre == "":
            print("Genre cannot be empty.")
            return

        price = float(input("Enter price: "))

        if price <= 0:
            print("Price must be greater than 0.")
            return

        copies = int(input("Enter copies: "))

        if copies < 0:
            print("Copies must be greater than or equal to 0.")
            return

        counter += 1

        book = {
            "id": counter,
            "title": title,
            "author": author,
            "genre": genre,
            "price": price,
            "copies": copies
        }

        books.append(book)

        print("Book added successfully.")

    except ValueError:
        print("Invalid numerical value. Please try again.")

#=================================================================

def print_one_book(b):
    print("----------------------------------------")
    print(f"ID       : {b['id']}")
    print(f"Title    : {b['title']}")
    print(f"Author   : {b['author']}")
    print(f"Genre    : {b['genre']}")
    print(f"Price    : {b['price']:.2f}")
    print(f"Copies   : {b['copies']}")
    print("----------------------------------------")

#=================================================================
def print_many_books(book_list):
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


def view_books():
    if len(books) == 0:
        print("No books available.")
        return

    if len(books) == 1:
        print_one_book(books[0])
    else:
        print_many_books(books)


def search_book_by_id(book_id):
    result = []

    for b in books:
        if b["id"] == book_id:
            result.append(b)

    if not result:
        print(f"No book found with id {book_id}.")
        return None

    print_one_book(result[0])
    return result[0]


def search_book_by_name(search_term):
    result = []

    for b in books:
        if (search_term.lower() in b["title"].lower()
                or search_term.lower() in b["author"].lower()):
            result.append(b)

    if not result:
        print("No matching books found.")
        return None

    if len(result) == 1:
        print_one_book(result[0])
    else:
        print_many_books(result)

    return result


def search_books():
    print("\n1. Search by ID")
    print("2. Search by Title/Author")

    try:
        choice = int(input("Enter choice: "))

        if choice == 1:
            book_id = int(input("Enter book id: "))
            search_book_by_id(book_id)

        elif choice == 2:
            search_term = input("Enter title or author: ").strip()

            if search_term == "":
                print("Search value cannot be empty.")
                return

            search_book_by_name(search_term)

        else:
            print("Invalid choice.")

    except ValueError:
        print("Invalid value. Please try again.")


def update_book():
    try:
        book_id = int(input("Enter book id to update: "))

        book = search_book_by_id(book_id)

        if book is None:
            return

        price_input = input(
            f"Enter new price ({book['price']}): "
        ).strip()

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

        copies_input = input(
            f"Enter new copies ({book['copies']}): "
        ).strip()

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

    except ValueError:
        print("Invalid book id. Please enter an integer.")


def delete_book():
    try:
        book_id = int(input("Enter book id to delete: "))

        book = search_book_by_id(book_id)

        if book is None:
            return

        answer = input(
            "Are you sure you want to delete this book? (y/n): "
        ).lower()

        if answer == "y":
            books.remove(book)
            print("Book deleted successfully.")

        else:
            print("Delete operation cancelled.")

    except ValueError:
        print("Invalid book id. Please enter an integer.")


def save_to_file():
    try:
        with open("books.txt", "w") as file:

            for b in books:
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


def load_from_file():
    global books
    global counter

    try:
        new_books = []

        with open("books.txt", "r") as file:

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

                new_books.append(book)

        books = new_books

        if len(books) > 0:
            counter = max(b["id"] for b in books)
        else:
            counter = 0

        print("Catalog loaded successfully.")

    except FileNotFoundError:
        print("books.txt file not found.")

    except ValueError:
        print("Invalid data found in books.txt.")

    except Exception:
        print("Error while loading catalog.")


def main():
    while True:

        choice = menu()

        match choice:

            case 1:
                add_book()

            case 2:
                view_books()

            case 3:
                search_books()

            case 4:
                update_book()

            case 5:
                delete_book()

            case 6:
                save_to_file()

            case 7:
                load_from_file()

            case 8:
                print("Exiting program...")
                break

            case _:
                print("Invalid choice. Please retry.")


if __name__ == "__main__":
    main()