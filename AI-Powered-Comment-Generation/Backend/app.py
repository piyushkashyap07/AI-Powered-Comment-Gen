from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import google.generativeai as genai
import os, time
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
from prompt import generate_prompt
load_dotenv()
prompt = generate_prompt()
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins for testing; restrict in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Configure Google Generative AI
genai.configure(api_key=os.environ['GOOGLE_API_KEY'])


# Define request body model
class PostText(BaseModel):
    text: str

# Define the model instance
model = genai.GenerativeModel("gemini-1.5-flash")

@app.post("/generate_comment")
async def generate_comment(post_text: PostText):
    try:
        time.sleep(3)
        response = model.generate_content(prompt + post_text.text)
        
        time.sleep(3)
        generated_comment = response.text.strip()
        return {"comment": generated_comment}
    except Exception as e:
        import traceback
        error_traceback = traceback.format_exc()
        print(f"Error occurred: {str(e)}\nTraceback: {error_traceback}")
        raise HTTPException(status_code=500, detail=str(e))
# uvicorn app:app --reload
