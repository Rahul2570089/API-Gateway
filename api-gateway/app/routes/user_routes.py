import grpc
from fastapi import APIRouter, HTTPException
from services.user_client import create_user, get_user

router = APIRouter()

@router.post("/")
def create_user_route(user: dict):
    try:
        response = create_user(user)
        return {
            "message": response.message,
            "user": {"id": response.user.id, "name": response.user.name, "email": response.user.email}
        }
    except grpc.RpcError as e:
        raise HTTPException(status_code=e.code().value[0], detail=e.details())

@router.get("/{user_id}")
def get_user_route(user_id: int):
    try:
        response = get_user(user_id)
        return {"user": {"id": response.id, "name": response.name, "email": response.email}}
    except grpc.RpcError as e:
        raise HTTPException(status_code=e.code().value[0], detail=e.details())
