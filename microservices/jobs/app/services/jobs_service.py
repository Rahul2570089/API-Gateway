from app import jobs_pb2, jobs_pb2_grpc

class JobService(jobs_pb2_grpc.JobServiceServicer):
    def GetJob(self, request, context):
        if request.job_id == 1:
            return jobs_pb2.GetJobResponse(job_id=1, status="Job Completed")
        return jobs_pb2.GetJobResponse(job_id=0, status="Job not found")

    def CreateJob(self, request, context):
        return jobs_pb2.CreateJobResponse(status="Job created successfully")
