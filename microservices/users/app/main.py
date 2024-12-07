import grpc
from concurrent import futures
import users_pb2
import users_pb2_grpc
from services.users_service import UserService

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    users_pb2_grpc.add_UserServiceServicer_to_server(UserService(), server)
    server.add_insecure_port("[::]:50051")
    server.start()
    print("Users Microservice is successfully running on port 50051...")
    server.wait_for_termination()

if __name__ == "__main__":
    serve()
