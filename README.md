# Keystroke-Logger

The Keystroke Logger Project is a Python-based tool designed to record keypress events. It's created using the `pynput` library and packaged into an executable with PyInstaller. This project is intended for educational purposes, allowing users to understand and experiment with key logging mechanisms.

**Note: This project is intended for educational purposes only and should not be used for unauthorized surveillance or in violation of privacy laws.**

## Part 1: Creating the Key Logger Script
- Utilize the existing Python file "logger.pyw".

## Part 2: Setting Up Environment
1. Ensure Python (preferably version 3.7 or 3.8) is installed and added to PATH.
-    Important: Check the box that says "Add Python to PATH" before installation. This step is crucial for running Python from the command line.
2. Install the `pynput` library, which is used to monitor and control input devices:
-   `pip install pynput`.

## Part 3: Making the Python File Executable
 1. Install PyInstaller using pip. It's recommended to do this in a virtual environment:
-  `pip install pyinstaller`.
 2. Compile the script:
  - Open the command prompt in the directory where your script is located.
  -  Run PyInstaller with the --onefile option: - 
  -  `pyinstaller --onefile logger.pyw`.

## Part 4: Locating the Executable
- The executable can be found in the `dist` folder within the script's directory.

## Part 5: Using the Executable
- The compiled executable can be used independently. All other files can be deleted.
- ++ You can use the `Autorun` file, simply put it in the same usb with the executable... **Newst windows do not allow to auto-run from usb

##
**Note:** The executable is designed to be undetectable by standard antivirus programs.

**Disclaimer:** This project is created strictly for educational purposes and should be used responsibly.

** This project was created by dimitrisss


