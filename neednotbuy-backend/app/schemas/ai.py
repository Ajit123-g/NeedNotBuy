from pydantic import BaseModel, Field
from typing import Optional


# Request from frontend
class AnalyzeRequest(BaseModel):
    query: str = Field(
        ...,
        min_length=3,
        description="User's natural language requirement"
    )


# Structured information extracted by AI
class RequirementResponse(BaseModel):
    item: str
    duration_days: int = 1
    purpose: Optional[str] = None
    urgency: Optional[str] = "normal"


# Option returned by recommendation system
class OptionResponse(BaseModel):
    item_id: str
    title: str
    type: str
    estimated_cost: float
    availability: bool
    score: float


# Final recommendation response
class RecommendationResponse(BaseModel):

    requirement: RequirementResponse

    recommendation_type: Optional[str] = None

    recommended_item: Optional[OptionResponse] = None

    reason: str

    alternatives: list[OptionResponse] = []








from pydantic import BaseModel, Field
from typing import Optional


class OptionResponse(BaseModel):

    item_id: str

    title: str

    type: str

    estimated_cost: float

    availability: bool

    score: float


class RecommendationResponse(BaseModel):

    requirement: RequirementResponse

    recommendation_type: Optional[str] = None

    recommended_item: Optional[OptionResponse] = None

    alternatives: list[OptionResponse] = Field(
        default_factory=list
    )

    reason: str