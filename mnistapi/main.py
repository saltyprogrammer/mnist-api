from fastapi import FastAPI

from mnistapi.router import image_post

app = FastAPI()
app.include_router(image_post.router)


@app.get("/")
def index():
    return {"message": "Nothing to do here"}