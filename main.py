from fastapi import FastAPI

app = FastAPI(title= "FastAPI Backend Project")

@ app.get("/health")
def health():
    return {"status" : "ok"}

