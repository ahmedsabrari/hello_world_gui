"""
Main class for the Tkinter application.
"""
import tkinter as tk
from tkinter import ttk

from .widgets import create_button, create_label
from .styles import configure_styles
import logic.functions as logic

class App:
    """Main class for the GUI application"""
    
    def __init__(self):
        """Initialize the application"""
        self.root = tk.Tk()
        self.root.title("Hello World GUI")
        self.root.geometry("400x300")
        self.root.resizable(True, True)
        
        # Configure styles
        configure_styles()
        
        # Application variables
        self.message_var = tk.StringVar(value="Welcome!")
        
        # Create the UI
        self.setup_ui()
        
        # Bind events
        self.bind_events()
    
    def setup_ui(self):
        """Create the UI"""
        # Main frame
        main_frame = ttk.Frame(self.root, padding="20")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Allow the frame to expand with the window
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        main_frame.columnconfigure(1, weight=1)
        main_frame.rowconfigure(3, weight=1)
        
        # Main label
        self.label = create_label(main_frame, self.message_var, style="Title.TLabel")
        self.label.grid(row=0, column=0, columnspan=2, pady=(0, 20))
        
        # Welcome button
        self.hello_button = create_button(
            main_frame, 
            "Welcome", 
            command=lambda: logic.update_message(self.message_var, "Hello, World!")
        )
        self.hello_button.grid(row=1, column=0, pady=10, sticky=tk.E)
        
        # Goodbye button
        self.goodbye_button = create_button(
            main_frame, 
            "Goodbye", 
            command=lambda: logic.update_message(self.message_var, "Goodbye!")
        )
        self.goodbye_button.grid(row=1, column=1, pady=10, sticky=tk.W)
        
        # Settings button
        self.settings_button = create_button(
            main_frame,
            "Settings",
            command=lambda: logic.open_settings(self.root, self.message_var)
        )
        self.settings_button.grid(row=2, column=0, columnspan=2, pady=10)
        
        # Input field
        ttk.Label(main_frame, text="Enter text:").grid(row=3, column=0, sticky=tk.W, pady=(20, 5))
        self.entry_var = tk.StringVar()
        entry = ttk.Entry(main_frame, textvariable=self.entry_var)
        entry.grid(row=3, column=1, sticky=(tk.W, tk.E), pady=(20, 5))
        
        # Button to update the message with the input text
        self.update_button = create_button(
            main_frame,
            "Update Message",
            command=lambda: logic.update_message(self.message_var, self.entry_var.get())
        )
        self.update_button.grid(row=4, column=0, columnspan=2, pady=10)
    
    def bind_events(self):
        """Bind application events"""
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
    
    def on_closing(self):
        """Handle the window closing event"""
        if logic.confirm_exit(self.root):
            self.root.destroy()
    
    def run(self):
        """Run the application"""
        self.root.mainloop()