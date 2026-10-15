from app.repositories import category_repository
from app.repositories import item_repository as repo


def get_all():
    return repo.get_all()


def get_by_id(item_id):
    return repo.get_by_id(item_id)


def validate(data, partial=False):
    if not isinstance(data, dict):
        return None, "Data JSON wajib berupa objek"

    if not partial:
        for field in ["name", "price", "category_id"]:
            if field not in data:
                return None, f"Field {field} wajib diisi"

    result = {}

    if "name" in data:
        name = data["name"]

        if not isinstance(name, str) or not name.strip():
            return None, "Nama barang wajib diisi"

        result["name"] = name.strip()

    if "price" in data:
        price = data["price"]

        if type(price) is not int or price < 0:
            return None, "Harga harus berupa bilangan bulat nonnegatif"

        result["price"] = price

    if "category_id" in data:
        category_id = data["category_id"]

        if type(category_id) is not int or category_id <= 0:
            return None, "category_id harus berupa bilangan bulat positif"

        category = category_repository.get_by_id(category_id)

        if category is None:
            return None, "Kategori tidak ditemukan"

        result["category_id"] = category_id

    return result, None


def create(data):
    values, error = validate(data)

    if error:
        return None, error

    item = repo.create(
        values["name"],
        values["price"],
        values["category_id"]
    )

    return item, None


def update(item_id, data):
    if repo.get_by_id(item_id) is None:
        return None, "Barang tidak ditemukan"

    values, error = validate(data, partial=True)

    if error:
        return None, error

    if not values:
        return None, "Minimal satu field harus diperbarui"

    return repo.update(item_id, values), None


def delete(item_id):
    if repo.get_by_id(item_id) is None:
        return False

    return repo.delete(item_id)
