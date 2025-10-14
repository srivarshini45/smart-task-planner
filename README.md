🚀 Smart Task Planner
An intelligent project management tool that transforms high-level goals into detailed, actionable roadmaps using the power of Google's Gemini API and a FastAPI backend.

This application accepts a simple goal and a timeframe from the user, then generates a comprehensive plan complete with tasks, descriptions, deadlines, dependencies, priority levels, and critical path analysis.

✨ Key Features
🧠 AI-Powered Task Generation: Leverages the Google Gemini API to break down complex goals into manageable steps.

📊 Intelligent Analysis: Automatically determines task priority (High, Medium, Low) and identifies tasks on the critical path—tasks that directly impact the project deadline.

** dual_view_mode ## 📈 Dual View Mode**:

List View: A classic, interactive to-do list with checkboxes to track completion.

Timeline View: A dynamic Gantt-style chart that visualizes the project schedule and highlights the critical path.

✅ Interactive UI: A clean, responsive frontend where users can check off tasks as they are completed.

📋 Copy to Clipboard: Easily export the entire generated plan as formatted text to use in documents or other applications.

🚀 Built with FastAPI: A modern, fast, and robust Python backend ensures high performance and automatic API documentation.

🛠️ Tech Stack
Backend: Python, FastAPI, Uvicorn

LLM: Google Gemini API (google-generativeai)

Frontend: HTML5, Tailwind CSS, Vanilla JavaScript

Environment: python-dotenv for managing API keys

🏁 Getting Started
Follow these instructions to get a local copy up and running for development and testing purposes.

Prerequisites
Python 3.8+

An active Google Gemini API Key. You can get one from Google AI Studio.

Installation
Clone the repository:

git clone [https://github.com/your-username/smart-task-planner.git](https://github.com/your-username/smart-task-planner.git)
cd smart-task-planner

Create and activate a Python virtual environment:

macOS/Linux:

python3 -m venv venv
source venv/bin/activate

Windows:

python -m venv venv
.\venv\Scripts\activate

Install the required dependencies:

pip install -r requirements.txt

(Note: If you don't have a requirements.txt file, you can create one after installing the packages manually: pip freeze > requirements.txt)

Create a .env file:
In the root of the project directory, create a file named .env and add your Google Gemini API key:

GEMINI_API_KEY="YOUR_API_KEY_HERE"

🏃‍♂️ Usage
Start the backend server:
Run the following command in your terminal from the project's root directory:

uvicorn main:app --reload

The API will be running at http://127.0.0.1:8000.

Open the frontend:
Simply open the index.html file in your web browser. It will automatically connect to your running local backend.

Generate a plan!
Enter your goal and timeframe into the form and see the AI work its magic.

📂 Project Structure
smart-task-planner/
├── .env                # Stores the API key (not committed to Git)
├── main.py             # The FastAPI backend application
├── index.html          # The self-contained frontend application
├── requirements.txt    # List of Python dependencies
└── README.md           # You are here!

📄 API Documentation
The API is self-documenting thanks to FastAPI. Once the server is running, you can access the interactive API documentation (Swagger UI) at:

http://127.0.0.1:8000/docs

Endpoint: POST /generate-plan
Description: Accepts a goal and timeframe, returning a complete, AI-generated task plan.

Request Body:

{
  "goal": "Build a personal portfolio website",
  "timeframe": "2 weeks"
}

Success Response (200 OK):

{
  "plan": [
    {
      "id": 1,
      "task": "Define Website Scope & Content",
      "description": "...",
      "deadline": "2025-10-15",
      "dependencies": [],
      "priority": "High",
      "is_critical": true
    }
  ]
}

🤝 Contributing
Contributions, issues, and feature requests are welcome! Feel free to check the issues page.

