def list_events(service, date):
    """
    List all events for a specific date from the Google Calendar.

    Args:
        service (googleapiclient.discovery.Resource): Authorized Google Calendar API service instance.
        date (str): Date in YYYY-MM-DD format.

    Returns:
        list: A list of events for the specified date.
    """
    events_result = service.events().list(
        calendarId='primary',
        timeMin=f"{date}T00:00:00Z",
        timeMax=f"{date}T23:59:59Z",
        singleEvents=True,
        orderBy='startTime'
    ).execute()
    return events_result.get('items', [])

def clear_day(service, date):
    """
    Clear all events marked as "banana" color for a specific date.

    Args:
        service (googleapiclient.discovery.Resource): Authorized Google Calendar API service instance.
        date (str): Date in YYYY-MM-DD format.

    Returns:
        int: Number of events cleared.
    """
    events = list_events(service, date)
    cleared_events = 0
    for event in events:
        if 'colorId' in event and event['colorId'] == '5':  # '5' corresponds to "banana" color in Google Calendar
            service.events().delete(calendarId='primary', eventId=event['id']).execute()
            cleared_events += 1
    return cleared_events

def add_event(service, event):
    """
    Add a new event to the Google Calendar.

    Args:
        service (googleapiclient.discovery.Resource): Authorized Google Calendar API service instance.
        event (dict): Event details as a dictionary.

    Returns:
        dict: The created event resource.
    """
    event['colorId'] = 5
    return service.events().insert(calendarId='primary', body=event).execute()