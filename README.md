# 🕒 Time Agent using Google ADK

A simple AI agent built using **Google's Agent Development Kit (ADK)** and **Gemini 2.5** that tells you the current time in any major city 🌍.

---

## 🚀 Running the Agent

### Clone this repo:
```bash
git clone https://github.com/Sangivi-Ganesh/time-agent-adk.git
cd time-agent-adk

###Activate your virtual environment:
python -m venv .venv
.\.venv\Scripts\activate

###Run your agent: 
adk run my_agent

###Example interaction:
[user]: What time is it in Tokyo?
[time_agent]: The current time in Tokyo is 08:42 PM.


🧠 How it works
The agent uses a simple tool function:
def get_current_time(city: str) -> dict:

🫶 Credits
Built while learning Google ADK and Gemini
Inspired by the Kaggle “Your First AI Agent” course ✨

