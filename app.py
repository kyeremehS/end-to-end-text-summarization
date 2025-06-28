from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse, HTMLResponse, Response
from textsummarizer.pipeline.prediction import PredictionPipeline
import os

app = FastAPI()

# Mount static files directory (for CSS, JS, images)
app.mount("/static", StaticFiles(directory="static"), name="static")

# Load Jinja2 templates
templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse, tags=["frontend"])
async def index(request: Request):
    """Serve the main HTML page."""
    return templates.TemplateResponse("index.html", {"request": request})


@app.get("/train", tags=["backend"])
async def training():
    """Trigger a training process."""
    try:
        os.system("python main.py")
        return Response("Training successful!")
    except Exception as e:
        return Response(f"Error occurred: {e}")


@app.post("/predict", response_class=HTMLResponse, tags=["backend"])
async def predict_route(request: Request, text: str = Form(...)):
    """Handle text summarization and render it in the HTML."""
    try:
        obj = PredictionPipeline()
        summary = obj.predict(text)
        return templates.TemplateResponse("index.html", {
            "request": request,
            "summary": summary,
            "text": text
        })
    except Exception as e:
        return templates.TemplateResponse("index.html", {
            "request": request,
            "error": str(e),
            "text": text
        })


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
