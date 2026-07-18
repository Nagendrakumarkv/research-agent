PROMPT:

Act as a Senior AI Engineer and my expert mentor. I have just completed a 10-day bootcamp on building Agentic AI from scratch using the new `google-genai` Python SDK. I understand function calling, manual memory management (context windows), the ReAct framework (Thought/Action/Observation), and graceful error handling.

My goal now is to build a production-level **Deep-Research Agent** in Python over the next 5 days. This agent should be able to take a complex research prompt, use tools to gather facts, calculate data if needed, and write a final formatted report to my local hard drive.

Here is the exact folder structure we will build towards:

research_agent/
│
├── main.py                 # The CLI entry point and user interface
├── config.py               # API key loading and Gemini model configuration
├── agent/
│   ├── __init__.py
│   ├── engine.py           # The robust ReAct loop (Thought/Action/Observation)
│   └── memory.py           # Class to manage the short-term memory history array
└── tools/
    ├── __init__.py
    ├── web_search.py       # Wikipedia search tool
    ├── calculator.py       # Math execution tool
    └── file_system.py      # Tool to save the final markdown report to disk

Here is the 5-Day Curriculum. Acknowledge this plan, and then ask me if I am ready to begin Day 1.

*   **Day 1: Setup & Configuration.** We will set up the virtual environment, create the folder structure, and write `config.py` to securely handle the Gemini API initialization.
*   **Day 2: The Tool Registry.** We will build `web_search.py`, `calculator.py`, and `file_system.py`. We will ensure they have perfect docstrings and type hints for the Gemini API, and include `try/except` blocks to handle failures gracefully.
*   **Day 3: Memory Management.** We will write `memory.py`. Instead of a raw list, we will build a Python class that abstracts away the appending of `types.Content` objects for User prompts, Model responses, and Tool observations.
*   **Day 4: The ReAct Engine.** We will write `engine.py`. This is the core logic. We will import the tools and memory, define the strict System Persona, and build the resilient `while` loop that handles the Thought -> Action -> Observation cycle and prevents infinite loops.
*   **Day 5: The CLI & Integration.** We will write `main.py` to tie it all together. We will build a clean terminal interface where a user can enter a research goal, watch the agent's internal monologue stream in real-time, and get a success message when the report is saved.

**Rules for our interaction:**
1.  **Strict Pacing:** We will do ONLY one day at a time. Do not generate code for future days until I say "I am ready for Day X".
2.  **Modular Code:** Ensure the code is modular. The agent engine should not care how the tools work under the hood, it should just call them.
3.  **Modern SDK:** Use the current `google-genai` SDK and its `types` module for all configurations and memory management.

Do you understand these instructions? If so, summarize the final product we are building and ask me to begin Day 1.

-----------------------------------------------------------------------------------

python -m venv .venv

.venv\Scripts\activate

------------------------------------------------------------------------------------