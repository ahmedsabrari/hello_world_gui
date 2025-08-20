"""
Unit tests for the business logic.
"""
import unittest
import tkinter as tk
from unittest.mock import MagicMock, patch

import logic.functions as logic

class TestAppLogic(unittest.TestCase):
    """Test the application's business logic"""
    
    def setUp(self):
        """Set up the test environment"""
        self.root = tk.Tk()
        self.message_var = tk.StringVar(value="Initial message")
    
    def tearDown(self):
        """Clean up the test environment"""
        self.root.destroy()
    
    def test_update_message_with_valid_text(self):
        """Test updating the message with valid text"""
        # Execute
        logic.update_message(self.message_var, "New message")
        
        # Assert
        self.assertEqual(self.message_var.get(), "New message")
    
    def test_update_message_with_empty_text(self):
        """Test updating the message with empty text"""
        # Execute
        logic.update_message(self.message_var, "")
        
        # Assert
        self.assertEqual(self.message_var.get(), "Empty message!")
    
    def test_update_message_with_whitespace(self):
        """Test updating the message with whitespace only"""
        # تنفيذ
        logic.update_message(self.message_var, "   ")
        
        # التحقق
        self.assertEqual(self.message_var.get(), "Empty message!!")
    
    @patch('logic.functions.messagebox.askyesno')
    def test_confirm_exit_yes(self, mock_askyesno):
        """Test confirming exit with 'Yes' option"""
        # Setup
        mock_askyesno.return_value = True
        
        # Execute
        result = logic.confirm_exit(self.root)
        
        # Assert
        self.assertTrue(result)
        mock_askyesno.assert_called_once_with(
            "Confirm Exit",
            "Are you sure you want to exit?",
            parent=self.root
        )
    
    @patch('logic.functions.messagebox.askyesno')
    def test_confirm_exit_no(self, mock_askyesno):
        """Test confirming exit with 'No' option"""
        # Setup
        mock_askyesno.return_value = False
        
        # Execute
        result = logic.confirm_exit(self.root)
        
        # Assert
        self.assertFalse(result)
        mock_askyesno.assert_called_once_with(
            "Confirm Exit",
            "Are you sure you want to exit?",
            parent=self.root
        )

if __name__ == "__main__":
    unittest.main()