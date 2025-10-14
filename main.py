import os
import json
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
from typing import List, Optional
import google.generativeai as genai
from dotenv import load_dotenv
from datetime import date

# --- Configuration ---
load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# Check for API Key
if not GEMINI_API_KEY:
    raise ValueError("GEMINI_API_KEY not found. Please set it in your .env file.")

# Configure the Gemini API client
genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel('models/gemini-pro-latest')

# --- FastAPI App Initialization ---
app = FastAPI(
    title="Smart Task Planner API",
    description="An API that uses a Large Language Model to break down user goals into actionable tasks.",
    version="1.0.0"
)

# --- CORS Middleware ---
# Allows the frontend (running on a different origin) to communicate with this backend.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins for simplicity. For production, restrict this.
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --- Pydantic Models (Data Schemas) ---

class GoalInput(BaseModel):
    """Defines the structure of the input from the user."""
    goal: str = Field(..., example="Launch a new productivity app in 3 months")
    timeframe: str = Field(..., example="3 months")

class Task(BaseModel):
    """Defines the structure of a single task in the generated plan."""
    id: int = Field(..., description="Unique identifier for the task.")
    task: str = Field(..., description="The name of the task.")
    description: str = Field(..., description="A brief description of what needs to be done.")
    deadline: str = Field(..., description="Suggested completion date in YYYY-MM-DD format.")
    dependencies: List[int] = Field(..., description="List of task IDs that this task depends on.")

class PlanOutput(BaseModel):
    """Defines the structure of the final output returned by the API."""
    plan: List[Task]

# --- Helper Function for LLM Interaction ---

def generate_plan_from_llm(goal: str, timeframe: str) -> Optional[dict]:
    """
    Constructs a prompt, sends it to the Gemini API, and attempts to parse the response.
    """
    # The current date is dynamically included to give the LLM context for deadlines.
    today = date.today().strftime("%Y-%m-%d")
    
    # This detailed prompt is crucial for getting a structured and logical response.
    prompt = f"""
    You are an expert project manager AI based in India. Your task is to break down a high-level goal into a detailed, actionable plan.

    Goal: "{goal}"
    Total Timeframe: "{timeframe}"
    Current Date: "{today}"

    Based on this, generate a list of tasks. For each task, provide:
    1. A unique integer `id` starting from 1.
    2. A short, actionable `task` name.
    3. A brief `description` of what needs to be done for the task.
    4. A suggested `deadline` as a string in "YYYY-MM-DD" format, logically spaced within the total timeframe starting from today.
    5. A list of `dependencies`, which are the integer `id`s of other tasks that must be completed first. The first task should have an empty dependency list `[]`.

    Return your response ONLY as a single, valid JSON object with a single key "plan" which contains a list of these task objects. Do not include any text, code block markers, or explanations before or after the JSON.

    Example format:
    {{
      "plan": [
        {{
          "id": 1,
          "task": "Example Task 1",
          "description": "Description for task 1.",
          "deadline": "2025-10-21",
          "dependencies": []
        }},
        {{
          "id": 2,
          "task": "Example Task 2",
          "description": "Description for task 2.",
          "deadline": "2025-10-28",
          "dependencies": [1]
        }}
      ]
    }}
    """
    
    try:
        # The Gemini API call
        response = model.generate_content(prompt)
        
        # Clean up the response text to ensure it's valid JSON.
        # Sometimes the model might wrap the JSON in ```json ... ```
        cleaned_text = response.text.strip().replace("```json", "").replace("```", "").strip()
        
        # --- ADD THIS LINE FOR DEBUGGING ---
        #print(f"--- RAW LLM RESPONSE ---\n{cleaned_text}\n--------------------------")
        # -----------------------------------

        # Parse the cleaned text into a Python dictionary
        parsed_json = json.loads(cleaned_text)
        return parsed_json
        
    except Exception as e:
        print(f"Error communicating with LLM or parsing JSON: {e}")
        return None


# --- API Endpoint ---

@app.post("/generate-plan", response_model=PlanOutput)
async def create_plan(goal_input: GoalInput):
    """
    Accepts a user's goal and timeframe, then uses an LLM to generate a structured task plan.
    """
    if not goal_input.goal or not goal_input.timeframe:
        raise HTTPException(status_code=400, detail="Goal and timeframe cannot be empty.")

    # Call the helper function to get the plan from the LLM
    generated_data = generate_plan_from_llm(goal_input.goal, goal_input.timeframe)

    if not generated_data or "plan" not in generated_data:
        raise HTTPException(
            status_code=500, 
            detail="Failed to generate a valid plan from the LLM. The model may have returned an unexpected format."
        )

    # Pydantic will automatically validate the structure of the generated_data.
    # If it doesn't match the PlanOutput model, FastAPI will raise a validation error.
    return generated_data

# A simple root endpoint to confirm the API is running.
@app.get("/")
def read_root():
    return {"message": "Welcome to the Smart Task Planner API. Go to /docs for the API documentation."}

