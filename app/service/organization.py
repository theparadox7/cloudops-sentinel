from sqlalchemy.orm import Session

from app.model.organization import Organization
from app.repository.organization import (
    create_organization as create_organization_repository,
    delete_organization as delete_organization_repository,
    get_organization_by_id as get_organization_by_id_repository,
    get_organizations as get_organizations_repository,
    update_organization as update_organization_repository,
)
from app.schema.organization import OrganizationCreate,OrganizationUpdate



def create_organization(
    db: Session,
    organization_data: OrganizationCreate,
) -> Organization:
    organization = Organization(
        name=organization_data.name,
    )

    return create_organization_repository(
        db,
        organization,
    )


def get_organizations(db: Session) -> list[Organization]:
    return get_organizations_repository(db)


def get_organization_by_id(
    db: Session,
    organization_id: int,
) -> Organization | None:
    return get_organization_by_id_repository(
        db,
        organization_id,
    )
    
def update_organization(
    db: Session,
    organization_id: int,
    organization_data: OrganizationUpdate,
) -> Organization | None:
    organization = get_organization_by_id_repository(
        db,
        organization_id,
    )

    if organization is None:
        return None

    if organization_data.name is not None:
        return update_organization_repository(
            db,
            organization,
            organization_data.name,
        )

    return organization

def delete_organization(
    db: Session,
    organization_id: int,
) -> bool:
    organization = get_organization_by_id_repository(
        db,
        organization_id,
    )

    if organization is None:
        return False

    delete_organization_repository(
        db,
        organization,
    )

    return True
