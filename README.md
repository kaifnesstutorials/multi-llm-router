🧠 Multi-LLM Router

Cost-efficient, fault-tolerant multi-LLM routing system built with FastAPI.
Routes prompts intelligently to multiple LLM providers (Groq & OpenAI) with automatic fallback, token-based cost tracking, and a real-time monitoring dashboard.

📌 Repo: https://github.com/kaifnesstutorials/multi-llm-router

📌 Overview

Multi-LLM Router is a scalable microservice that intelligently sends user prompts to multiple Large Language Model (LLM) providers based on cost, availability, and reliability.

It provides:

Automatic failover between providers

Token usage and cost tracking per request

Monitoring dashboard for provider health, latency, and usage

This is ideal for developers looking to optimize LLM usage, reduce costs, and maintain reliability.

🧠 Why This Project?

Direct usage of LLM APIs can be expensive and unreliable:

Some providers are cheaper but may fail occasionally

High token usage increases cost

Limited observability into latency, usage, or provider success

Multi-LLM Router solves these challenges by:

Prioritizing cheapest providers first

Falling back automatically if a provider fails

Logging token usage and cost

Providing observability via a dashboard

💡 Key Features
🧠 Smart Routing

Dynamically sorts providers by cost

Routes to the cheapest available provider

Automatic fallback if a provider fails

💰 Cost Optimization

Token counting and cost calculation per request

Optional prompt optimization to reduce token usage

Aggregated cost tracking in dashboard

🩺 Reliability

Provider health monitoring (success/failure)

Latency tracking per provider

Success rate percentage tracking

📊 Observability & Dashboard

Usage statistics (tokens, cost, requests)

Provider usage bar charts

Request history and prompt optimization warnings

⚡ Prompt Optimization

Trims overly large prompts to reduce token cost

Displays warning in dashboard when a prompt is trimmed

📂 Project Structure
multi-llm-router/
│
├── app.py                    # FastAPI main application
├── router.py                 # Multi-LLM routing logic
├── utils/
│   └── logger.py             # Usage logging
├── providers/
│   ├── base.py               # Provider base class
│   ├── groq_provider.py      # Groq API integration
│   └── openai_provider.py    # OpenAI API integration
├── config/
│   └── providers.yaml        # Provider configuration
├── templates/
│   └── index.html            # Frontend HTML dashboard
├── logs/
│   └── usage.json            # Stored usage logs
├── requirements.txt          # Python dependencies
└── .gitignore

🚀 Setup & Installation

1️⃣ Clone the Repository

git clone https://github.com/kaifnesstutorials/multi-llm-router.git
cd multi-llm-router


2️⃣ Create a Virtual Environment

python -m venv venv
# Windows
venv\Scripts\activate
# Linux/macOS
source venv/bin/activate


3️⃣ Install Dependencies

pip install -r requirements.txt


4️⃣ Update providers.yaml with your API keys

providers:
  - name: groq
    base_url: https://api.groq.com/openai/v1
    model: llama-3.1-8b-instant
    api_key: "YOUR_GROQ_KEY"
    cost_per_1k_tokens: 0.0005
    timeout: 30

  - name: openai
    base_url: https://api.openai.com/v1
    model: gpt-4o-mini
    api_key: "YOUR_OPENAI_KEY"
    cost_per_1k_tokens: 0.003
    timeout: 30


⚠️ Do not commit API keys to GitHub.

5️⃣ Run the Server

uvicorn app:app --reload


Open the dashboard at: http://127.0.0.1:8000

📌 API Endpoints
🔹 POST /generate

Generate a response using the routing system.

Request Body:

{
  "prompt": "Explain AI in simple words"
}


Response Example:

{
  "provider": "openai",
  "modelUsed": "gpt-4o-mini",
  "tokens": 15,
  "cost": 0.000045,
  "latency": 1.2,
  "response": "AI stands for Artificial Intelligence...",
  "status": "success"
}

🔹 GET /stats

Returns usage statistics:

Total tokens used

Total cost

Request counts

🧑‍💻 Author

Mohd Kaif Shaikh – AI & Data Science Enthusiast
