import grpc
from microservices.users.app import users_pb2, users_pb2_grpc

users_db = {}

class UserService(users_pb2_grpc.UserServiceServicer):
    def CreateUser(self, request, context):
        if request.id in users_db:
            context.abort(grpc.StatusCode.ALREADY_EXISTS, "User already exists")
        user = {"id": request.id, "name": request.name, "email": request.email}
        users_db[request.id] = user
        return users_pb2.CreateUserResponse(message="User created successfully", user=users_pb2.User(**user))

    def GetUser(self, request, context):
        user = users_db.get(request.id)
        if not user:
            context.abort(grpc.StatusCode.NOT_FOUND, "User not found")
        return users_pb2.User(**user)
