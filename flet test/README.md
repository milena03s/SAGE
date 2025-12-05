# Flet Mobile App

A blank mobile application template built with [Flet](https://flet.dev/), a framework for building beautiful multi-platform apps with Python.

## Project Structure

```
.
├── main.py              # Main application file
├── requirements.txt     # Python dependencies
└── README.md           # This file
```

## Prerequisites

- Python 3.9 or higher
- pip (Python package manager)

## Installation

1. Install dependencies:
```bash
pip install -r requirements.txt
```

## Running the App

Run the application with:
```bash
python main.py
```

The app will open in a window. You can interact with the UI elements to test functionality.

## Building for Mobile

To build for iOS or Android, use the Flet CLI:

### Android APK
```bash
flet build apk
```

### iOS
```bash
flet build ipa
```

For detailed build instructions, see the [Flet documentation](https://flet.dev/docs/publish).

## Features

- Clean, responsive UI layout
- Button with click event handling
- SnackBar notifications
- Cross-platform compatibility (Windows, macOS, Linux, iOS, Android, Web)

## Customization

Edit `main.py` to:
- Add new UI components
- Create custom layouts
- Implement business logic
- Add navigation and routing

## Resources

- [Flet Documentation](https://flet.dev/docs)
- [Flet Gallery](https://flet.dev/gallery)
- [Python Documentation](https://www.python.org/doc/)
