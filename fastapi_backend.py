from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.responses import JSONResponse
import whisper 
import tempfile
import os

app = FastAPI()
model = whisper.load_model("base")

@app.post("/transcribe/")
async def transcribe(file: UploadFile = File(...)):
    try:
        # Save uploaded audio file a temporary file
        with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as temp_file:
            temp_file.write(file.file.read())
            temp_file_path = temp_file.name

        # Transcribe audio file with timestamps
        result = model.transcribe(temp_file_path, language="en", verbose=True)

        # Remove temporary audio file
        os.remove(temp_file_path)

        return JSONResponse(content={"transcription": result["text"], "segments": result["segments"]})

    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
