from fastapi import APIRouter

from app.schemas.ai import (
    AnalyzeRequest,
    RequirementResponse
)

from app.services.ai_service import analyze_requirement


router = APIRouter(
    prefix="/api/ai",
    tags=["AI"]
)


@router.post(
    "/analyze",
    response_model=RequirementResponse
)
def analyze(request: AnalyzeRequest):

    result = analyze_requirement(request.query)

    return result

#=====================================================================================================
from fastapi import APIRouter, HTTPException

from app.schemas.ai import (
    AnalyzeRequest,
    RequirementResponse
)

from app.services.ai_service import (
    analyze_requirement
)


router = APIRouter(
    prefix="/api/ai",
    tags=["AI"]
)


@router.post(
    "/analyze",
    response_model=RequirementResponse
)
async def analyze(
    request: AnalyzeRequest
):

    try:

        result = await analyze_requirement(
            request.query
        )

        return result

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=f"AI analysis failed: {str(e)}"
        )



    


#============================================================================================
from app.schemas.ai import (
    AnalyzeRequest,
    RequirementResponse,
    RecommendationResponse
)

from app.services.ai_service import analyze_requirement

from app.services.recommendation_service import generate_recommendation

@router.post(
    "/recommend",
    response_model=RecommendationResponse
)
async def recommend(
    request: AnalyzeRequest
):

    # STEP 1: Extract requirement using real LLM

    requirement = await analyze_requirement(
        request.query
    )

    # STEP 2: Search database and generate recommendation

    result = generate_recommendation(
        requirement
    )

    # STEP 3: Return final response

    return {
        "requirement": requirement,
        **result
    }