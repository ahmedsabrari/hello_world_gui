"""
Customize styles and appearance for the application.
"""
import tkinter as tk
from tkinter import ttk

def configure_styles():
    """Configure the application styles"""
    style = ttk.Style()
    
    # Button styles
    style.configure("TButton", 
                   padding=6, 
                   font=("Arial", 12))
    
    style.configure("Primary.TButton",
                   padding=6,
                   font=("Arial", 12, "bold"),
                   foreground="white",
                   background="#0078D7")
    
    # Label styles
    style.configure("TLabel",
                   font=("Arial", 11))
    
    style.configure("Title.TLabel",
                   font=("Arial", 16, "bold"),
                   foreground="#0078D7")
    
    # Frame styles
    style.configure("TFrame",
                   background="#F0F0F0")
    
    # Entry field styles
    style.configure("TEntry",
                   font=("Arial", 11),
                   padding=5)