from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database import get_db
from app import models, schemas
from app.auth import get_current_user

router = APIRouter(prefix="/companies", tags=["Companies"])


@router.post("/", response_model=schemas.CompanyResponse, status_code=status.HTTP_201_CREATED)
def create_company(
    company: schemas.CompanyCreate,
    db: Session = Depends(get_db)
):
    existing = db.query(models.Company).filter(
        models.Company.name == company.name
    ).first()
    if existing:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Company already exists"
        )

    new_company = models.Company(**company.model_dump())
    db.add(new_company)
    db.commit()
    db.refresh(new_company)
    return new_company


@router.get("/", response_model=list[schemas.CompanyResponse])
def get_companies(db: Session = Depends(get_db)):
    return db.query(models.Company).all()