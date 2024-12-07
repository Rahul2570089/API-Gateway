from fastapi import FastAPI
from app.routes.user_routes import router as user_router

app = FastAPI(title="API Gateway")


# Include routes
app.include_router(user_router, prefix="/users", tags=["Users"])

@app.get("/")
async def root():
    return {"message": "API Gateway is running!"}
