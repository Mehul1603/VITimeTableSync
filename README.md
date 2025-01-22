# Google Calendar Automation CLI

This Python project automates your Google Calendar to match your college lecture schedule. It uses the Google Calendar API to perform operations like clearing holidays, adding working Saturdays, and parsing academic calendar files.

## Features
- **Clear Holidays**: Delete all events for specified dates.
- **Working Saturdays**: Add events for Saturdays based on a template day.
- **Parse Academic Calendar**: Extract holidays and working Saturdays from text files.

## Prerequisites
1. Python 3.8+
2. `credentials.json` file for Google Calendar API authentication.

## Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/google-calendar-automation-cli.git
   cd google-calendar-automation-cli
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
Run the application:
```bash
python main.py
```

## File Structure
- `main.py`: Entry point of the application.
- `modules/`: Contains all modularized components.
- `data/`: Stores sample text files like academic calendars.
- `tests/`: Unit tests for various modules.
- `requirements.txt`: Python dependencies.
- `README.md`: Project documentation.