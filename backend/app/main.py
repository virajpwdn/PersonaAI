# main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
from api.routes import auth
from api.routes import graph
from api.graph.graph import checkpointer_cm
from api.database.db import RedisClient


# ===== LIFESPAN MANAGER =====
@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    App lifecycle manager - runs startup and shutdown logic
    Similar to Express app.listen() pattern
    """
    # ===== STARTUP =====
    print("\n" + "="*50)
    print("🚀 Starting Application")
    print("="*50)
    
    # Connect to Redis
    try:
        RedisClient.connect()
    except Exception as e:
        print(f"❌ Failed to connect to Redis: {e}")
        # raise  # Fail startup if Redis is critical
    
    print("✅ Application ready to accept requests\n")
    
    yield
    
    # ===== SHUTDOWN =====
    print("\n" + "="*50)
    print("🛑 Shutting down Application")
    print("="*50)
    
    # Cleanup: Disconnect from Redis
    RedisClient.disconnect()
    
    # Cleanup: Close graph checkpoint
    checkpointer_cm.__exit__(None, None, None)
    
    print("✅ Application shutdown complete\n")


# ===== INITIALIZE FASTAPI APP =====
app = FastAPI(lifespan=lifespan)

# ===== INCLUDE ROUTERS =====
app.include_router(auth.router)
app.include_router(graph.router)

# ===== MIDDLEWARE =====
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

# ===== ROUTES =====
@app.get("/health")
def health():
    """Health check endpoint"""
    return {"status": "server is up and running!"}


# ===== RUN SERVER =====
if __name__ == "__main__":
    import uvicorn
    
    uvicorn.run(
        app=app,
        host="0.0.0.0",
        port=8000
    )