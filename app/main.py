from fastapi import FastAPI
from routes.user_routes import router as user_router
from routes.rol_routes import router as rol_router
from routes.empresa_routes import router as empresa_router
from routes.carrera_routes import router as carrera_router
from routes.ofertas_routes import router as ofertas_router
from routes.aplicante_routes import router as aplicante_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    #"http://localhost.tiangolo.com",
    #"https://localhost.tiangolo.com",
    "http://localhost:5173"
    #"http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(user_router)
app.include_router(rol_router)
app.include_router(empresa_router)
app.include_router(carrera_router)
app.include_router(ofertas_router)
app.include_router(aplicante_router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)