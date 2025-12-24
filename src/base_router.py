from src.notifications.router import router as notifications_router

from fastapi import APIRouter


main_router = APIRouter()

main_router.include_router(notifications_router)