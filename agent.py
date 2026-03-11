from google import genai
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")
if not API_KEY:
    raise ValueError("Set GEMINI_API_KEY in your .env file")

# Create the GenAI client
client = genai.Client(api_key=API_KEY)

def generate_diet_plan(user_data: str) -> str:
    prompt = f"""
    You are a professional nutritionist AI.

    Based on the user details below, generate a healthy daily diet plan.

    User:
    {user_data}

    Provide:
    - Daily calories
    - Macronutrients
    - Breakfast
    - Lunch
    - Snacks
    - Dinner
    """

    # Use a valid Gemini model
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text
