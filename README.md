# Secure Password Generator (GUI + Logic)

Desktop password generator application built with Python and PyQt5.  
This project evolved from a console-based script into a fully interactive GUI application with theme switching, clipboard integration, and dynamic password length selection.

Designed to demonstrate both core Python logic and event-driven desktop application development.


## Business Problem

Weak passwords remain one of the most common security risks in personal and professional environments.

Users often:
- Create predictable passwords
- Reuse passwords across services
- Avoid complex symbols due to inconvenience
- Lack simple tools for generating secure credentials

There is a need for a lightweight, user-friendly desktop utility that generates strong, randomized passwords instantly.


## Solution

The Secure Password Generator provides a two-stage implementation:

### Phase 1 — Console Logic Version
A Python-based script that:
- Generates secure random passwords
- Uses letters, digits, and special characters
- Accepts user-defined password length
- Demonstrates understanding of Python's `random` and `string` modules

### Phase 2 — Full GUI Application (PyQt5)
A complete desktop interface that:
- Allows password length selection via slider (6–50 characters)
- Generates passwords dynamically
- Copies passwords directly to clipboard
- Supports light and dark theme modes
- Displays confirmation messages
- Uses structured layout and styled components

This project demonstrates progression from algorithmic logic to user-facing desktop software.


## Key Features

### Core Functionality
- Random secure password generation
- Adjustable password length (6–50)
- Combination of:
  - Uppercase & lowercase letters
  - Digits
  - Special symbols

### GUI Features
- QLineEdit password output field
- Interactive slider with real-time label updates
- Generate button
- Copy-to-clipboard button
- Light/Dark theme toggle
- Styled interface with custom CSS-like stylesheets
- Popup confirmation messages (QMessageBox)


## Technical Architecture

The project follows a structured object-oriented approach:

- `PasswordGenerator` class inherits from `QWidget`
- Layout management using:
  - `QVBoxLayout`
  - `QHBoxLayout`
- Event-driven logic using Qt signals & slots
- Theme management via conditional stylesheet updates
- Clipboard interaction through `QApplication.clipboard()`
- Separation between:
  - Password generation logic
  - UI interaction logic
  - Theme styling logic

This reflects real-world desktop application structuring principles.


## Development Environment

- Language: Python 3.9.6  
- GUI Library: PyQt5  
- Operating System: macOS  
- Editor: VS Code  


## Tech Stack

- Python 3.9.6  
- PyQt5  
- Built-in libraries:
  - `random`
  - `string`
  - `sys`


## Project Structure

```
secure_password_generator/
│
├── main.py              # GUI application
├── console_version.py   # Logic-only version (Phase 1)
├── requirements.txt
└── README.md
```


## Installation

1. Clone the repository:

```
git clone https://github.com/maria-python/secure_password_generator.git
cd secure_password_generator
```

2. Install dependencies:

```
pip install PyQt5
```


## Usage

Run the GUI application:

```
python main.py
```

The application window will open with:

- Password output field  
- Slider to select length  
- Generate button  
- Copy button  
- Theme toggle  


## Workflow

1. Adjust the slider to select password length  
2. Click **Generate**  
3. Password appears in the output field  
4. Click **Copy** to save it to clipboard  
5. Optionally toggle between light and dark mode  


## Results

- Demonstrates secure password generation logic  
- Shows understanding of event-driven GUI programming  
- Implements dynamic UI updates  
- Applies custom styling with Qt stylesheets  
- Integrates system clipboard functionality  
- Reflects progression from script to full desktop application  


## Learning Outcomes

- Randomized data generation in Python  
- Using `string` character sets  
- Object-oriented GUI development  
- Qt signals and slots mechanism  
- Styling widgets with CSS-like syntax  
- Managing application state (theme toggle)  


## Future Improvements

- Character-type checkboxes (letters / digits / symbols)  
- Password strength meter  
- Exclude similar characters option  
- Save generated passwords to encrypted file  
- Packaging as standalone executable (PyInstaller)  
- Unit testing for password logic  


## Author

Mariia Ilnitska  

Junior Python Automation / Tech Assistant  


**✉️ Contacts**

Gmail: maria.ilnitska11@gmail.com  

LinkedIn: www.linkedin.com/in/maria-ilnitska  

Telegram: @mariailnitska
