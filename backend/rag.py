from pathlib import Path
import os

from dotenv import load_dotenv
from google import genai

BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv(BASE_DIR / ".env")

client = genai.Client(
    api_key=os.getenv("GOOGLE_API_KEY")
)


def ask_gemini(context, question):
    """
    Ask Gemini using the retrieved resume context.
    """

    prompt = f"""
You are an AI Resume Assistant.

Answer ONLY using the information present in the resume context.

If the answer is not available in the resume,
say:
"I couldn't find that information in the resume."

Resume Context:
{context}

Question:
{question}
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt,
    )

    return response.text