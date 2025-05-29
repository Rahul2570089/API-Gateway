import grpc
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '../../../microservices/jobs/app'))

from microservices.jobs.app import jobs_pb2, jobs_pb2_grpc

def create_job(job_data):
    with grpc.insecure_channel(os.getenv("JOBS_SERVICE_URL")) as channel:
        stub = jobs_pb2_grpc.JobServiceStub(channel)
        request = jobs_pb2.CreateJobRequest(job_name=job_data.get("job_name", ""))
        response = stub.CreateJob(request)
    return response

def get_job(job_id):
    with grpc.insecure_channel(os.getenv("JOBS_SERVICE_URL")) as channel:
        stub = jobs_pb2_grpc.JobServiceStub(channel)
        request = jobs_pb2.GetJobRequest(job_id=job_id)
        response = stub.GetJob(request)
    return response