from sqlalchemy.orm import Session

from db.models import Format
from api.schemas.format import FormatCreate


def get_all_formats(db: Session):
    return db.query(Format).all()


def get_format_by_id(db: Session, id: int):
    return db.query(Format).filter(Format.id == id).first()


def add_format(db: Session, format: FormatCreate):
    db_format = Format(type=format.type)
    db.add(db_format)
    db.commit()
    db.refresh(db_format)
    return db_format


def edit_format(db: Session, id: int, format_data: FormatCreate):
    db_format = get_format_by_id(id, id)
    if not db_format:
        return None
    db_format.type = format_data.type
    db.commit()
    db.refresh(db_format)
    return db_format


def remove_format(db: Session, id: int):
    db_format = get_format_by_id(id, db )
    if not db_format:
        return None
    db.delete(db_format)
    db.commit()
    return db_format
