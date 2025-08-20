#!/usr/bin/env python3
"""
Main entry point for the Hello World GUI application.
"""
import sys
import os

# Add the package path to the system path
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

from gui.app import App

def main():
    """Main function to run the application"""
    app = App()
    app.run()

if __name__ == "__main__":
    main()