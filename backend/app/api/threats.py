from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.database.session import get_db

from app.schemas.threat import (
    ThreatCreate,
    ThreatResponse,
    ThreatUpdate,
)

from app.services.threat_service import (
    create_new_threat,
    list_threats,
    retrieve_threat,
    update_existing_threat,
    remove_threat,
)


router = APIRouter(
    prefix="/threats",
    tags=["Threats"],
)


@router.post(
    "/",
    response_model=ThreatResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_threat_endpoint(
    threat: ThreatCreate,
    db: Session = Depends(get_db),
):
    return create_new_threat(
        db,
        threat,
    )


@router.get(
    "/",
    response_model=list[ThreatResponse],
)
def get_threats_endpoint(
    db: Session = Depends(get_db),
):
    return list_threats(db)


@router.get(
    "/{threat_id}",
    response_model=ThreatResponse,
)
def get_threat_endpoint(
    threat_id: int,
    db: Session = Depends(get_db),
):
    threat = retrieve_threat(
        db,
        threat_id,
    )

    if not threat:
        raise HTTPException(
            status_code=404,
            detail="Threat not found",
        )

    return threat


@router.put(
    "/{threat_id}",
    response_model=ThreatResponse,
)
def update_threat_endpoint(
    threat_id: int,
    threat_data: ThreatUpdate,
    db: Session = Depends(get_db),
):
    threat = update_existing_threat(
        db,
        threat_id,
        threat_data,
    )

    if not threat:
        raise HTTPException(
            status_code=404,
            detail="Threat not found",
        )

    return threat


@router.delete(
    "/{threat_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
def delete_threat_endpoint(
    threat_id: int,
    db: Session = Depends(get_db),
):
    threat = remove_threat(
        db,
        threat_id,
    )

    if not threat:
        raise HTTPException(
            status_code=404,
            detail="Threat not found",
        )

    return None
