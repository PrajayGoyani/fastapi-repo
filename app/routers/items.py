from fastapi import APIRouter, Cookie, Depends, HTTPException, Header, status
from sqlalchemy.orm import Session
from app.services import item as item_service
from app.schemas.main import ItemResponse, ItemCreate, ItemResponse, ItemUpdate, ItemResponse
from app.database import get_db

router = APIRouter(
    prefix="/items",
    tags=["items"]
)

# Depends() used for injecting DB session object into handler function

# Create
@router.post("", response_model=ItemResponse, status_code=status.HTTP_201_CREATED)
def create_item(item: ItemCreate, db: Session = Depends(get_db)):
    return item_service.create_item(db=db, item=item) # named arguments passing

@router.get("") # response_model=list[ItemResponse]
def read_items(
    session_id: str | None = Cookie(default=None),
    user_agent: str | None = Header(default=None),
    skip: int = 0, limit: int = 100, db: Session = Depends(get_db)
):
    data = {"session": session_id, "agent": user_agent}
    items = item_service.get_items(db=db, skip=skip, limit=limit)

    return { "client_data": data, "data": items }

@router.get("/{item_id}", response_model=ItemResponse)
def read_item(item_id: int, db: Session = Depends(get_db)):
    db_item = item_service.get_item(db=db, item_id=item_id)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return db_item

@router.put("/{item_id}", response_model=ItemResponse)
def update_item(item_id: int, item: ItemUpdate, db: Session = Depends(get_db)):
    db_item = item_service.update_item(db=db, item_id=item_id, item=item)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return db_item

@router.delete("/{item_id}", response_model=ItemResponse)
def delete_item(item_id: int, db: Session = Depends(get_db)):
    db_item = item_service.delete_item(db=db, item_id=item_id)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return db_item
