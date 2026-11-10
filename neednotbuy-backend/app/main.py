from fastapi import FastAPI

app = FastAPI(
    title="NeedNotBuy API",
    version="1.0.0"
)

@app.get("/")
def health_check():
    return{
        "message":"NeedNotBuy backend is running"
    }



#===============================================================
# import os
# from dotenv import load_dotenv
# from supabase import create_client

# load_dotenv()
# supabase = create_client(
#     os.environ["SUPABASE_URL"],
#     os.environ["SUPABASE_KEY"],
# )

# EMAIL="ak8257085@gmail.com"
# PASSWORD="Kumar@123"
# NAME="AJIT CHAURASIYA"


# try:
#     # Log in
#     res = supabase.auth.sign_in_with_password({
#         "email": EMAIL,
#         "password": PASSWORD,
#     })

# except Exception:
#     # Sign up (the trigger creates the profile row)
#     supabase.auth.sign_up({
#         "email": EMAIL,
#         "password": PASSWORD,
#         "options": {"data": {"name": NAME}},
#     })
#     res = supabase.auth.sign_in_with_password({
#         "email": EMAIL,
#         "password": PASSWORD,
#     })
# user = res.user

# # Fetch the profile
# profile = (
#     supabase.table("profiles")
#     .select("*")
#     .eq("id", user.id)
#     .maybe_single()
#     .execute()
# )
# print(profile.data)

# # Update the profile
# supabase.table("profiles").update({"name": NAME}).eq("id", user.id).execute()

# # Log out
# supabase.auth.sign_out()

from fastapi import FastAPI

from app.api.ai import router as ai_router


app = FastAPI(
    title="NeedNotBuy API",
    version="1.0.0"
)


app.include_router(ai_router)


@app.get("/")
def home():
    return {
        "message": "NeedNotBuy Backend Running"
    }


# =============================================================

from fastapi import FastAPI
from app.api.items import router as items_router

app = FastAPI(
    title="NeedNotBuy API"
)

app.include_router(items_router)


# ====================
from app.api.bookings import router as bookings_router
app.include_router(bookings_router)

from fastapi import FastAPI

from app.api.ai import router as ai_router
from app.api.items import router as items_router
from app.api.bookings import router as bookings_router


app = FastAPI(
    title="NeedNotBuy API",
    version="1.0.0"
)


app.include_router(ai_router)
app.include_router(items_router)
app.include_router(bookings_router)


@app.get("/")
def home():
    return {
        "message": "NeedNotBuy Backend Running"
    }




from app.api.payments import router as payments_router

app.include_router(payments_router)



#====================================================================================================
from fastapi import FastAPI

from app.api.ai import router as ai_router


app = FastAPI(
    title="NeedNotBuy API"
)


app.include_router(ai_router)




# =======================================

from fastapi import FastAPI

from app.api.router import api_router

app = FastAPI(
    title="NeedNotBuy API"
)

app.include_router(api_router)


@app.get("/")
async def root():

    return {
        "message": "NeedNotBuy backend running"
    }


from fastapi.middleware.cors import CORSMiddleware
app=FastAPI(
    title="NeedNotBuy API"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)