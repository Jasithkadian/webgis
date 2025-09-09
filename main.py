from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
import json
import os

app = FastAPI()

# ✅ Enable CORS so React can connect
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # ⚠️ dev only
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Helper function to read JSON files
def read_json_file(filename: str):
    filepath = os.path.join(os.path.dirname(__file__), filename)
    with open(filepath, "r", encoding="utf-8") as f:
        return json.load(f)

@app.get("/")
def home():
    return {"message": "FRA WebGIS Backend is running"}

@app.get("/claims")
def get_claims():
    data = read_json_file("claims.json")
    return JSONResponse(content=data)

@app.get("/assets")
def get_assets():
    data = read_json_file("assets.json")
    return JSONResponse(content=data)

@app.get("/dss/recommend")
def get_recommendations():
    data = read_json_file("dss.json")
    return JSONResponse(content=data)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
