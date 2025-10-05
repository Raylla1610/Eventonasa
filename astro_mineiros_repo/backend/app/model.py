import numpy as np
from tensorflow.keras.models import load_model as tf_load
from pathlib import Path

MODEL_PATH = Path(__file__).parent.parent / 'models' / 'demo_model'

def load_model():
    try:
        model = tf_load(MODEL_PATH)
        return model
    except Exception as e:
        print('Falha ao carregar modelo:', e)
        return None

def predict_from_array(model, arr):
    if model is None:
        return np.array([0.1, 0.9])
    x = arr.reshape(1, arr.shape[0], 1)
    probs = model.predict(x)[0]
    return probs
