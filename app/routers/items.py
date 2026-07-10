from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app import crud, schemas
from app.database import get_db

router = APIRouter(
    prefix="/items",
    tags=["items"]
)

# Depends() used for injecting DB session object into handler function

# Create
@router.post("", response_model=schemas.ItemResponse, status_code=status.HTTP_201_CREATED)
def create_item(item: schemas.ItemCreate, db: Session = Depends(get_db)):
    return crud.create_item(db=db, item=item) # named arguments passing

@router.get("", response_model=list[schemas.ItemResponse])
def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_items(db=db, skip=skip, limit=limit)

@router.get("/{item_id}", response_model=schemas.ItemResponse)
def read_item(item_id: int, db: Session = Depends(get_db)):
    db_item = crud.get_item(db=db, item_id=item_id)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return db_item

@router.put("/{item_id}", response_model=schemas.ItemResponse)
def update_item(item_id: int, item: schemas.ItemUpdate, db: Session = Depends(get_db)):
    db_item = crud.update_item(db=db, item_id=item_id, item=item)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return db_item

@router.delete("/{item_id}", response_model=schemas.ItemResponse)
def delete_item(item_id: int, db: Session = Depends(get_db)):
    db_item = crud.delete_item(db=db, item_id=item_id)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return db_item
