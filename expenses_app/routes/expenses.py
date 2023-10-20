from fastapi import APIRouter

expenses_api_router = APIRouter(prefix="expenses")

@expenses_api_router.get("/")
async def get_expenses():
    """Get all expenses"""
    return {}



