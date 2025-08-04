#!/usr/bin/env python3
"""
AI Mathspace Bot - Screenshot Handler
A single-run script that takes a screenshot, sends it to GPT-4 for analysis,
and pastes the answer.
"""

import os
import sys
import time
import base64
import logging
from io import BytesIO
from PIL import Image, ImageGrab
import pyperclip
import requests
from openai import OpenAI

# Import configuration
from config import *

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


class MathspaceBot:
    """AI-powered bot for solving Mathspace questions."""
    
    def __init__(self):
        """Initialize the bot with OpenAI client."""
        self.client = None
        self._setup_openai()
    
    def _setup_openai(self):
        """Setup OpenAI client with API key."""
        api_key = os.getenv('OPENAI_API_KEY')
        if not api_key:
            logger.error("OPENAI_API_KEY environment variable not set")
            sys.exit(1)
        
        self.client = OpenAI(api_key=api_key)
        logger.info("OpenAI client initialized successfully")
    
    def take_screenshot(self):
        """Take a screenshot of the current screen."""
        try:
            logger.info("Taking screenshot...")
            screenshot = ImageGrab.grab()
            
            # Convert to RGB if necessary
            if screenshot.mode != 'RGB':
                screenshot = screenshot.convert('RGB')
            
            # Save to memory as JPEG
            img_buffer = BytesIO()
            screenshot.save(img_buffer, format=SCREENSHOT_FORMAT, quality=SCREENSHOT_QUALITY)
            img_buffer.seek(0)
            
            logger.info(f"Screenshot captured successfully ({screenshot.size[0]}x{screenshot.size[1]})")
            return img_buffer.getvalue()
        
        except Exception as e:
            logger.error(f"Failed to take screenshot: {e}")
            raise
    
    def encode_image(self, image_data):
        """Encode image data to base64."""
        return base64.b64encode(image_data).decode('utf-8')
    
    def analyze_image(self, image_data):
        """Send image to GPT-4 for analysis and get the answer."""
        try:
            logger.info("Sending image to GPT-4 for analysis...")
            
            base64_image = self.encode_image(image_data)
            
            response = self.client.chat.completions.create(
                model=OPENAI_MODEL,
                messages=[
                    {
                        "role": "user",
                        "content": [
                            {
                                "type": "text",
                                "text": SYSTEM_PROMPT
                            },
                            {
                                "type": "image_url",
                                "image_url": {
                                    "url": f"data:image/jpeg;base64,{base64_image}"
                                }
                            }
                        ]
                    }
                ],
                max_tokens=MAX_TOKENS,
                temperature=TEMPERATURE
            )
            
            answer = response.choices[0].message.content.strip()
            logger.info(f"GPT-4 analysis complete. Answer: {answer}")
            return answer
        
        except Exception as e:
            logger.error(f"Failed to analyze image with GPT-4: {e}")
            raise
    
    def paste_answer(self, answer):
        """Copy answer to clipboard and simulate paste."""
        try:
            logger.info(f"Copying answer to clipboard: {answer}")
            pyperclip.copy(answer)
            
            # Small delay to ensure clipboard is updated
            time.sleep(CLIPBOARD_DELAY)
            
            logger.info("Answer copied to clipboard successfully")
            print(f"\nAnswer: {answer}")
            print("The answer has been copied to your clipboard.")
            
        except Exception as e:
            logger.warning(f"Could not copy to clipboard (likely headless environment): {e}")
            print(f"\nAnswer: {answer}")
            print("Could not copy to clipboard - please copy the answer manually.")
    
    def run(self):
        """Main execution method - runs once and exits."""
        try:
            logger.info("Starting AI Mathspace Bot (single-run mode)")
            
            # Take screenshot
            image_data = self.take_screenshot()
            
            # Analyze with GPT-4
            answer = self.analyze_image(image_data)
            
            # Copy answer to clipboard
            self.paste_answer(answer)
            
            logger.info("Bot execution completed successfully")
            
        except KeyboardInterrupt:
            logger.info("Bot execution interrupted by user")
            sys.exit(0)
        except Exception as e:
            logger.error(f"Bot execution failed: {e}")
            sys.exit(1)


def main():
    """Main entry point."""
    print("AI Mathspace Bot - Single Run Mode")
    print("=" * 40)
    print("This script will:")
    print("1. Take a screenshot of your screen")
    print("2. Send it to GPT-4 for analysis")
    print("3. Copy the answer to your clipboard")
    print("4. Exit")
    print("\nMake sure you have the math question visible on your screen.")
    print("Press Ctrl+C to cancel at any time.")
    print()
    
    # Give user time to prepare
    try:
        for i in range(STARTUP_DELAY, 0, -1):
            print(f"Starting in {i}...")
            time.sleep(1)
        print("Starting now!")
        print()
    except KeyboardInterrupt:
        print("\nCancelled by user.")
        sys.exit(0)
    
    # Run the bot
    bot = MathspaceBot()
    bot.run()


if __name__ == "__main__":
    main()
