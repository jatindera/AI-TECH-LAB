=========================
AI Tech Lab - Getting Started
=========================

This workspace is a curated collection of structured learning paths, experiments, and agent-based projects using:

- MLOps
- Google ADK
- LangChain
- LangGraph
- Microsoft Agentic Framework
- Semantic Kernel
- A2A Protocol
- MCP Protocol

The goal is to explore and build agent-centric AI systems using modern frameworks in isolated, organized environments.

-------------------
1. Clone the Project
-------------------

   git clone https://github.com/jatindera/ai-tech-lab.git
   cd ai-tech-lab

---------------------------------------------------
2. Create and Activate a Python Virtual Environment
---------------------------------------------------

To isolate your dependencies, create a `.venv` in the root directory.

🐧 For **Linux/macOS**:
   python3 -m venv .venv
   source .venv/bin/activate

🪟 For **Windows (Command Prompt)**:
   python -m venv .venv
   .venv\Scripts\activate.bat

🪟 For **Windows (PowerShell)**:
   python -m venv .venv
   .venv\Scripts\Activate.ps1

> Once activated, your terminal prompt will change to include `(.venv)`

-----------------------
3. Install `uv` Package Manager
-----------------------

Inside the activated virtual environment, install `uv`:

   pip install uv

You can now use `uv` to manage dependencies, environments, and speed up installs.

----------------------------------------
4. Navigate to a Module and Install Deps
----------------------------------------

Each module (e.g., LangChain, Google ADK) has its own folder with a `requirements.txt` or `uv.config.toml`.

Example (Google ADK FastAPI Agent):

   cd google-adk/advanced/FastAPI-AgentServe
   uv pip install -r requirements.txt

> Use `uv venv` here if you prefer isolated `.venv` per project (optional)

-----------------------------
Project Structure & Readmes
-----------------------------

Each major folder in this workspace represents a topic or tech stack:

- mlops/
- google-adk/
- langchain/
- langgraph/
- semantic-kernel/
- microsoft-agentic/
- a2a-protocol/
- mcp-protocol/
- projects/

Each of these has its own `README.md` file explaining how to run or extend the examples inside.

Examples:
- `google-adk/advanced/FastAPI-AgentServe/README.md`
- `langchain/basics/README.md`

------------------
Environment & Files
------------------

- `.env` — Located at root; holds shared secrets like `GOOGLE_API_KEY`
- `.venv/` — Virtual environment directory (excluded from Git)
- `.gitignore` — Includes venv, cache, and editor settings

----------------
Author & License
----------------

Author: Jatinder Arora
License: MIT (or specify your own license)

-----------------
Happy Experimenting!
-----------------
