import numpy as np
from lightkurve import LightCurve
import io

async def preprocess_from_file(file):
    content = await file.read()
    try:
        s = content.decode('utf-8')
        import pandas as pd
        df = pd.read_csv(io.StringIO(s))
        time = df.iloc[:,0].values
        flux = df.iloc[:,1].values
    except Exception:
        time = np.linspace(0,27,1000)
        flux = np.ones_like(time)
    arr = np.zeros((600,))
    return arr
