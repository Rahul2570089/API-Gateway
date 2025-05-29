import grpc
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '../../../microservices/pipeline/app'))

from microservices.pipeline.app import pipelines_pb2, pipelines_pb2_grpc

def create_pipeline(pipeline_data):
    with grpc.insecure_channel(os.getenv("PIEPLINE_SERVICE_URL")) as channel:
        stub = pipelines_pb2_grpc.PipelineServiceStub(channel)
        request = pipelines_pb2.CreatePipelineRequest(pipeline_name=pipeline_data.get("pipeline_name", ""))
        response = stub.CreatePipeline(request)
    return response

def get_pipeline(pipeline_id):
    with grpc.insecure_channel(os.getenv("PIPELINE_SERVICE_URL")) as channel:
        stub = pipelines_pb2_grpc.PipelineServiceStub(channel)
        request = pipelines_pb2.GetPipelineRequest(pipeline_id=pipeline_id)
        response = stub.GetPipeline(request)
    return response