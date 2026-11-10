from fastapi import APIRouter, HTTPException
from app.database.supabase_client import supabase
from app.schemas.booking import BookingCreate

router=APIRouter(
    prefix="/api/bookings",
    tags=["Bookings"]
)

@router.post("/", status_code=201)
def create_booking(
    booking: BookingCreate,
    user_id: str
):

    # Step 1: Get item from database

    item_response = (
        supabase
        .table("items")
        .select("*")
        .eq("id", str(booking.item_id))
        .execute()
    )

    if not item_response.data:
        raise HTTPException(
            status_code=404,
            detail="Item not found"
        )

    item = item_response.data[0]


    # Step 2: Check item availability

    if not item["availability"]:
        raise HTTPException(
            status_code=400,
            detail="Item is not available"
        )


    # Step 3: Validate booking dates

    if booking.end_date <= booking.start_date:
        raise HTTPException(
            status_code=400,
            detail="End date must be after start date"
        )


    # Step 4: Calculate duration

    duration_days = (
        booking.end_date - booking.start_date
    ).days


    # Step 5: Calculate total amount

    total_amount = float(item["price"]) * duration_days


    # Step 6: Prepare booking data

    booking_data = {

        "user_id": user_id,

        "item_id": str(booking.item_id),

        "start_date": booking.start_date.isoformat(),

        "end_date": booking.end_date.isoformat(),

        "total_amount": total_amount,

        "status": "pending",

        "payment_status": "pending"

    }


    # Step 7: Insert booking into Supabase

    response = (
        supabase
        .table("bookings")
        .insert(booking_data)
        .execute()
    )


    # Step 8: Return response

    return response.data[0]

#===================
# getting booking id
@router.get("/{booking_id}")
def get_booking(booking_id: str):

    response = (
        supabase
        .table("bookings")
        .select("*")
        .eq("id", booking_id)
        .execute()
    )

    if not response.data:
        raise HTTPException(
            status_code=404,
            detail="Booking not found"
        )

    return response.data[0]

# ===================
# All booking id
@router.get("/user/{user_id}")
def get_user_bookings(user_id: str):

    response = (
        supabase
        .table("bookings")
        .select("*")
        .eq("user_id", user_id)
        .execute()
    )

    return response.data