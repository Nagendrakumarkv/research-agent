"""
Configuration module for the Deep Research Agent.

Responsibilities:
- Load environment variables
- Validate API key
- Initialize Gemini client
- Expose reusable configuration objects
"""

import os

from dotenv import load_dotenv
from google import genai

# Load variables from .env
load_dotenv()

# Read API key
API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    raise ValueError(
        "GEMINI_API_KEY not found in .env file."
    )

# Initialize Gemini client
client = genai.Client(api_key=API_KEY)

# Gemini model to use throughout the project
MODEL_NAME = "gemini-2.5-flash"