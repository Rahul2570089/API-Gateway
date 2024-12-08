from fastapi import FastAPI
from routes.user_routes import router as user_router

app = FastAPI(title="API Gateway")


# Include routes
app.include_router(user_router, prefix="/users", tags=["Users"])

@app.get("/")
async def root():
    return {"message": "API Gateway is running!"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("api-gateway.app.main:app", host="0.0.0.0", port=8000, reload=True)