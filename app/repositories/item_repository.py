items = [
    {"id": 1, "name": "Laptop ThinkPad",
     "price": 12500000, "category_id": 1},

    {"id": 2, "name": "Mouse Wireless",
     "price": 250000, "category_id": 2},

    {"id": 3, "name": "Keyboard Mechanical",
     "price": 750000, "category_id": 2},

    {"id": 4, "name": "Laut Bercerita",
     "price": 100000, "category_id": 3},

    {"id": 5, "name": "Dikta & Hukum",
     "price": 95000, "category_id": 3},

    {"id": 6, "name": "Monitor LG 24 Inch",
     "price": 2100000, "category_id": 1}
]


def get_all():
    return items


def get_by_id(item_id):
    for item in items:
        if item["id"] == item_id:
            return item
    return None


def create(name, price, category_id):
    new_id = max(
        [i["id"] for i in items], default=0
    ) + 1

    item = {
        "id": new_id,
        "name": name,
        "price": price,
        "category_id": category_id
    }

    items.append(item)
    return item


def update(item_id, data):
    item = get_by_id(item_id)

    if item:
        item.update(data)

    return item


def delete(item_id):
    item = get_by_id(item_id)

    if item:
        items.remove(item)
        return True

    return False