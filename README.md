# Hello World GUI

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Tests Status](https://img.shields.io/badge/tests-passing-brightgreen)](https://github.com/ahmedsabrari/hello_world_gui/actions)
[![Code Style: Black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

A professional, extensible "Hello World" GUI application built with Python and Tkinter, featuring a clean separation between UI components and business logic.

![Hello World GUI Screenshot](assets/images/Welcome.jpg)
![Hello World GUI Screenshot](assets/images/Goodbye.jpg)
![Hello World GUI Screenshot](assets/images/New_message.jpg)
![Hello World GUI Screenshot](assets/images/New_message_1.jpg)
![Hello World GUI Screenshot](assets/images/Update_message.jpg)

## 📖 About The Project

Hello World GUI is a demonstration project showcasing best practices in Python GUI application development. It implements a clean architecture pattern with complete separation between the user interface and business logic, making it an excellent starting point for more complex Tkinter applications.

The application features a simple yet elegant interface with multiple interaction options, customizable messages, and a settings dialog. It serves as both a functional example and a template for building professional Python GUI applications.

### Key Features

- 🎨 Clean, modern GUI built with Tkinter
- 🧩 Modular architecture with separated UI and logic layers
- ⚙️ Customizable themes and styles
- 🔧 Extensible widget system
- 🧪 Comprehensive test suite
- 📦 Easy installation and packaging

## 🚀 Built With

- ![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white) - Primary programming language
- ![Tkinter](https://img.shields.io/badge/Tkinter-3776AB?style=for-the-badge&logo=python&logoColor=white) - GUI framework
- ![unittest](https://img.shields.io/badge/unittest-3776AB?style=for-the-badge&logo=python&logoColor=white) - Testing framework

## 📋 Prerequisites

Before installing Hello World GUI, ensure you have the following prerequisites:

- Python 3.8 or higher
- pip (Python package installer)
- Git (for development version)

### Verifying Installation

```bash
# Check Python version
python --version

# Check pip version
pip --version

# Check Git version (optional)
git --version
```

## ⚙️ Installation

### Method 1: Install from GitHub (Recommended for Development)

```bash
# Clone the repository
git clone https://github.com/ahmedsabrari/hello_world_gui.git

# Navigate to the project directory
cd hello-world-gui

# Install in development mode
pip install -e .
```

### Method 2: Manual Installation

```bash
# Download the source code
# Extract the archive and navigate to the directory

# Install dependencies (if any)
pip install -r requirements.txt

# Run directly without installation
python main.py
```

## 🎯 Usage

### Starting the Application

```bash
# After installation, run the application
hello-world-gui

# Or run directly from the source
python main.py
```

### Basic Interactions

1. Click the "Greet" button to display a welcome message
2. Click the "Farewell" button to display a goodbye message
3. Use the text input field to customize the message
4. Click the "Settings" button to open the settings dialog

### Application Settings

The application can be configured through the settings dialog or by modifying the source code:

1. UI components - Modify `gui/app.py`
2. Business logic - Update `logic/functions.py`
3. Widget styles - Customize `gui/styles.py`

## 🧪 Testing

### Running Tests

```bash
# Run all tests
python -m unittest discover tests

# Run specific test file
python -m unittest tests/test_app.py

# Run with verbose output
python -m unittest discover tests -v
```

## 🗺️ Roadmap

### Planned Features
- [ ] Multi-language support
- [ ] Additional theme options
- [ ] Plugin system for extensibility
- [ ] Advanced settings persistence
- [ ] Additional widget types
- [ ] Cross-platform packaging improvements

### Future Enhancements
- [ ] Database integration examples
- [ ] Network functionality examples
- [ ] Async operations support
- [ ] Advanced theming engine
- [ ] Component library extensions

## ❓ FAQ

### Q: Why use this architecture for a simple Hello World app?
A: This architecture demonstrates best practices that scale to complex applications, making it an excellent learning resource and foundation for real-world projects.

### Q: Can I use this for commercial projects?
A: Yes, the MIT license allows use in commercial projects with proper attribution.

### Q: How do I add new widgets?
A: Add new widget creation functions in `gui/widgets.py` and import them where needed.

### Q: How can I customize the appearance?
A: Modify the styles in `gui/styles.py` or extend the style configuration system.

### Q: Is there support for other Python GUI frameworks?
A: Currently, the project focuses on Tkinter, but the architecture could be adapted to other frameworks like PyQt or Kivy.

## 📞 Support

If you have any questions or issues:

1. Check the [documentation](https://github.com/ahmedsabrari/hello_world_gui/wiki)
2. Search existing [issues](https://github.com/ahmedsabrari/hello_world_gui/issues)
3. Create a new issue with detailed information

## 🙏 Acknowledgments

- Python Software Foundation for the excellent Python language
- The Tkinter community for documentation and examples
- Contributors who help improve this project

---

<div align="center">
Made with ❤️ by [ahmedsabrari](https://github.com/ahmedsabrari)
</div>