# Microservices Architecture with API Gateway

A distributed microservices architecture built with FastAPI, gRPC, and Kubernetes, featuring an API Gateway that routes requests to multiple backend services.

## Architecture Overview

```
┌─────────────────┐    ┌─────────────────┐
│   API Gateway   │    │   Load Balancer │
│   (FastAPI)     │◄───┤   (Kubernetes)  │
│   Port: 8000    │    │                 │
└─────────┬───────┘    └─────────────────┘
          │
          ├─────────────────────────────────┐
          │                                 │
          ▼                                 ▼
┌─────────────────┐              ┌─────────────────┐
│  Users Service  │              │  Jobs Service   │
│    (gRPC)       │              │    (gRPC)       │
│  Port: 50051    │              │  Port: 50052    │
└─────────────────┘              └─────────────────┘
          │
          ▼
┌─────────────────┐
│Pipeline Service │
│    (gRPC)       │
│  Port: 50053    │
└─────────────────┘
```

## Services Overview

### API Gateway
- **Technology**: FastAPI with JWT authentication
- **Port**: 8000
- **Purpose**: Routes HTTP requests to appropriate microservices via gRPC
- **Features**:
  - JWT token-based authentication
  - Request routing and load balancing
  - Error handling and response formatting
  - Health checks and monitoring

### Users Service
- **Technology**: gRPC with Protocol Buffers
- **Port**: 50051
- **Purpose**: Manages user data and operations
- **Endpoints**:
  - `CreateUser`: Create new users
  - `GetUser`: Retrieve user information

### Jobs Service
- **Technology**: gRPC with Protocol Buffers
- **Port**: 50052
- **Purpose**: Handles job management and processing
- **Endpoints**:
  - `CreateJob`: Create new jobs
  - `GetJob`: Retrieve job status and information

### Pipeline Service
- **Technology**: gRPC with Protocol Buffers
- **Port**: 50053
- **Purpose**: Manages data pipelines and workflows
- **Endpoints**:
  - `CreatePipeline`: Create new pipelines
  - `GetPipeline`: Retrieve pipeline status and information

## Prerequisites

- Docker and Docker Compose
- Kubernetes cluster (minikube, kind, or cloud provider)
- kubectl CLI tool
- Python 3.9+ (for local development)

## Quick Start

### 1. Clone the Repository

```bash
git clone <repository-url>
cd microservices-architecture
```

### 2. Build Docker Images

```bash
# Build API Gateway
docker build -t api-gateway:latest ./api-gateway

# Build Users Service
docker build -t users-service:latest ./microservices/users

# Build Jobs Service
docker build -t jobs-service:latest ./microservices/jobs

# Build Pipeline Service
docker build -t pipeline-service:latest ./microservices/pipeline
```

### 3. Deploy to Kubernetes

```bash
# Create namespace
kubectl create namespace microservices

# Create JWT secret
kubectl create secret generic jwt-secret \
  --from-literal=JWT_SECRET_KEY=your-secret-key-here \
  --from-literal=JWT_ALGORITHM=HS256 \
  --from-literal=JWT_EXPIRE_MINUTES=30 \
  -n microservices

# Deploy services
kubectl apply -f microservices/users/k8s/
kubectl apply -f microservices/jobs/k8s/
kubectl apply -f microservices/pipeline/k8s/

# Deploy API Gateway
kubectl apply -f api-gateway/k8s/
```

### 4. Access the API

```bash
# Get the API Gateway external IP
kubectl get service api-gateway -n microservices

# Or use port forwarding for local access
kubectl port-forward service/api-gateway 8000:80 -n microservices
```

## API Usage

### Authentication

First, obtain a JWT token:

```bash
curl -X POST http://localhost:8000/login \
  -H "Content-Type: application/json" \
  -d '{"username": "admin", "password": "secret"}'
```

Response:
```json
{
  "access_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9...",
  "token_type": "bearer"
}
```

### API Endpoints

#### Users Service (via API Gateway)

**Create User:**
```bash
curl -X POST http://localhost:8000/users/ \
  -H "Authorization: Bearer YOUR_JWT_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"id": 1, "name": "John Doe", "email": "john@example.com"}'
```

**Get User:**
```bash
curl -X GET http://localhost:8000/users/1 \
  -H "Authorization: Bearer YOUR_JWT_TOKEN"
```

#### Jobs Service (via API Gateway)

**Create Job:**
```bash
curl -X POST http://localhost:8000/jobs/ \
  -H "Authorization: Bearer YOUR_JWT_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"job_name": "Data Processing Job"}'
```

**Get Job:**
```bash
curl -X GET http://localhost:8000/jobs/1 \
  -H "Authorization: Bearer YOUR_JWT_TOKEN"
```

#### Pipeline Service (via API Gateway)

**Create Pipeline:**
```bash
curl -X POST http://localhost:8000/pipelines/ \
  -H "Authorization: Bearer YOUR_JWT_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"pipeline_name": "ML Training Pipeline"}'
```

**Get Pipeline:**
```bash
curl -X GET http://localhost:8000/pipelines/1 \
  -H "Authorization: Bearer YOUR_JWT_TOKEN"
```

## Local Development

### Running Services Locally

1. **Start Users Service:**
```bash
cd microservices/users
pip install -r requirements.txt
python app/main.py
```

2. **Start Jobs Service:**
```bash
cd microservices/jobs
pip install -r requirements.txt
python app/main.py
```

3. **Start Pipeline Service:**
```bash
cd microservices/pipeline
pip install -r requirements.txt
python app/main.py
```

4. **Start API Gateway:**
```bash
cd api-gateway
pip install -r requirements.txt

# Set environment variables
export JWT_SECRET_KEY=your-secret-key-here
export JWT_ALGORITHM=HS256
export JWT_EXPIRE_MINUTES=30
export USER_SERVICE_URL=localhost:50051
export JOBS_SERVICE_URL=localhost:50052
export PIPELINE_SERVICE_URL=localhost:50053

python -m uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
```

### Generating Protocol Buffers

If you modify the `.proto` files, regenerate the Python files:

```bash
# For Users Service
cd microservices/users/app
python -m grpc_tools.protoc --python_out=. --grpc_python_out=. users.proto

# For Jobs Service
cd microservices/jobs/app
python -m grpc_tools.protoc --python_out=. --grpc_python_out=. jobs.proto

# For Pipeline Service
cd microservices/pipeline/app
python -m grpc_tools.protoc --python_out=. --grpc_python_out=. pipelines.proto
```

## Configuration

### Environment Variables

**API Gateway:**
- `JWT_SECRET_KEY`: Secret key for JWT token signing
- `JWT_ALGORITHM`: JWT signing algorithm (default: HS256)
- `JWT_EXPIRE_MINUTES`: Token expiration time in minutes
- `USER_SERVICE_URL`: Users service gRPC endpoint
- `JOBS_SERVICE_URL`: Jobs service gRPC endpoint
- `PIPELINE_SERVICE_URL`: Pipeline service gRPC endpoint

### Kubernetes Resources

Each service includes:
- **Deployment**: Defines the container specifications and replicas
- **Service**: Exposes the service within the cluster
- **Ingress**: (API Gateway only) External access configuration

## Monitoring and Health Checks

### Health Endpoints

- **API Gateway**: `GET /` - Returns service status
- **gRPC Services**: TCP socket health checks on respective ports

### Kubernetes Probes

All services include:
- **Liveness Probe**: Checks if the container is running
- **Readiness Probe**: Checks if the service is ready to accept traffic

## Troubleshooting

### Common Issues

1. **Import Errors in gRPC Services:**
   - Ensure the Python path includes the correct directories
   - Check that all `_pb2.py` files are properly generated

2. **Authentication Issues:**
   - Verify JWT secret is correctly set in Kubernetes secrets
   - Check token expiration time

3. **Service Discovery Issues:**
   - Ensure all services are running and accessible
   - Check Kubernetes service DNS resolution

### Debugging

1. **Check Pod Status:**
```bash
kubectl get pods -n microservices
kubectl describe pod <pod-name> -n microservices
```

2. **View Logs:**
```bash
kubectl logs <pod-name> -n microservices
```

3. **Test Service Connectivity:**
```bash
kubectl exec -it <pod-name> -n microservices -- curl http://service-name:port
```
