from fastapi import APIRouter, UploadFile, File
from fastapi.responses import JSONResponse
import numpy as np
from app.utils import preprocess_from_file
from app.model import load_model, predict_from_array

router = APIRouter()
model = load_model()

@router.post('/predict')
async def predict(file: UploadFile = File(...)):
    arr = await preprocess_from_file(file)
    probs = predict_from_array(model, arr)
    return JSONResponse({'probabilities': probs.tolist()})
