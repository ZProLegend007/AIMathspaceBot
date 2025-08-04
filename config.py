# Configuration file for AI Mathspace Bot

# OpenAI API settings
OPENAI_API_KEY = "" # Enter your API key
OPENAI_MODEL = "gpt-4o"
MAX_TOKENS = 150
TEMPERATURE = 0.1

# Screenshot settings
SCREENSHOT_FORMAT = "JPEG"
SCREENSHOT_QUALITY = 90

# Timing settings (in seconds)
STARTUP_DELAY = 3
CLIPBOARD_DELAY = 0.5

# Prompt for GPT-4
SYSTEM_PROMPT = """Please solve this math question from the screenshot. Provide only the final answer in the most concise form possible. If it's a multiple choice question, provide the letter and answer. If it's a calculation, provide just the numerical result. Do not include explanations or working steps."""
