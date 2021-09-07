from fastapi import FastAPI
from mangum import Mangum
from app.endpoints.mutant import router as mutant_router
from app.endpoints.stats import router as stats_router

app = FastAPI(
    title="magneto's mutant army",
    # root_path="/dev"
)


@app.get("/")
async def root():
    return {"message": "Hello World"}

app.include_router(mutant_router, prefix="/api/v1")
app.include_router(stats_router, prefix="/api/v1")

handler = Mangum(app)
