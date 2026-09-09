from sqlalchemy.orm import Session

from app.model.organization import Organization


def create_organization(
    db: Session,
    organization: Organization,
) -> Organization:
    db.add(organization)
    db.commit()
    db.refresh(organization)

    return organization

def get_organizations(db: Session) -> list[Organization]:
    return db.query(Organization).all()
def get_organization_by_id(
    db: Session,
    organization_id: int,
) -> Organization | None:
    return (
        db.query(Organization)
        .filter(Organization.id == organization_id)
        .first()
    )