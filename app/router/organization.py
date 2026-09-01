from fastapi import APIRouter

from app.schema.organization import OrganizationCreate, OrganizationResponse


router = APIRouter(
    prefix="/api/v1/organizations",
    tags=["Organizations"],
)


@router.post("/", response_model=OrganizationResponse)
def create_organization(organization: OrganizationCreate):
    return organization