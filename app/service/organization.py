from sqlalchemy.orm import Session

from app.model.organization import Organization
from app.repository.organization import (
    create_organization as create_organization_repository,
    get_organization_by_id as get_organization_by_id_repository,
    get_organizations as get_organizations_repository,
)
from app.schema.organization import OrganizationCreate



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