"""POST method for image classification"""

from fastapi import APIRouter, Depends
from tflite_runtime.interpreter import Interpreter

from mnistapi.models.mnist import get_tflite_model

router = APIRouter(
    prefix="/predictor",
    tags=["predictor", "classification"]
)

@router.post("/classify")
def classify_image(db: Interpreter=Depends(get_tflite_model)):
    return {"message": "not implemented"}