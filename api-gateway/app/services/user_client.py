import grpc
from ....microservices.users.app import users_pb2, users_pb2_grpc

def fetch_user(user_id: int):
    with grpc.insecure_channel("users-service:50051") as channel:
        stub = users_pb2_grpc.UserServiceStub(channel)
        response = stub.GetUser(users_pb2.GetUserRequest(user_id=user_id))
    return response

def create_user(name: str):
    with grpc.insecure_channel("users-service:50051") as channel:
        stub = users_pb2_grpc.UserServiceStub(channel)
        response = stub.CreateUser(users_pb2.CreateUserRequest(name=name))
    return response.status
