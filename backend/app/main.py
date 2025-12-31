from fastapi import FastAPI
from api.routes import auth

app = FastAPI()
app.include_router(auth.router)

# @app.on_event("startup")
# def startup():
#     init_db()

@app.get("/health")
def health():
    return {"status": "server is up and running!"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app=app, host="0.0.0.0", port=8000)