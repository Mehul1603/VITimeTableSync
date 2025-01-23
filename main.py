from modules.auth import create_service
from modules.parser import parse_calendar
from modules.scheduler import apply_holidays, apply_working_saturdays
import sys

def display_menu():
    """
    Display the main menu for the CLI application.
    """
    print("\nGoogle Calendar Automation CLI")
    print("1. Parse Academic Calendar")
    print("2. Setup Timetable")
    print("3. Exit")

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
            print("Paste the copied text from Calendar into temp_file")
            year = input("Enter the year: ")
            month = input("Enter the month (01, 02, 03...): ")
            with open("temp_file.txt", "r") as f:
                text = f.read()
            holidays, working_saturdays = parse_calendar(text, month, year)
            apply_holidays(service, holidays)
            apply_working_saturdays(service, working_saturdays, corr_date)

        elif choice == '2':
            print("Functionality not implemented yet.")

        elif choice == '3':
            print("Exiting application.")
            sys.exit()

        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()