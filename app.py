
import os
from dotenv import load_dotenv
from google import genai
from groq import Groq

# Load API keys from .env
load_dotenv()

# Read API keys
gemini_key = os.getenv("GEMINI_API_KEY")
groq_key = os.getenv("GROQ_API_KEY")

# Check API keys
if not gemini_key or not groq_key:
    print("Error: API keys are missing in .env")
    raise SystemExit(1)

# Create API clients
gemini_client = genai.Client(api_key=gemini_key)
groq_client = Groq(api_key=groq_key)

# Model IDs
GEMINI_MODEL = "gemini-3.5-flash-lite"
GROQ_MODEL = "openai/gpt-oss-20b"

print("===== AI API APPLICATION =====")
print("1. Gemini API")
print("2. Groq API")

choice = input("Choose an API (1 or 2): ")
prompt = input("Enter your question: ")

if not prompt.strip():
    print("Please enter a question.")

elif choice == "1":
    try:
        response = gemini_client.models.generate_content(
            model=GEMINI_MODEL,
            contents=prompt
        )

        print("\nGemini Response:")
        print(response.text)

    except Exception as e:
        print("Error type:", type(e).__name__)
        print("Error details:", e)

elif choice == "2":
    try:
        response = groq_client.chat.completions.create(
            model=GROQ_MODEL,
            messages=[
                {"role": "user", "content": prompt}
            ]
        )
        print("\nGroq Response:")
        print(response.choices[0].message.content)

    except Exception as e:
        print("Groq API error:", e)

else:
    print("Invalid choice. Please select 1 or 2.")