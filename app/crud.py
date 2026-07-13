from sqlalchemy import select
from sqlalchemy.orm import Session
from app import models, schemas

def get_item(db: Session, item_id: int):
    return db.scalar(select(models.Item).where(models.Item.id == item_id))
    # return db.get(models.Item, item_id) # primary key lookup
    # return db.query(models.Item).filter(models.Item.id == item_id).first() #legacy

def get_items(db: Session, skip: int = 0, limit: int = 100):
    statement = select(models.Item).offset(skip).limit(limit)
    return db.scalars(statement).all()
    # return db.query(models.Item).offset(skip).limit(limit).all() #legacy

def create_item(db: Session, item: schemas.ItemCreate):
    # creation_data = item.model_dump()
    # if "name" in creation_data:
    #     creation_data["name"] = creation_data["name"].strip().title()
    # db_item = models.Item(**creation_data)

    # field mapping
    db_item = models.Item(
        name=item.name.strip().title(),
        price=item.price,
        is_offer=item.is_offer
    )
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

def update_item(db: Session, item_id: int, item: schemas.ItemUpdate):
    db_item = get_item(db, item_id)
    if db_item:
        # Automatic dynamic loop (Fast, but unsafe for custom mutations)
        # update_data = item.model_dump(exclude_unset=True)
        # for key, value in update_data.items():
        #     setattr(db_item, key, value)

        if item.name:
            db_item.name = item.name.strip().title()

        db_item.price = item.price
        db_item.is_offer = item.is_offer
        db.commit()
        db.refresh(db_item)
    return db_item

def delete_item(db: Session, item_id: int):
    db_item = get_item(db, item_id)
    if db_item:
        db.delete(db_item)
        db.commit()
    return db_item
