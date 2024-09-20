from abc import ABC, abstractmethod

# Bas klassen Item
class Item(ABC):
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
        self.is_borrowed = False  # Flagga för att spåra om objektet är lånat

    @abstractmethod
    def display_info(self):
        pass

# Subklass Book som ärver från Item
class Book(Item):
    def __init__(self, title, author, year, pages):
        super().__init__(title, author, year)
        self.pages = pages

    def display_info(self):
        return f"Bok: {self.title}, Författare: {self.author}, År: {self.year}, Sidor: {self.pages}"

# Subklass Magazine som ärver från Item
class Magazine(Item):
    def __init__(self, title, author, year, issue):
        super().__init__(title, author, year)
        self.issue = issue

    def display_info(self):
        return f"magazine: {self.title}, Författare: {self.author}, År: {self.year}, Utgåva: {self.issue}"

# Klass LibraryUser för att representera låntagare
class LibraryUser:
    def __init__(self, name):
        self.name = name
        self.borrowed_items = []

    def borrow(self, item):
        if item.is_borrowed:
            raise Exception(f"{item.title} är redan lånat av någon annan.")
        item.is_borrowed = True
        self.borrowed_items.append(item)

    def return_item(self, item):
        if item in self.borrowed_items:
            item.is_borrowed = False
            self.borrowed_items.remove(item)
        else:
            raise Exception(f"{item.title} är inte lånat av {self.name}.")

    def list_borrowed_items(self):
        if not self.borrowed_items:
            print(f"{self.name} har inte lånat några objekt.")
        else:
            print(f"{self.name} har lånat följande objekt:")
            for item in self.borrowed_items:
                print(item.display_info())

# Klass Library som hanterar bibliotekets funktioner
class Library:
    def __init__(self):
        self.items = []
        self.users = []

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        if item in self.items:
            self.items.remove(item)
        else:
            raise Exception(f"{item.title} finns inte i biblioteket.")

    def register_user(self, user):
        self.users.append(user)

    def borrow_item(self, user, item):
        if item not in self.items:
            raise Exception(f"{item.title} finns inte i biblioteket.")
        user.borrow(item)

    def return_item(self, user, item):
        user.return_item(item)

    def list_items(self):
        print("Alla objekt i biblioteket:")
        for item in self.items:
            print(item.display_info())

    def list_available_items(self):
        print("Tillgängliga objekt i biblioteket:")
        for item in self.items:
            if not item.is_borrowed:
                print(item.display_info())

    def borrowed_summary(self):
        print("Sammanfattning över lånade objekt:")
        for user in self.users:
            if user.borrowed_items:
                print(f"{user.name} har lånat:")
                for item in user.borrowed_items:
                    print(item.display_info())
            else:
                print(f"{user.name} har inte lånat några objekt.")

# Exempel på användning av klasserna
def main():
    # Skapa bibliotek
    library = Library()

    # Skapa några böcker och tidskrifter
    book1 = Book("boktitel 1", "författare 1", 1949, 328)
    book2 = Book("boktitel 2", "författare 2", 1932, 311)
    magazine1 = Magazine("magazine 1", "författare 3", 2024, "September")

    # Lägg till objekt i biblioteket
    library.add_item(book1)
    library.add_item(book2)
    library.add_item(magazine1)

    # Registrera medlem
    user1 = LibraryUser("Alice")
    user2 = LibraryUser("Bob")
    library.register_user(user1)
    library.register_user(user2)

    # Låna böcker och magasin
    try:
        library.borrow_item(user1, book1)
        library.borrow_item(user2, magazine1)
    except Exception as e:
        print(e)

    # Visa lånade objekt
    user1.list_borrowed_items()
    user2.list_borrowed_items()

    # Försök att låna en redan lånad bok
    try:
        library.borrow_item(user2, book1)
    except Exception as e:
        print(e)

    # Visa alla böcker och magasin
    library.list_available_items()

    # Lämna tillbaka en bok
    try:
        library.return_item(user1, book1)
    except Exception as e:
        print(e)

    # Visa lånade objekt efter retur
    user1.list_borrowed_items()


    # Sammanfattning över lånade objekt
    library.borrowed_summary()

if __name__ == "__main__":
    main()
