"""Loads MNIST model classifiers"""

import os

from tflite_runtime.interpreter import Interpreter

def get_tflite_model():
    """Get a tflite model"""
    if path := os.getenv("MODEL_PATH"):
        yield Interpreter(path)
    else:
        raise FileNotFoundError("Could not found the required model.")
    