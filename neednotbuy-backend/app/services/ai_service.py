from app.schemas.ai import RequirementResponse


def analyze_requirement(query: str) -> RequirementResponse:

    query_lower = query.lower()

    # Temporary item detection
    known_items = [
        "projector",
        "camera",
        "laptop",
        "speaker",
        "luggage",
        "drill machine"
    ]

    item = None

    for known_item in known_items:
        if known_item in query_lower:
            item = known_item
            break

    return RequirementResponse(
        item=item or "unknown",
        duration_days=1,
        purpose=None,
        urgency=None
    )


# from app.schemas.ai import RequirementResponse

# def analyze_requirement(
#     item: str,
#     duration_days: int = 1,
#     purpose: str | None = None
# ) -> RequirementResponse:

#     return RequirementResponse(
#         item=item,
#         duration_days=duration_days,
#         purpose=purpose,
#         urgency=None
#     )


import json

from mistralai import Mistral

from app.core.config import settings
from app.schemas.ai import RequirementResponse


# Create Mistral client
client = Mistral(
    api_key=settings.MISTRAL_API_KEY
)


async def analyze_requirement(
    query: str
) -> RequirementResponse:

    prompt = f"""
You are a requirement extraction system.

Extract the user's requirement.

Return ONLY valid JSON.

Required format:

{{
    "item": "string",
    "duration_days": number,
    "purpose": "string or null",
    "urgency": "low, normal, or high"
}}

Rules:

- Extract only information supported by the user's request.
- Do not recommend an option.
- Do not invent prices.
- Do not invent availability.
- If duration is not mentioned, use 1.
- If purpose is not mentioned, use null.
- Return only valid JSON without markdown formatting.

User request:

{query}
"""

    response = client.chat.complete(
        model="mistral-small-2603",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    response_text = response.choices[0].message.content.strip()

    data = json.loads(response_text)

    return RequirementResponse(**data)