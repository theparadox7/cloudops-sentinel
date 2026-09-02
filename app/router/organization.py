from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.schema.organization import OrganizationCreate, OrganizationResponse
from app.service.organization import (
    create_organization,
    get_organizations,
)


router = APIRouter(
    prefix="/api/v1/organizations",
    tags=["Organizations"],
)


@router.post("/", response_model=OrganizationResponse)
def create_organization_endpoint(
    organization: OrganizationCreate,
    db: Session = Depends(get_db),
):
    return create_organization(
        db,
        organization,
    )


@router.get("/", response_model=list[OrganizationResponse])
def get_organizations_endpoint(
    db: Session = Depends(get_db),
):
    return get_organizations(db)