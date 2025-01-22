from modules.auth import create_service
from modules.calendar_operations import clear_day, list_events
from modules.parser import parse_academic_calendar
from modules.scheduler import apply_holidays, apply_working_saturdays
import sys


def main():
    """
    Main entry point for the CLI application.

    This function initializes the Google Calendar API service and provides a menu 
    to perform various calendar operations interactively.
    """
    service = create_service()
    corr_date = {'Mon':'2025-01-06', 'Tue':'2025-01-07', 'Wed':'2025-01-08', 'Thu':'2025-01-09', 'Fri':'2025-01-10'}
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        if choice == '1':
            date = input("Enter the date to clear (YYYY-MM-DD): ")
            events_cleared = clear_day(service, date)
            print(f"Cleared {events_cleared} events for {date}.")
        elif choice == '2':
            template_day = input("Enter the template day (YYYY-MM-DD): ")
            working_saturdays = input("Enter working Saturdays (comma-separated YYYY-MM-DD): ").split(',')
            apply_working_saturdays(service, working_saturdays, template_day)
            print("Working Saturdays added successfully.")
        elif choice == '3':
            file_path = input("Enter the path to the academic calendar file: ")
            with open(file_path, 'r') as f:
                text = f.read()
            holidays, working_saturdays = parse_academic_calendar(text)
            print(f"Holidays: {holidays}")
            print(f"Working Saturdays: {working_saturdays}")
        elif choice == '4':
            print("Exiting application.")
            sys.exit()
        else:
            print("Invalid choice. Please try again.")