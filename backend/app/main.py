from fastapi import FastAPI
from api.routes import auth
from api.routes import graph
from api.graph.graph import checkpointer_cm
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.include_router(auth.router)
app.include_router(graph.router)

# @app.on_event("startup")
# def startup():
#     init_db()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.get("/health")
def health():
    return {"status": "server is up and running!"}

@app.on_event("shutdown")
def shutdown():
    checkpointer_cm.__exit__(None, None, None)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app=app, host="0.0.0.0", port=8000)