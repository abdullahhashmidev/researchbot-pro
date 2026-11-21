# 🤖 ResearchBot Pro

**AI-powered business research and reporting** built with **LangGraph**, **CrewAI** and the **Groq** LLM.
Ask a business question or a topic and get a professional, source-backed report in minutes.

---

## ✨ Features

- 🔍 **Automatic web research** with DuckDuckGo (no search API key needed)
- 🤖 **Multi-agent pipeline**: Researcher → Analyst → Writer (CrewAI)
- 🔄 **LangGraph workflow** with input validation, error routing and a save step
- 👔 **CEO, CFO and Problem-Solving reports** with structured sections and 30/60/90-day plans
- 📊 **Streamlit dashboard**: executive, financial, HR and sales views, plus custom CSV/Excel upload with charts
- 💾 **Markdown export** for every generated report
- 🆓 **Free to run**: Groq free tier and DuckDuckGo

## 🏗️ How it works

```
Topic / business question
        │
        ▼
 [LangGraph workflow]
   ├─ validate_input     → checks length and content
   ├─ run_research       → CrewAI crew (Researcher → Analyst → Writer)
   └─ save_report        → outputs/report_<topic>_<timestamp>.md
```

## 📁 Project structure

```
researchbot_pro/
├── app.py              # Streamlit dashboard + AI reports (main entry point)
├── quick_chat.py       # Simple single-LLM chat demo
├── main.py             # Command-line research workflow
├── requirements.txt
├── .env.example
└── src/
    ├── config.py       # Environment and settings
    ├── agents/         # CrewAI agents (researcher, analyst, writer, CEO, CFO, ...)
    ├── crew/           # Crews that combine agents and tasks
    ├── graph/          # LangGraph state and workflow
    ├── analytics/      # Data loading, profiling and Plotly charts
    ├── tools/          # DuckDuckGo search tool
    └── utils/          # File handling
```

## 🚀 Setup

Requires **Python 3.10+**. Run these inside the `researchbot_pro` folder.

**Windows (Git Bash)**
```bash
python -m venv .venv
source .venv/Scripts/activate
```

**macOS / Linux**
```bash
python3 -m venv .venv
source .venv/bin/activate
```

Then, on any OS:
```bash
pip install -r requirements.txt
cp .env.example .env
```

Open `.env` and set your key. Get a free key at [console.groq.com](https://console.groq.com).

```env
GROQ_API_KEY=your_groq_api_key_here
MODEL_NAME=groq/llama-3.3-70b-versatile
OUTPUT_DIR=outputs
```

## ▶️ Run

Dashboard (recommended):
```bash
streamlit run app.py
```

Command-line research report:
```bash
python main.py
```

Generated reports are saved in `outputs/`.

## ☁️ Deploy on Streamlit Community Cloud

1. Push this repo to GitHub.
2. In Streamlit Cloud, choose **Main file path**: `researchbot_pro/app.py`.
3. Under **Settings → Secrets**, add:
   ```toml
   GROQ_API_KEY = "your_groq_api_key_here"
   ```

## ⚠️ Notes

- The dashboard's executive, financial, HR and sales views use **synthetic sample data** for demonstration. Use **Custom Data Upload** for real data.
- AI reports call external LLM and search services, so results depend on those services and may vary between runs.
- Never commit your `.env` file. It is already listed in `.gitignore`.

## 👤 Author

**Abdullah Hashmi**, AI Engineer, Karachi, Pakistan
GitHub: [@abdullahhashmidev](https://github.com/abdullahhashmidev)
