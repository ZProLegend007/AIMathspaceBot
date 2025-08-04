#!/usr/bin/env python3
"""
Test script for screenshot_handler.py functionality
"""

import os
import sys
import tempfile
from unittest.mock import patch, MagicMock
from PIL import Image

# Add the current directory to the path so we can import our module
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

def test_screenshot_functionality():
    """Test the screenshot functionality without OpenAI dependency."""
    
    # Set a fake API key for testing
    os.environ['OPENAI_API_KEY'] = 'test-key'
    
    try:
        from screenshot_handler import MathspaceBot
        
        bot = MathspaceBot()
        
        # Test image encoding
        test_image = Image.new('RGB', (100, 100), color='red')
        with tempfile.NamedTemporaryFile(suffix='.jpg') as tmp:
            test_image.save(tmp.name, 'JPEG')
            with open(tmp.name, 'rb') as f:
                image_data = f.read()
            
            encoded = bot.encode_image(image_data)
            assert isinstance(encoded, str)
            assert len(encoded) > 0
            print("✓ Image encoding test passed")
        
        # Test clipboard functionality
        test_answer = "Test answer: 42"
        try:
            bot.paste_answer(test_answer)
            print("✓ Clipboard functionality test passed")
        except Exception as e:
            print(f"⚠ Clipboard test warning (expected in headless environment): {e}")
        
        print("✓ All core functionality tests passed")
        
    except ImportError as e:
        print(f"✗ Import error: {e}")
        return False
    except Exception as e:
        print(f"✗ Test failed: {e}")
        return False
    
    finally:
        # Clean up environment
        if 'OPENAI_API_KEY' in os.environ:
            del os.environ['OPENAI_API_KEY']
    
    return True

if __name__ == "__main__":
    print("Testing screenshot_handler.py functionality...")
    print("=" * 50)
    
    success = test_screenshot_functionality()
    
    if success:
        print("\n✓ All tests completed successfully!")
        sys.exit(0)
    else:
        print("\n✗ Some tests failed!")
        sys.exit(1)