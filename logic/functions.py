"""
Business logic and event handling for the application.
"""
import tkinter as tk
from tkinter import ttk, messagebox

from gui.widgets import create_button, create_dialog

def update_message(message_var, new_message):
    """
    Update the displayed message.
    
    Args:
        message_var: The message variable
        new_message: The new message
    """
    if new_message.strip():
        message_var.set(new_message)
    else:
        message_var.set("Empty message!!")

def confirm_exit(parent):
    """
    Confirm exit from the application.
    
    Args:
        parent: The parent widget
        
    Returns:
        bool: True if confirmed, False if canceled
    """
    result = messagebox.askyesno(
        "Confirm Exit",
        "Are you sure you want to exit?",
        parent=parent
    )
    return result

def open_settings(parent, message_var):
    """
    Open the settings window.
    
    Args:
        parent: The parent widget
        message_var: The message variable
    """
    dialog, button_frame = create_dialog(parent, "Settings", "Customize welcome message:")
    
    # Input field for settings
    settings_var = tk.StringVar()
    entry = ttk.Entry(dialog, textvariable=settings_var, width=30)
    entry.pack(pady=10)
    
    # Save button
    save_button = create_button(
        button_frame,
        "Save",
        command=lambda: save_settings(settings_var, message_var, dialog),
        style="Primary.TButton"
    )
    save_button.pack(side=tk.LEFT, padx=5)
    
    # Cancel button
    cancel_button = create_button(
        button_frame,
        "Cancel",
        command=dialog.destroy
    )
    cancel_button.pack(side=tk.LEFT, padx=5)

def save_settings(settings_var, message_var, dialog):
    """
    Save the customized settings.
    
    Args:
        settings_var: The settings variable
        message_var: The message variable
        dialog: The dialog window
    """
    new_message = settings_var.get().strip()
    if new_message:
        message_var.set(new_message)
        dialog.destroy()
    else:
        messagebox.showwarning("Warning", "Please enter a valid message!", parent=dialog)