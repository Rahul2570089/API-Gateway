import grpc
from microservices.users.app import users_pb2, users_pb2_grpc

def create_user(user_data):
    with grpc.insecure_channel("localhost:50051") as channel:
        stub = users_pb2_grpc.UserServiceStub(channel)
        request = users_pb2.User(**user_data)
        response = stub.CreateUser(request)
    return response

def get_user(user_id):
    with grpc.insecure_channel("localhost:50051") as channel:
        stub = users_pb2_grpc.UserServiceStub(channel)
        request = users_pb2.UserId(id=user_id)
        response = stub.GetUser(request)
    return response
