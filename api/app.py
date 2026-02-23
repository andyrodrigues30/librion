from fastapi import FastAPI

app = FastAPI(title="Librion API")

@app.get("/")
def hello():
  return {"hello": "world"}