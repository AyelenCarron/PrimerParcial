from abc import ABC, abstractmethod

class LibraryItem(ABC):
    def __init__(self, title: str, item_id: int):
        if not title:
            raise ValueError("El título no puede estar vacío y debe ser una cadena de texto.")
        if item_id <= 0:
            raise ValueError("El ID debe ser un número entero positivo.")
        self.title = title
        self.item_id = item_id

    @abstractmethod
    def checkout(self, user: str) -> str:
        pass

class Book(LibraryItem):
    def __init__(self, title, item_id, author, pages):
        super().__init__(title, item_id)
        if not author:
            raise ValueError("El autor no puede estar vacío y debe ser una cadena de texto.")
        if pages <= 0:
            raise ValueError("El número de páginas debe ser un entero positivo.")
        self.author = author
        self.pages = pages

    def checkout(self, user):
        return f"Libro '{self.title}' prestado por {user}."

class Magazine(LibraryItem):
    def __init__(self, title, item_id, issue_number):
        super().__init__(title, item_id)
        if issue_number <= 0:
            raise ValueError("El número de emisión debe ser positivo.")
        self.issue_number = issue_number

    def checkout(self, user):
        return f"El libro/revista'{self.title}'número {self.issue_number} fue retirado por {user}."