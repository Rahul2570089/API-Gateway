from app import users_pb2, users_pb2_grpc

class UserService(users_pb2_grpc.UserServiceServicer):
    def GetUser(self, request, context):
        # Mock user retrieval
        if request.user_id == 1:
            return users_pb2.GetUserResponse(user_id=1, name="John Doe")
        else:
            return users_pb2.GetUserResponse(user_id=0, name="Not Found")

    def CreateUser(self, request, context):
        # Mock user creation
        return users_pb2.CreateUserResponse(status="created")
