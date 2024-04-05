from fastapi import FastAPI
from routes.user_routes import router as user_router
from routes.role_routes import router as rol_router
from routes.company_routes import router as empresa_router
from routes.career_routes import router as carrera_router
from routes.job_offer_routes import router as ofertas_router
from routes.applicant_routes import router as aplicante_router
from routes.auth_routes import router as auth_router
from routes.statistics_routes import router as statistics_router
from routes.faculty_routes import router as faculty_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_router)
app.include_router(user_router)
app.include_router(rol_router)
app.include_router(empresa_router)
app.include_router(carrera_router)
app.include_router(ofertas_router)
app.include_router(aplicante_router)
app.include_router(statistics_router)
app.include_router(faculty_router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
