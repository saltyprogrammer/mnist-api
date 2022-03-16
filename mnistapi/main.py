from fastapi import FastAPI

from fastapi.middleware.cors import CORSMiddleware

from mnistapi.router import image_post

origins = ["*"]

app = FastAPI()
app.include_router(image_post.router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def index():
    return {"message": "Nothing to do here"}