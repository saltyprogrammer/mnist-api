"""POST method for image classification"""

from io import BytesIO
import numpy as np

from fastapi import APIRouter, Depends, UploadFile, File, Form
from tflite_runtime.interpreter import SignatureRunner
from PIL import Image
from PIL import ImageOps

from mnistapi.models.mnist import get_tflite_model

router = APIRouter(
    prefix="/predictor",
    tags=["predictor", "classification"]
)

def preprocess_image(image: Image):

    image = ImageOps.grayscale(image).resize((28, 28))
    image = np.array(image).reshape((28, 28, 1)) / 255

    return np.expand_dims(image, axis=0).astype("float32")

def predict(signature: SignatureRunner, batch: np.ndarray):
    predictions = signature(input_2=batch)["dense_1"][0]
    return int(predictions.argmax())

@router.post("/classify")
async def classify_image(file: UploadFile=File(...), signature: SignatureRunner=Depends(get_tflite_model)):
    batch = preprocess_image(Image.open(BytesIO(await file.read())))
    print(batch.shape)
    return {"category": predict(signature, batch)}