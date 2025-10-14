# 🚀 Smart Task Planner

An intelligent project management tool that transforms high-level goals into detailed, actionable roadmaps using the power of **Google's Gemini API** and a **FastAPI backend**.

This application accepts a simple goal and a timeframe from the user, then generates a comprehensive plan complete with tasks, descriptions, deadlines, dependencies, priority levels, and critical path analysis.

---

## ✨ Key Features

* **🧠 AI-Powered Task Generation:** Breaks down complex goals into manageable steps using Google Gemini API.
* **📊 Intelligent Analysis:** Automatically determines task priority (High, Medium, Low) and identifies tasks on the critical path—tasks that directly impact the project deadline.

### Dual View Mode

* **List View:** Classic, interactive to-do list with checkboxes to track completion.

* **Timeline View:** Dynamic Gantt-style chart visualizing the project schedule and highlighting the critical path.

* **✅ Interactive UI:** Clean, responsive frontend where users can check off tasks as they are completed.

* **📋 Copy to Clipboard:** Easily export the entire generated plan as formatted text for documents or other applications.

* **🚀 Built with FastAPI:** Modern, fast, and robust Python backend ensures high performance and automatic API documentation.

---

## 🛠️ Tech Stack

* **Backend:** Python, FastAPI, Uvicorn
* **LLM:** Google Gemini API (`google-generativeai`)
* **Frontend:** HTML5, Tailwind CSS, Vanilla JavaScript
* **Environment:** `python-dotenv` for managing API keys

---

## 🏁 Getting Started

Follow these instructions to get a local copy up and running for development and testing.

### Prerequisites

* Python 3.8+
* An active Google Gemini API Key (available from [Google AI Studio](https://ai.google.com/studio))

---

### Installation

1. **Clone the repository**

```bash
git clone [https://github.com/your-username/smart-task-planner.git](https://github.com/srivarshini45/smart-task-planner)
cd smart-task-planner
```

2. **Create and activate a Python virtual environment**

**macOS/Linux:**

```bash
python3 -m venv venv
source venv/bin/activate
```

**Windows:**

```bash
python -m venv venv
.\venv\Scripts\activate
```

3. **Install dependencies**

```bash
pip install "fastapi[all]" uvicorn google-generativeai python-dotenv
```

4. **Create a `.env` file**
   In the root of the project directory, add your API key:

```
GEMINI_API_KEY="YOUR_API_KEY_HERE"
```

---

## 🏃‍♂️ Usage

1. **Start the backend server**

```bash
uvicorn main:app --reload
```

The API will run at: `http://127.0.0.1:8000`

2. **Open the frontend**
   Open `index.html` in your browser. It will connect automatically to the backend.

3. **Generate a plan**
   Enter your goal and timeframe into the form and let the AI create your project roadmap.

---

## 📂 Project Structure

```
smart-task-planner/
├── .env                # Stores the API key (not committed)
├── main.py             # FastAPI backend
├── index.html          # Frontend application
├── requirements.txt    # Python dependencies
└── README.md           # Project documentation
```

---

## 📄 API Documentation

FastAPI provides **self-documenting API**. Access interactive documentation at:
`http://127.0.0.1:8000/docs`

**Endpoint:** `POST /generate-plan`

**Request Body Example:**

```json
{
  "goal": "Build a personal portfolio website",
  "timeframe": "2 weeks"
}
```

**Success Response Example (200 OK):**

```json
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
```

---

## 🎥 Demo Video

Check out a short demo video showcasing the Smart Task Planner in action:

https://github.com/user-attachments/assets/03ea74f6-44ac-43e6-b80d-f35d998de13d

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Check the [issues](https://github.com/your-username/smart-task-planner/issues) page to get started.
