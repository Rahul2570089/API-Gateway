import grpc
from concurrent import futures
import pipelines_pb2
import pipelines_pb2_grpc
from app.services.pipeline_service import PipelineService

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    pipelines_pb2_grpc.add_PipelineServiceServicer_to_server(PipelineService(), server)
    server.add_insecure_port("[::]:50053")
    server.start()
    print("Pipeline microservice is running on port 50053...")
    server.wait_for_termination()

if __name__ == "__main__":
    serve()
