from equipment import Camera, Laptop


def add_item(items, item_id, name):
    kind = kind.strip().lower()

    if kind == "laptop":
        item = Laptop(item_id, name)
    elif kind == "camera":
        item = Camera(item_id, name)
    else:
        raise ValueError("Choose Laptop or Camera.")

    key = item.get_item_id()
    if key in items:
        raise ValueError("ID alredy exists.") 

    items[key] = item
    return item

def find_item(items, item_id):
    key = item_id.strip().upper()

    if key not in items:
        raise ValueError("ID not found.")

    return items[key]

def describe(item):
    due = item.get_due()

    if due is None:
        status = "Available"
    else:
        borrower = item.get_borrower()
        status = f"On loan to {borrower}, due {due}"

    kind = type(item).__name__ 
    return f"{item.get_item_id()} | {kind} | {item.get_item()} | {status}"