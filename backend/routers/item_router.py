from fastapi import APIRouter, Path, Body, HTTPException
from models.schemas import Item, ItemInput, ItemUpdate, ItemsResponse
from services.item_service import retrieve_all, create_item, update_item
from typing import List

router = APIRouter(
    prefix="/items",
    tags=["items"],
)

@router.get(
        "", 
        response_model=ItemsResponse, 
        summary="list all items",
        status_code=200,)
async def get_items():
    try:
        items: List[Item] = await retrieve_all()
        return ItemsResponse(count=len(items), items=items)
    except Exception as e:
        raise HTTPException(status_code=502, detail=f"API error:{e}")
    
@router.post(
    "", 
    response_model=Item, 
    summary="create a new item", 
    status_code=201,)
async def create_new_item(item: ItemInput = Body(...)): # requires body
    try:
        new_item = await create_item(item)
        return new_item
    except Exception as e:
        raise HTTPException(status_code=502, detail=f"API error:{e}")
    
@router.patch(
    "/{item_id}",
    response_model=Item,
    summary="update an item",
    status_code=200,
)
async def patch_item(item_id: int = Path(...), item_body: ItemUpdate = Body(...)
):
    try:
        updated_item = await update_item(item_id, item_body)
        if not updated_item:
            raise HTTPException(status_code=404, detail="Item not found")
        return updated_item
    except Exception as e:
        raise HTTPException(status_code=502, detail=f"API error:{e}")