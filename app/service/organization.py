from sqlalchemy.orm import Session

from app.model.organization import Organization
from app.schema.organization import OrganizationCreate


def create_organization(
    db: Session,
    organization_data: OrganizationCreate,
) -> Organization:
    organization = Organization(
        name=organization_data.name,
    )

    db.add(organization)
    db.commit()
    db.refresh(organization)

    return organization