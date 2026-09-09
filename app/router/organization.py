from fastapi import APIRouter, Depends,HTTPException,status
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.schema.organization import OrganizationCreate, OrganizationResponse,OrganizationUpdate
from app.service.organization import (
    create_organization,
    delete_organization,
    get_organization_by_id,
    get_organizations,
    update_organization,
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

@router.get("/{organization_id}", response_model=OrganizationResponse)
def get_organization_by_id_endpoint(
    organization_id: int,
    db: Session = Depends(get_db),
):
    organization = get_organization_by_id(
        db,
        organization_id,
    )

    if organization is None:
        raise HTTPException(
            status_code=404,
            detail="Organization not found",
        )

    return organization

@router.patch("/{organization_id}", response_model=OrganizationResponse)
def update_organization_endpoint(
    organization_id: int,
    organization_data: OrganizationUpdate,
    db: Session = Depends(get_db),
):
    organization = update_organization(
        db,
        organization_id,
        organization_data,
    )

    if organization is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Organization not found",
        )

    return organization

@router.delete("/{organization_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_organization_endpoint(
    organization_id: int,
    db: Session = Depends(get_db),
):
    deleted = delete_organization(
        db,
        organization_id,
    )

    if not deleted:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Organization not found",
        )
        
