from models.schemas import Item, ItemInput, ItemUpdate
from typing import List, Dict

fake_db: Dict[int, Item] = { 1: Item(id=1, name="milk", price=3.5, link=None) }
fake_id_counter = 2

async def retrieve_all() -> List[Item]:
    # get from postgres database
    retrieved: List[Item] = list(fake_db.values())
    return retrieved

async def create_item(item: ItemInput) -> Item:
    # insert into postgres database and have database return object and also assign an id (uuid)
    global fake_id_counter
    created = Item(
        id =fake_id_counter,
        name=item.name,
        price=item.price,
        link=item.link,
    )
    fake_db[fake_id_counter] = created
    fake_id_counter += 1
    return created

async def update_item(item_id: int, item_body: ItemUpdate) -> Item:
    # update item in postgres database and return updated object
    existing = fake_db.get(item_id)
    if not existing:
        return None
    updated = Item(
        id=item_id,
        name=item_body.name if item_body.name is not None else existing.name,
        price=item_body.price if item_body.price is not None else existing.price,
        link=item_body.link if item_body.link is not None else existing.link,
    )
    fake_db[item_id] = updated
    return updated