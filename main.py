import os
from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware # Import CORSMiddleware
from pydantic import BaseModel, EmailStr
import resend

load_dotenv()

app = FastAPI()

origins = [
    "http://localhost:5173",  # Your React app's development URL
    "https://www.tomrighele.com", # Your production React app's URL
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,          # List of origins that are allowed to make requests
    allow_credentials=True,         # Allow cookies to be included in requests (e.g., for auth)
    allow_methods=["*"],            # Allow all HTTP methods (GET, POST, PUT, DELETE, etc.)
    allow_headers=["*"],            # Allow all headers in the request
)

resend.api_key = os.getenv("RESEND_API_KEY")
EMAIL_FROM = os.getenv("EMAIL_FROM")

if not resend.api_key:
    raise ValueError("RESEND_API_KEY not found in environment variables. Please set it.")

class EmailData(BaseModel):
    to: EmailStr
    subject: str
    html_content: str

@app.post("/send-email")
async def send_email(email_data: EmailData):
    """
    Receives email data and sends an email using the Resend API.
    """
    try:
        # For Resend, the 'from' email must be a domain you've verified with Resend.
        # Replace 'onboarding@resend.dev' with your verified sender email.
        # If you don't have a verified domain, you can use 'onboarding@resend.dev'
        # for testing purposes, but for production, use your own domain.
        params: resend.Emails.SendParams = {
            "from": EMAIL_FROM,  # IMPORTANT: Replace with your verified sender email
            "to": email_data.to,
            "subject": email_data.subject,
            "html": email_data.html_content,
        }
        response = resend.Emails.send(params)
        
        return {"message": "Email sent successfully!", "data": response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to send email: {e}")

@app.get("/")
async def root():
    return {"message": "FastAPI Resend Email Sender is running!"}