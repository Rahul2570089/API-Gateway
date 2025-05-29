from fastapi import FastAPI, Depends
from fastapi.security import OAuth2PasswordRequestForm
from fastapi import HTTPException
from routes.user_routes import router as user_router
from routes.job_routes import router as job_router
from routes.pipeline_routes import router as pipeline_router
from app.auth import create_access_token

app = FastAPI(title="API Gateway")


# Include routes
app.include_router(user_router, prefix="/users", tags=["Users"])
app.include_router(job_router, prefix="/jobs", tags=["Jobs"])
app.include_router(pipeline_router, prefix="/pipelines", tags=["Pipelines"])


@app.post("/login")
def login(form_data: dict):
    username = form_data["username"]
    password = form_data["password"]

    # Dummy user
    if username == "admin" and password == "secret":
        token = create_access_token(data=form_data)
        return {"access_token": token, "token_type": "bearer"}
    
    raise HTTPException(status_code=401, detail="Invalid credentials")

@app.get("/")
async def root():
    return {"message": "API Gateway is running!"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("api-gateway.app.main:app", host="0.0.0.0", port=8000, reload=True)