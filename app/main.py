from fastapi import FastAPI
from mangum import Mangum
from endpoints.mutant import router as api_router

app = FastAPI()


@app.get("/root")
async def root():
    return {"message": "Hello World"}

app.include_router(api_router, prefix="/api/v1")

handler = Mangum(app)
