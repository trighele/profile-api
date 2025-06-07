-----

# FastAPI Email Sender with Resend

This is a simple FastAPI application that provides a POST endpoint to send emails using the [Resend API](https://resend.com/). It's designed to be straightforward and easy to set up for anyone needing to integrate email sending capabilities into their FastAPI projects.

-----

## 🚀 Features

  * **FastAPI Framework:** Leverage the speed and simplicity of FastAPI.
  * **Resend API Integration:** Easily send emails via the Resend platform.
  * **Environment Variables:** Securely manage your API key using `.env` files.
  * **Pydantic Validation:** Robust input validation for email data.

-----

## 🛠️ Setup

Follow these steps to get your project up and running:

### 1\. Clone the Repository (or create files manually)

If you're starting from scratch, create the following files: `main.py` and `.env`.

### 2\. Install Dependencies

Navigate to your project directory in the terminal and install the required Python packages:

```bash
pip install fastapi uvicorn python-dotenv resend
```

### 3\. Get Your Resend API Key

1.  **Sign up** or **log in** to your [Resend account](https://resend.com/).
2.  Go to your API Keys section and **create a new API key**.
3.  **Copy** your API key. It typically starts with `re_...`.

### 4\. Configure Environment Variables

Create a file named `.env` in the root of your project directory (where `main.py` is located) and add your Resend API key:

```ini
RESEND_API_KEY="re_YOUR_RESEND_API_KEY"
```

**Replace `re_YOUR_RESEND_API_KEY` with the actual API key you copied from Resend.**

### 5\. Update Sender Email

In `main.py`, you'll see a line like this:

```python
"from": "onboarding@resend.dev", # IMPORTANT: Replace with your verified sender email
```

**For production, you must replace `"onboarding@resend.dev"` with an email address from a domain you have [verified with Resend](https://www.google.com/search?q=https://resend.com/docs/send-emails/setup-domains).** Using `onboarding@resend.dev` is generally for testing purposes only.

-----

## ▶️ How to Run

1.  **Start the FastAPI application** using Uvicorn from your terminal:

    ```bash
    uvicorn main:app --reload
    ```

      * `main`: Refers to the `main.py` file.
      * `app`: Refers to the `FastAPI()` instance named `app` inside `main.py`.
      * `--reload`: Automatically reloads the server on code changes (useful during development).

    The application will typically run on `http://127.0.0.1:8000`.

-----

## 🧪 Testing the API

Once the server is running, you can test the email sending functionality.

### Using FastAPI's Interactive Docs (Swagger UI)

Open your web browser and go to: `http://127.0.0.1:8000/docs`

1.  You'll see the `/send-email` endpoint listed.

2.  Click on it, then click **"Try it out"**.

3.  In the **"Request body"** text area, enter a JSON payload similar to this:

    ```json
    {
      "to": "recipient@example.com",
      "subject": "Hello from FastAPI and Resend!",
      "html_content": "<h1>This is a test email</h1><p>Sent from your FastAPI application using Resend.</p>"
    }
    ```

    **Remember to replace `"recipient@example.com"` with a real email address you can check.**

4.  Click **"Execute"**.

You should receive a `200 OK` response, and the email should arrive in the specified recipient's inbox.

-----

## ⚠️ Important Notes

  * **Security:** Never hardcode your API key directly in your code. Always use environment variables as shown. For production, consider more robust secret management solutions.
  * **Verified Domains:** Resend requires you to verify your sending domains to prevent spam and ensure deliverability. Make sure your "from" email address is associated with a verified domain.
  * **Error Handling:** This example includes basic error handling. For a production application, you might want more granular error messages and logging.

-----