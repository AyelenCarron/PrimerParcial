import csv
from models import Book, Magazine

def load_library_items(path):
    items = []
    with open(path, newline='', encoding='latin1') as file:
        reader = csv.reader(file)
        for row in reader:
            try:
                tipo = row[0].strip().lower()
                title = row[1]
                item_id = int(row[2])
                if tipo == "book":
                    author = row[3]
                    pages = int(row[4])
                    items.append(Book(title, item_id, author, pages))
                elif tipo == "magazine":
                    issue_number = int(row[3])
                    items.append(Magazine(title, item_id, issue_number))
            except Exception as e:
                print("Error:", row, "->", e)
    return items

def checkout_items(items, user):
    return [item.checkout(user) for item in items]

def count_items(items):
    counts = {"book": 0, "magazine": 0}
    for item in items:
        if isinstance(item, Book):
            counts["book"] += 1
        elif isinstance(item, Magazine):
            counts["magazine"] += 1
    return counts

def find_by_title(items, keyword):
    keyword = keyword.lower()
    return [item for item in items if keyword in item.title.lower()]