import grpc
from fastapi import APIRouter, HTTPException, Depends
from app.auth import verify_token
from app.services.job_client import create_job, get_job

router = APIRouter()

@router.post("/", dependencies=[Depends(verify_token)])
def create_job_route(job: dict):
    try:
        response = create_job(job)
        return {"status": response.status}
    except grpc.RpcError as e:
        raise HTTPException(status_code=500, detail=e.details())

@router.get("/{job_id}", dependencies=[Depends(verify_token)])
def get_job_route(job_id: int):
    try:
        response = get_job(job_id)
        return {"job_id": response.job_id, "status": response.status}
    except grpc.RpcError as e:
        raise HTTPException(status_code=500, detail=e.details())