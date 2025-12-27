from contextlib import asynccontextmanager
from fastapi import FastAPI
from app.db import db
from fastapi.middleware.cors import CORSMiddleware
from app.routers.equipment import router as equipment_router
from app.routers.requests import router as request_router
from app.routers.teams import router as team_router
from app.routers.user import router as user_router
from app.routers.setup import router as setup_router
from app.routers.maintenance_req import router as maintenance_req
from app.routers.scrapped import router as scarapper_router
from app.routers.organization import router as organization




@asynccontextmanager
async def lifespan(app: FastAPI):
    await db.connect()
    yield
    await db.disconnect()

app = FastAPI(lifespan=lifespan)

# 2. Add the middleware to the FastAPI app
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],            # Allows cookies/auth headers
    allow_methods=["*"],               # Allows ALL HTTP methods (GET, POST, PATCH, etc.)
    allow_headers=["*"],               # Allows ALL headers
)


app.include_router(equipment_router)
app.include_router(request_router)
app.include_router(team_router)
app.include_router(user_router)
app.include_router(setup_router)
app.include_router(maintenance_req)
app.include_router(scarapper_router)
app.include_router(organization)