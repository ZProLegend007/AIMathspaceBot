#!/usr/bin/env python3
"""
Demo mode for AI Mathspace Bot - runs without OpenAI API
"""

import os
import sys
import time
import base64
import logging
from io import BytesIO
from PIL import Image, ImageGrab, ImageDraw, ImageFont

# Add current directory to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from config import *

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


class DemoMathspaceBot:
    """Demo version of MathspaceBot for testing without OpenAI API."""
    
    def __init__(self):
        """Initialize the demo bot."""
        logger.info("Demo bot initialized (no OpenAI API required)")
    
    def take_screenshot(self):
        """Take a screenshot or create a demo image."""
        try:
            logger.info("Taking screenshot...")
            
            try:
                # Try to take a real screenshot
                screenshot = ImageGrab.grab()
                logger.info(f"Real screenshot captured ({screenshot.size[0]}x{screenshot.size[1]})")
            except Exception:
                # Create a demo image if screenshot fails
                logger.info("Creating demo math question image...")
                screenshot = Image.new('RGB', (800, 600), color='white')
                draw = ImageDraw.Draw(screenshot)
                
                # Try to use a font, fall back to default if not available
                try:
                    font = ImageFont.truetype("DejaVuSans.ttf", 40)
                except:
                    font = ImageFont.load_default()
                
                # Draw a simple math question
                draw.text((50, 200), "What is 15 + 27?", fill='black', font=font)
                draw.text((50, 300), "A) 42", fill='black', font=font)
                draw.text((50, 350), "B) 43", fill='black', font=font)
                draw.text((50, 400), "C) 44", fill='black', font=font)
                draw.text((50, 450), "D) 45", fill='black', font=font)
            
            # Convert to RGB if necessary
            if screenshot.mode != 'RGB':
                screenshot = screenshot.convert('RGB')
            
            # Save to memory
            img_buffer = BytesIO()
            screenshot.save(img_buffer, format=SCREENSHOT_FORMAT, quality=SCREENSHOT_QUALITY)
            img_buffer.seek(0)
            
            return img_buffer.getvalue()
        
        except Exception as e:
            logger.error(f"Failed to create screenshot: {e}")
            raise
    
    def analyze_image(self, image_data):
        """Simulate GPT-4 analysis with a demo response."""
        logger.info("Simulating GPT-4 analysis...")
        
        # Simulate processing time
        time.sleep(2)
        
        # Return a demo answer
        demo_answer = "A) 42"
        logger.info(f"Demo analysis complete. Answer: {demo_answer}")
        return demo_answer
    
    def paste_answer(self, answer):
        """Handle answer output in demo mode."""
        try:
            logger.info(f"Demo answer: {answer}")
            print(f"\n🎯 Demo Answer: {answer}")
            print("📋 In real mode, this would be copied to your clipboard.")
            
        except Exception as e:
            logger.warning(f"Demo output error: {e}")
            print(f"\n🎯 Demo Answer: {answer}")
    
    def run(self):
        """Run the demo bot."""
        try:
            logger.info("Starting AI Mathspace Bot (DEMO MODE)")
            print("🔧 Running in DEMO MODE - no OpenAI API required")
            print()
            
            # Take screenshot
            image_data = self.take_screenshot()
            
            # Simulate analysis
            answer = self.analyze_image(image_data)
            
            # Output answer
            self.paste_answer(answer)
            
            logger.info("Demo execution completed successfully")
            print("\n✅ Demo completed! To use real mode, set OPENAI_API_KEY and run screenshot_handler.py")
            
        except KeyboardInterrupt:
            logger.info("Demo interrupted by user")
            sys.exit(0)
        except Exception as e:
            logger.error(f"Demo execution failed: {e}")
            sys.exit(1)


def main():
    """Main entry point for demo mode."""
    print("🚀 AI Mathspace Bot - DEMO MODE")
    print("=" * 40)
    print("This demo will:")
    print("1. Take a screenshot (or create a demo image)")
    print("2. Simulate GPT-4 analysis")
    print("3. Show a demo answer")
    print("4. Exit")
    print("\n📝 No OpenAI API key required for demo mode.")
    print("Press Ctrl+C to cancel at any time.")
    print()
    
    # Give user time to prepare
    try:
        for i in range(STARTUP_DELAY, 0, -1):
            print(f"Starting demo in {i}...")
            time.sleep(1)
        print("Starting demo now!")
        print()
    except KeyboardInterrupt:
        print("\nDemo cancelled by user.")
        sys.exit(0)
    
    # Run the demo bot
    bot = DemoMathspaceBot()
    bot.run()


if __name__ == "__main__":
    main()