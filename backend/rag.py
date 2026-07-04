import os

from dotenv import load_dotenv
from google import genai
from google.genai.errors import ClientError

# Load environment variables
load_dotenv()

# Configure Gemini
client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))


def ask_gemini(context, question):
    """
    Sends the retrieved resume context and user question to Gemini.
    """

    prompt = f"""
You are an AI Resume Assistant.

Answer ONLY using the information provided in the resume context.

If the answer is not present in the context, say:
"I couldn't find that information in the resume."

Resume Context:
{context}

Question:
{question}

Answer:
"""

    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt,
        )

        return response.text

    except ClientError as e:
        error = str(e)

        if "429" in error:
            return (
                "⚠️ Gemini API quota exceeded.\n"
                "Please wait a few minutes or use another API key."
            )

        elif "API_KEY_INVALID" in error or "401" in error:
            return (
                "❌ Invalid Gemini API Key.\n"
                "Please check your GOOGLE_API_KEY in the .env file."
            )

        else:
            return f"Gemini API Error:\n{error}"

    except Exception as e:
        return f"Unexpected Error:\n{e}"