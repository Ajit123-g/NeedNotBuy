from pydantic import BaseModel, Field
from uuid import UUID

class CreareOrderRequest(BaseModel):
    booking_id: UUID



class CreateOrderRequest(BaseModel):
    booking_id: UUID
    paypal_order_id: str
    status: str
    amount: float = Field(gt=0)
    currency: str = "USD"