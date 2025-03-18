import json

class Book:
    def __init__(self, title, author, year, genre, read_status):
        self.title = title
        self.author = author
        self.year = year
        self.genre = genre
        self.read_status = read_status

    def to_dict(self):
        return {
            "title": self.title,
            "author": self.author,
            "year": self.year,
            "genre": self.genre,
            "read_status": self.read_status
        }

class Library:
    def __init__(self, filename="library.json"):
        self.filename = filename
        self.books = []
        self.load_library()

    def save_library(self):
        with open(self.filename, "w") as f:
            json.dump([book.to_dict() for book in self.books], f, indent=4)

    def load_library(self):
        try:
            with open(self.filename, "r") as f:
                data = json.load(f)
                self.books = [Book(
                    title=book["title"],
                    author=book["author"],
                    year=book["year"],
                    genre=book["genre"],
                    read_status=book.get("read_status", False)
                ) for book in data]
        except (FileNotFoundError, json.JSONDecodeError):
            self.books = []

    def add_book(self):
        title = input("Enter title: ")
        author = input("Enter author: ")
        year = int(input("Enter publication year: "))
        genre = input("Enter genre: ")
        read_status = input("Has the book been read? (yes/no): ").strip().lower() == "yes"
        self.books.append(Book(title, author, year, genre, read_status))
        self.save_library()
        print("Book added successfully!")

    def remove_book(self):
        title = input("Enter the title of the book to remove: ")
        self.books = [book for book in self.books if book.title.lower() != title.lower()]
        self.save_library()
        print("Book removed successfully!")

    def search_books(self):
        query = input("Enter title or author to search: ").lower()
        results = [book for book in self.books if query in book.title.lower() or query in book.author.lower()]
        self.display_books(results)

    def display_books(self, books=None):
        books = books if books is not None else self.books
        if not books:
            print("No books found.")
        else:
            for book in books:
                print(f"Title: {book.title}, Author: {book.author}, Year: {book.year}, Genre: {book.genre}, Read: {'Yes' if book.read_status else 'No'}")

    def display_statistics(self):
        total_books = len(self.books)
        read_books = sum(1 for book in self.books if book.read_status)
        percentage_read = (read_books / total_books * 100) if total_books > 0 else 0
        print(f"Total books: {total_books}, Read: {read_books} ({percentage_read:.2f}%)")

    def run(self):
        while True:
            print("\nLibrary Menu:")
            print("1. Add a book")
            print("2. Remove a book")
            print("3. Search for a book")
            print("4. Display all books")
            print("5. Display statistics")
            print("6. Exit")
            choice = input("Choose an option: ")
            
            if choice == "1":
                self.add_book()
            elif choice == "2":
                self.remove_book()
            elif choice == "3":
                self.search_books()
            elif choice == "4":
                self.display_books()
            elif choice == "5":
                self.display_statistics()
            elif choice == "6":
                print("Exiting... Goodbye!")
                break
            else:
                print("Invalid option, please try again.")

if __name__ == "__main__":
    library = Library()
    library.run()
