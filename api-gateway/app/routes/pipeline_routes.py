import grpc
from fastapi import APIRouter, HTTPException, Depends
from app.auth import verify_token
from app.services.pipeline_client import create_pipeline, get_pipeline

router = APIRouter()

@router.post("/", dependencies=[Depends(verify_token)])
def create_pipeline_route(pipeline: dict):
    try:
        response = create_pipeline(pipeline)
        return {"status": response.status}
    except grpc.RpcError as e:
        raise HTTPException(status_code=500, detail=e.details())

@router.get("/{pipeline_id}", dependencies=[Depends(verify_token)])
def get_pipeline_route(pipeline_id: int):
    try:
        response = get_pipeline(pipeline_id)
        return {"pipeline_id": response.pipeline_id, "status": response.status}
    except grpc.RpcError as e:
        raise HTTPException(status_code=500, detail=e.details())