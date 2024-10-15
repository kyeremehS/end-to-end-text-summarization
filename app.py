from fastapi import FastAPI
import uvicorn
import os
from fastapi.responses import RedirectResponse, Response
from textsummarizer.pipeline.prediction import PredictionPipeline


app = FastAPI()

@app.get("/", tags=["authentication"])
async def index():
    return RedirectResponse(url="/docs")

@app.get("/train")
async def training():
    try:
        os.system("python main.py")
        return Response("Training successful !!" )
    except Exception as e:
        return Response(f"Error occurred! {e}")
    
@app.post("/predict")
async def predict_route(text: str):
    try:
        obj = PredictionPipeline()
        result = obj.predict(text)
        return {"summary": result}
    except Exception as e:
        raise e

if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8000)
