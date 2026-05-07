# from fastapi import FastAPI
# from app.database import engine, Base
# from app.routers import users, jobs, applications, companies

# Base.metadata.create_all(bind=engine)

# app = FastAPI(
#     title="Job Listings API",
#     description="A REST API for job seekers and recruiters",
#     version="1.0.0"
# )

# app.include_router(users.router)
# app.include_router(jobs.router)
# app.include_router(applications.router)
# app.include_router(companies.router)

# @app.get("/")
# def root():
    
#     return {"message": "Job Listings API is running"}

from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi
from app.database import engine, Base
from app.routers import users, jobs, applications, companies

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Job Listings API",
    description="A REST API for job seekers and recruiters",
    version="1.0.0"
)

app.include_router(users.router)
app.include_router(jobs.router)
app.include_router(applications.router)
app.include_router(companies.router)

@app.get("/")
def root():
    return {"message": "Job Listings API is running"}

def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="Job Listings API",
        version="1.0.0",
        description="A REST API for job seekers and recruiters",
        routes=app.routes,
    )
    openapi_schema["components"]["securitySchemes"] = {
        "BearerAuth": {
            "type": "http",
            "scheme": "bearer",
            "bearerFormat": "JWT",
        }
    }
    openapi_schema["security"] = [{"BearerAuth": []}]
    app.openapi_schema = openapi_schema
    return app.openapi_schema

app.openapi = custom_openapi