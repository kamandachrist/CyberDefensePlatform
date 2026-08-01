from sqlalchemy.orm import Session

from fastapi import APIRouter, Depends, HTTPException, status

from app.database.session import get_db
from app.schemas.vulnerability import (
    VulnerabilityCreate,
    VulnerabilityResponse,
    VulnerabilityUpdate,
)
from app.services.vulnerability_service import (
    create_new_vulnerability,
    list_vulnerabilities,
    retrieve_vulnerability,
    update_existing_vulnerability,
    remove_vulnerability,
)

router = APIRouter(
    prefix="/vulnerabilities",
    tags=["Vulnerabilities"],
)


@router.post(
    "/",
    response_model=VulnerabilityResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_vulnerability(
    vulnerability: VulnerabilityCreate,
    db: Session = Depends(get_db),
):
    return create_new_vulnerability(
        db,
        vulnerability,
    )


@router.get(
    "/",
    response_model=list[VulnerabilityResponse],
)
def get_vulnerabilities(
    db: Session = Depends(get_db),
):
    return list_vulnerabilities(db)


@router.get(
    "/{vulnerability_id}",
    response_model=VulnerabilityResponse,
)
def get_vulnerability(
    vulnerability_id: int,
    db: Session = Depends(get_db),
):
    vulnerability = retrieve_vulnerability(
        db,
        vulnerability_id,
    )

    if not vulnerability:
        raise HTTPException(
            status_code=404,
            detail="Vulnerability not found",
        )

    return vulnerability


@router.put(
    "/{vulnerability_id}",
    response_model=VulnerabilityResponse,
)
def update_vulnerability(
    vulnerability_id: int,
    vulnerability_data: VulnerabilityUpdate,
    db: Session = Depends(get_db),
):
    vulnerability = update_existing_vulnerability(
        db,
        vulnerability_id,
        vulnerability_data,
    )

    if not vulnerability:
        raise HTTPException(
            status_code=404,
            detail="Vulnerability not found",
        )

    return vulnerability


@router.delete(
    "/{vulnerability_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
def delete_vulnerability(
    vulnerability_id: int,
    db: Session = Depends(get_db),
):
    vulnerability = remove_vulnerability(
        db,
        vulnerability_id,
    )

    if not vulnerability:
        raise HTTPException(
            status_code=404,
            detail="Vulnerability not found",
        )