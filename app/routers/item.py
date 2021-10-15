from typing import Optional, List

from fastapi import status, HTTPException, Query, APIRouter

from app.models import Item

router = APIRouter(
    prefix='/item',
    tags=['items'],
)


@router.get('', response_model=List[Item], status_code=status.HTTP_200_OK)
async def get_items_list(
        id: Optional[int] = None,
        value: Optional[str] = None,
        timestamp: Optional[int] = None,
        offset: int = Query(0, ge=0),
        limit: int = Query(10, ge=1)
):
    items = Item.objects
    if id:
        items = items.filter(id=id)
    if value:
        items = items.filter(value__icontains=value)
    if timestamp:
        items = items.filter(timestamp=timestamp)
    return await items.offset(offset).limit(limit).all()


@router.post('', response_model=Item, status_code=status.HTTP_201_CREATED)
async def create_item(item: Item):
    if await Item.objects.filter(id=item.id).exists():
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f'item with id = {item.id} already in database')
    await item.save()
    return item


@router.put('', response_model=Item, status_code=status.HTTP_202_ACCEPTED)
async def get_item(item: Item):
    item_id = item.id
    item_db = await Item.objects.get_or_none(id=item_id)
    if item_db is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'item with id = {item_id} not found')
    return await item_db.update(**item.dict())
