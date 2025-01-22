from datetime import datetime

def format_date(date):
    """
    Format a date string into a human-readable format.

    Args:
        date (str): Date in YYYY-MM-DD format.

    Returns:
        str: Formatted date string.
    """
    return datetime.strptime(date, '%Y-%m-%d').strftime('%A, %d %B %Y')

def log(message):
    """
    Log a message to the console.

    Args:
        message (str): Message to log.
    """
    print(f"[LOG] {message}")