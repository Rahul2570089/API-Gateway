import grpc
from concurrent import futures
import jobs_pb2
import jobs_pb2_grpc
from services.jobs_service import JobService

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    jobs_pb2_grpc.add_JobServiceServicer_to_server(JobService(), server)
    server.add_insecure_port("[::]:50052")
    server.start()
    print("Jobs microservice is running on port 50052...")
    server.wait_for_termination()

if __name__ == "__main__":
    serve()
