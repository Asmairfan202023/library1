import json

class PersonalLibraryManager:
    def __init__(self, filename="library.json"):
        self.filename = filename
        self.library = self.load_library()

    def load_library(self):
        try:
            with open(self.filename, "r") as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def save_library(self):
        with open(self.filename, "w") as file:
            json.dump(self.library, file, indent=4)

    def add_book(self):
        title = input("Enter book title: ")
        author = input("Enter author: ")
        year = input("Enter publication year: ")
        genre = input("Enter genre: ")
        read_status = input("Have you read this book? (yes/no): ").strip().lower()
        book = {
            "title": title,
            "author": author,
            "year": year,
            "genre": genre,
            "read": read_status == "yes"
        }
        self.library.append(book)
        self.save_library()
        print("Book added successfully!\n")

    def remove_book(self):
        title = input("Enter the title of the book to remove: ")
        self.library = [book for book in self.library if book["title"].lower() != title.lower()]
        self.save_library()
        print("Book removed successfully (if it existed).\n")

    def search_books(self):
        keyword = input("Enter a title or author to search for: ").lower()
        results = [book for book in self.library if keyword in book["title"].lower() or keyword in book["author"].lower()]
        if results:
            print("Search Results:")
            for book in results:
                print(f"Title: {book['title']}, Author: {book['author']}, Year: {book['year']}, Genre: {book['genre']}, Read: {'Yes' if book['read'] else 'No'}")
        else:
            print("No books found.\n")

    def show_statistics(self):
        total_books = len(self.library)
        read_books = sum(1 for book in self.library if book["read"])
        unread_books = total_books - read_books
        print(f"Total Books: {total_books}")
        print(f"Read Books: {read_books}")
        print(f"Unread Books: {unread_books}\n")

    def display_menu(self):
        while True:
            print("\nPersonal Library Manager")
            print("1. Add Book")
            print("2. Remove Book")
            print("3. Search Books")
            print("4. Show Statistics")
            print("5. Exit")
            choice = input("Enter your choice: ")
            if choice == "1":
                self.add_book()
            elif choice == "2":
                self.remove_book()
            elif choice == "3":
                self.search_books()
            elif choice == "4":
                self.show_statistics()
            elif choice == "5":
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    manager = PersonalLibraryManager()
    manager.display_menu()
