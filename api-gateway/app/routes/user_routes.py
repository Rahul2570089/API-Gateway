from fastapi import APIRouter, HTTPException
from app.services.user_client import fetch_user, create_user

router = APIRouter()

@router.get("/{user_id}")
async def get_user(user_id: int):
    user = fetch_user(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return {"user_id": user.user_id, "name": user.name}

@router.post("/")
async def create_new_user(name: str):
    status = create_user(name)
    return {"status": status}
