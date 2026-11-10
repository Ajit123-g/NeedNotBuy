from fastapi import APIRouter

from app.api import payments

api_router = APIRouter()

api_router.include_router(
    payments.router
)


api_router.include_router(payments.router)