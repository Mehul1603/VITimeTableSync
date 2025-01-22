from datetime import datetime, timedelta

def apply_holidays(service, holidays):
    """
    Clear all events for the specified holiday dates.

    Args:
        service (googleapiclient.discovery.Resource): Authorized Google Calendar API service instance.
        holidays (list): List of holiday dates in YYYY-MM-DD format.
    """
    for holiday in holidays:
        clear_day(service, holiday)

def apply_working_saturdays(service, working_saturdays, corr_date):
    """
    Add events to working Saturdays based on a template day's schedule.

    Args:
        service (googleapiclient.discovery.Resource): Authorized Google Calendar API service instance.
        working_saturdays (list): List of working Saturday dates in YYYY-MM-DD format.
        template_day (str): Template day in YYYY-MM-DD format to copy events from.
    """
    
    for saturday in working_saturdays:
        events = list_events(service, corr_date[saturday[1]])
        for event in events:
            event_copy = {
                'summary': event['summary'],
                'location': event['location'],
                'start': {'dateTime': event['start']['dateTime'], 'timeZone': event['start']['timeZone']},
                'end': {'dateTime': event['end']['dateTime'], 'timeZone': event['end']['timeZone']},
            }
            start_date = datetime.fromisoformat(event_copy['start']['dateTime'])
            end_date = datetime.fromisoformat(event_copy['end']['dateTime'])
            delta = datetime.fromisoformat(saturday[0]) - datetime.fromisoformat(corr_date[saturday[1]])
            event_copy['start']['dateTime'] = (start_date + delta).isoformat()
            event_copy['end']['dateTime'] = (end_date + delta).isoformat()
            add_event(service, event_copy)
