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