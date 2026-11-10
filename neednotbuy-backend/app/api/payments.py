from fastapi import APIRouter, HTTPException

from app.database.supabase_client import supabase

from app.schemas.payment import CreateOrderRequest

from app.services.paypal_service import (
    create_paypal_order,
    capture_paypal_order
)


router = APIRouter(
    prefix="/api/payments",
    tags=["Payments"]
)




@router.post("/create-order")
async def create_order(request: CreateOrderRequest):

    # STEP 1: Get booking from Supabase

    booking_response = (
        supabase
        .table("bookings")
        .select("*")
        .eq("id", str(request.booking_id))
        .execute()
    )

    if not booking_response.data:

        raise HTTPException(
            status_code=404,
            detail="Booking not found"
        )

    booking = booking_response.data[0]


    # STEP 2: Check booking status

    if booking["status"] != "pending":

        raise HTTPException(
            status_code=400,
            detail="Booking is not pending"
        )


    # STEP 3: Check payment status

    if booking["payment_status"] == "completed":

        raise HTTPException(
            status_code=400,
            detail="Booking already paid"
        )


    # STEP 4: Get amount from database

    amount = str(booking["total_amount"])


    # STEP 5: Create PayPal order

    paypal_order = await create_paypal_order(

        amount=amount,

        currency="USD",

        booking_id=str(request.booking_id)

    )


    # STEP 6: Get PayPal Order ID

    order_id = paypal_order["id"]


    # STEP 7: Save payment information in Supabase

    payment_data = {

        "booking_id": str(request.booking_id),

        "paypal_order_id": order_id,

        "amount": amount,

        "currency": "USD",

        "status": "created"

    }


    supabase.table("payments").insert(
        payment_data
    ).execute()


    # STEP 8: Return Order ID to frontend

    return {

        "message": "PayPal order created successfully",

        "paypal_order_id": order_id,

        "approval_url": next(
            (
                link["href"]
                for link in paypal_order.get("links", [])
                if link["rel"] == "approve"
            ),
            None
        )

    }









@router.post("/capture-order/{order_id}")
async def capture_order(order_id: str):

    # STEP 1: Find payment record

    payment_response = (
        supabase
        .table("payments")
        .select("*")
        .eq("paypal_order_id", order_id)
        .execute()
    )

    if not payment_response.data:

        raise HTTPException(
            status_code=404,
            detail="Payment record not found"
        )

    payment = payment_response.data[0]


    # STEP 2: Check if already completed

    if payment["status"] == "completed":

        raise HTTPException(
            status_code=400,
            detail="Payment already completed"
        )


    # STEP 3: Capture payment through PayPal

    paypal_response = await capture_paypal_order(
        order_id
    )


    # STEP 4: Verify PayPal response

    if paypal_response.get("status") != "COMPLETED":

        raise HTTPException(
            status_code=400,
            detail="Payment not completed"
        )


    # STEP 5: Update payment status

    supabase.table("payments").update({

        "status": "completed"

    }).eq(
        "paypal_order_id", order_id
    ).execute()


    # STEP 6: Update booking status

    supabase.table("bookings").update({

        "status": "confirmed",

        "payment_status": "completed"

    }).eq(
        "id", payment["booking_id"]
    ).execute()


    return {

        "message": "Payment completed successfully",

        "order_id": order_id,

        "booking_id": payment["booking_id"],

        "payment_status": "completed",

        "booking_status": "confirmed"

    }



# Temprory not include in final project
from fastapi import APIRouter, HTTPException

from app.schemas.payment import (
    CreateOrderRequest,
    CreateOrderResponse
)

from app.services.paypal_service import (
    create_paypal_order
)

router = APIRouter(
    prefix="/api/payments",
    tags=["Payments"]
)


@router.post(
    "/create-order",
    response_model=CreateOrderResponse
)
async def create_order(
    request: CreateOrderRequest
):

    # TEMPORARY TEST VALUES
    # Replace these with booking data from Supabase.

    amount = "10.00"
    currency = "USD"

    booking_id = str(request.booking_id)

    paypal_response = await create_paypal_order(
        amount=amount,
        currency=currency,
        booking_id=booking_id
    )

    paypal_order_id = paypal_response.get("id")

    if not paypal_order_id:
        raise HTTPException(
            status_code=502,
            detail="PayPal did not return an order ID."
        )

    return CreateOrderResponse(
        booking_id=request.booking_id,
        paypal_order_id=paypal_order_id,
        status=paypal_response.get("status", "CREATED")
    )