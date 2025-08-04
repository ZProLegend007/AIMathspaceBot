#!/bin/bash
# Example usage script for AI Mathspace Bot

echo "AI Mathspace Bot Setup and Usage Example"
echo "======================================="
echo

# Check if Python 3 is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is not installed. Please install Python 3.6 or later."
    exit 1
fi

echo "✓ Python 3 is installed"

# Check if pip is installed
if ! command -v pip3 &> /dev/null && ! command -v pip &> /dev/null; then
    echo "❌ pip is not installed. Please install pip."
    exit 1
fi

echo "✓ pip is installed"

# Install dependencies
echo "📦 Installing dependencies..."
pip3 install -r requirements.txt

# Check if OpenAI API key is set
if [ -z "$OPENAI_API_KEY" ]; then
    echo
    echo "⚠️  OPENAI_API_KEY environment variable is not set"
    echo "   Please set your OpenAI API key:"
    echo "   export OPENAI_API_KEY='your-api-key-here'"
    echo
    echo "   You can get an API key from: https://platform.openai.com/api-keys"
    echo
    exit 1
fi

echo "✓ OpenAI API key is set"

# Check for clipboard support
if ! command -v xclip &> /dev/null && ! command -v xsel &> /dev/null; then
    echo
    echo "⚠️  No clipboard utility found. Installing xclip for clipboard support..."
    echo "   You may need to run: sudo apt-get install xclip"
    echo
fi

echo
echo "🚀 Setup complete! You can now run the bot:"
echo "   python3 screenshot_handler.py"
echo
echo "📝 Make sure to have a math question visible on your screen before running the script."
echo