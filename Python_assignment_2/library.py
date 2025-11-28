# Name: Piyush Sharma
# Roll No: 2501201009
# Course: BCA
# Semester: 1st
# Subjest: Problem Solving with Python
# Tittle:  Library Inventory & Borrowing System 
# Date: 11-11-2025


# Task 1: Project Setup & Menu Screen 
print("Welcome to the Library Inventory & Borrowing System")
books = {}
borrowed = {}
def menu():
    print("\nLibrary Menu:")
    print("1. Add Book")
    print("2. View Books")
    print("3. Search Book")
    print("4. Borrow Book")
    print("5. Return Book")
    print("6. Exit")
    print()
    print()

#  Task 2: Book Data Entry 
def add_book():
    book_id = input("Enter Book ID: ")
    title = input("Enter Book Title: ")
    author = input("Enter Book Author: ")
    copies = int(input("Enter Number of Copies: "))
    books[book_id] = {'title': title, 'author': author, 'copies': copies}
    print(f"Book '{title}' added successfully.")
    print()
    print()

    # Task 3: Display & Search Books 
def view_books():
    print("\nLibrary Inventory")
    print("ID\tTitle\t\tAuthor\t\tCopies")
    print("-"*50)
    for bid, info in books.items():
        print(f"{bid}\t{info['title']}\t\t{info['author']}\t\t{info['copies']}")
    print()

def search_book():
    choice = input("Search by (1) Book ID or (2) Title: ")
    if choice == "1":
        bid = input("Enter Book ID: ")
        if bid in books:
            print(f"\n Book Found: {books[bid]}\n")
        else:
            print("\n Book Not Found\n")
    elif choice == "2":
        title = input("Enter Title keyword: ").lower()
        found = False
        for bid, info in books.items():
            if title in info['title'].lower():
                print(f"\n Book Found: {bid} -> {info}\n")
                found = True
        if not found:
            print("\nBook Not Found\n")
print()
print()

# Task 4: Borrowing system
def borrow_book():
    student = input("Enter Student Name: ")
    bid = input("Enter Book ID: ")
    if bid in books and books[bid]["copies"] > 0:
        books[bid]["copies"] -= 1
        borrowed[student] = bid
        print(f"\n {student} borrowed '{books[bid]['title']}' successfully!\n")
    else:
        print("\n Book not available or invalid ID\n")
print()
print()

#Task 5: Return Book + List Comprehension
def return_book():
    student = input("Enter Student Name: ")
    bid = input("Enter Book ID: ")
    if student in borrowed and borrowed[student] == bid:
        books[bid]["copies"] += 1
        del borrowed[student]
        print(f"\n{student} returned '{books[bid]['title']}' successfully!\n")
    else:
        print("\n Invalid return details\n")

# List comprehension to show borrowed books
borrowed_list = [f"{s} -> {b}" for s, b in borrowed.items()]
print("\n Current Borrowed Books:")
for entry in borrowed_list:
    print(entry)
    print()
print()
print()

# Task 6: User Loop & Exit
def run_library():
    while True:
        menu()
        choice = input("Enter choice (1-6): ")
        
        if choice == "1":
            add_book()
        elif choice == "2":
            view_books()
        elif choice == "3":
            search_book()
        elif choice == "4":
            borrow_book()
        elif choice == "5":
            return_book()
        elif choice == "6":
            print("\n Exiting Library Manager. Goodbye!\n")
            break
        else:
            print("\n Invalid choice, try again.\n")
print()
print()

# Task 7: Bonus Task — Save/Load Records
def save_records():
    with open("library_records.txt", "w") as f:
        f.write("Books:\n")
        for bid, info in books.items():
            f.write(f"{bid},{info['title']},{info['author']},{info['copies']}\n")
        f.write("\nBorrowed:\n")
        for student, bid in borrowed.items():
            f.write(f"{student},{bid}\n")
    print("Records saved to library_records.txt")
print()
print()

# Run Program
if __name__ == "__main__":
    run_library()
    save_choice = input("\nDo you want to save records? (yes/no): ")
    if save_choice.lower() == "yes":
        save_records()
