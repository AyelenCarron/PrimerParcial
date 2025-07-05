from utils import load_library_items, checkout_items, count_items, find_by_title

items = load_library_items("library.csv")

print("--- Checkout ---")
for msg in checkout_items(items, "Ezequiel"):
    print(msg)

print("--- Conteo ---")
print(count_items(items))

print("--- Búsqueda: 'Harry' ---")
result = find_by_title(items, "Harry")
for r in result:
    print(r.title)