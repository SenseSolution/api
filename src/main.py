from fastapi import FastAPI

app = FastAPI(title="todo api", version="0.0.1")


@app.get("/")
async def main():
    return {"message", "Hello!"}