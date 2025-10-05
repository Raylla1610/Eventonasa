from fastapi import FastAPI
from app.api import router as api_router

app = FastAPI(title='AstroMineiros API')
app.include_router(api_router, prefix='/api')

@app.get('/')
def root():
    return {'project':'AstroMineiros', 'status':'ok'}
