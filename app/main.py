from fastapi import FastAPI
from database import Base, engine
from fastapi.responses import RedirectResponse
from controllers import produto_controller
from controllers import usuario_controller 

Base.metadata.create_all(bind=engine)

app = FastAPI(title="API E-commerce (AV2)")

app.include_router(produto_controller.router)

app.include_router(usuario_controller.router)

@app.get("/", include_in_schema=False)
def root():
    return RedirectResponse(url="/docs")