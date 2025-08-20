"""
Reusable UI components.
"""
import tkinter as tk
from tkinter import ttk

def create_button(parent, text, command=None, style="TButton"):
    """
    Create a button with standard settings.
    
    Args:
        parent: The parent widget
        text: The button text
        command: The callback function on click
        style: The button style
        
    Returns:
        The button object
    """
    button = ttk.Button(
        parent,
        text=text,
        command=command,
        style=style
    )
    return button

def create_label(parent, text_var, style="TLabel"):
    """
    Create a label with standard settings.
    
    Args:
        parent: The parent widget
        text_var: The text variable
        style: The label style
        
    Returns:
        The label object
    """
    label = ttk.Label(
        parent,
        textvariable=text_var,
        style=style
    )
    return label

def create_dialog(parent, title, message):
    """
    Create a dialog window.
    
    Args:
        parent: The parent widget
        title: The dialog title
        message: The dialog message
        
    Returns:
        The dialog object
    """
    dialog = tk.Toplevel(parent)
    dialog.title(title)
    dialog.geometry("300x150")
    dialog.transient(parent)
    dialog.grab_set()
    
    # Message
    label = ttk.Label(dialog, text=message, wraplength=250)
    label.pack(pady=20)
    
    # Button frame
    button_frame = ttk.Frame(dialog)
    button_frame.pack(pady=10)
    
    return dialog, button_frame