from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

# --- NEW: Enable CORS ---
# This allows your local HTML file to talk to the local API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# ------------------------

class StringInput(BaseModel):
    part_a: str
    part_b: str

@app.post("/combine")
def combine_strings(payload: StringInput):
    combined = f"{payload.part_a} {payload.part_b}"
    return {"result": combined}
