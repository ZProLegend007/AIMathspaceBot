# AIMathspaceBot
An AI powered python script for linux that automatically takes a screenshot of a mathspace question, sends the image to an AI, and outputs a filtered output with the plain text answer.

## Features
- Single-run execution (no continuous loop)
- Screenshot capture of math questions
- GPT-4 powered question analysis
- Automatic answer extraction to clipboard
- Clean exit after solving one question

## Setup
1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Set your OpenAI API key:
```bash
export OPENAI_API_KEY="your-api-key-here"
```

## Usage
### Method 1: Quick Demo (No API Key Required)
```bash
python3 demo_handler.py
```
This runs a demo mode that simulates the entire process without requiring an OpenAI API key.

### Method 2: Full Mode (Requires OpenAI API Key)
1. Make sure the math question is visible on your screen
2. Run the script:
```bash
python3 screenshot_handler.py
```
3. The script will take a screenshot, analyze it with GPT-4, and copy the answer to your clipboard
4. The script exits automatically after processing one question

### Method 3: Using the Setup Script
```bash
./setup_and_run.sh
```
This script will check dependencies and guide you through the setup process.

## Requirements
- Python 3.6+
- OpenAI API key
- Linux environment (for screenshot functionality)
