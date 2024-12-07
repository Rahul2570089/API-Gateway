from app import pipelines_pb2, pipelines_pb2_grpc

class PipelineService(pipelines_pb2_grpc.PipelineServiceServicer):
    def GetPipeline(self, request, context):
        if request.pipeline_id == 1:
            return pipelines_pb2.GetPipelineResponse(pipeline_id=1, status="Pipeline Running")
        return pipelines_pb2.GetPipelineResponse(pipeline_id=0, status="Pipeline not found")

    def CreatePipeline(self, request, context):
        return pipelines_pb2.CreatePipelineResponse(status="Pipeline created successfully")
