from pydantic import BaseModel, Field


class RiskFactor(BaseModel):
    name: str
    score: float
    weight: float
    contribution: float


class AssetRiskResponse(BaseModel):
    asset_id: int
    hostname: str

    risk_score: float = Field(
        ge=0,
        le=100,
    )

    risk_level: str

    vulnerability_score: float = Field(
        ge=0,
        le=100,
    )

    incident_score: float = Field(
        ge=0,
        le=100,
    )

    asset_criticality_score: float = Field(
        ge=0,
        le=100,
    )

    risk_factors: list[RiskFactor]
