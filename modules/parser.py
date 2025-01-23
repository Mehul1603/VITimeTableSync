import re

# Function to parse the text into calendar items
def parse_calendar(text, month, year):
    """
    Parse academic calendar text to extract holidays and working Saturdays.

    Args:
        text (str): Multiline string containing academic calendar details.

    Returns:
        tuple: A tuple containing two lists - holidays and working Saturdays.
    """

    # Regex to match a date followed by an event
    pattern = r"(\d+)([^\d].*)"
    matches = re.findall(pattern, text)
    calendar = []
    holidays = []
    working_saturdays = []

    # Clean and add each match to the calendar
    for date, event in matches:
        # Remove extra spaces and newlines
        event_cleaned = event.strip()
        if len(date)==1:
            date = "0" + date
        calendar.append([date, event_cleaned])
    
    for date, event in calendar:
        if event:
            if event == "Instructional Day":
                continue
            if "Instructional Day(" in event and event[18:21] in ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]:
                working_saturdays.append([f"{year}-{month}-{date}", event[18:21]])
                continue
            if "Instructional Day(" in event and "No Instructional Day" not in event:
                continue
        holidays.append(f"{year}-{month}-{date}")
    return holidays, working_saturdays
