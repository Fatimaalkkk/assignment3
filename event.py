# Importing the FileHandler module to handle binary file operations.
from binary_file_handler import FileHandler

# Defining a class called Event to manage event data.
class Event:
    # Constructor method to initialize event attributes.
    def __init__(self, event_id, event_type, theme, date, time, duration, venue_address, client_id, guest_list, company, invoice):
        # List to store event data.
        self.events = []
        # Assigning attributes with provided values.
        self.event_id = event_id
        self.event_type = event_type
        self.theme = theme
        self.date = date
        self.time = time
        self.duration = duration
        self.venue_address = venue_address
        self.client_id = client_id
        self.guest_list = guest_list
        self.company = company
        self.invoice = invoice

    # Method to add a new event to the list and save to file.
    def add_event(self, event_data):
        # Appending event data to the list.
        self.events.append(event_data)
        # Writing the updated list to a binary file.
        FileHandler.write_to_binary_file(self.events, 'events.pkl')

    # Method to read event data from file.
    def read_events_from_file(self):
        # Returning event data read from the binary file.
        return FileHandler.read_from_binary_file('events.pkl')

    # Method to delete an event by its ID.
    def delete_event_by_id(self, event_id):
        # Reading event data from the file.
        events = self.read_events_from_file()
        # If there are events in the file:
        if events:
            # Iterating through each event.
            for event in events:
                # Checking if the event ID matches the provided ID.
                if event.get('Event ID') == event_id:
                    # Removing the event from the list.
                    events.remove(event)
                    # Writing the updated list back to the file.
                    FileHandler.write_to_binary_file(events, 'events.pkl')
                    # Returning True indicating successful deletion.
                    return True
            # Returning False if the event ID was not found.
            return False
        # Returning False if there are no events in the file.
        else:
            return False

    # Method to update an event's data by its ID.
    def update_event_by_id(self, event_id, updated_data):
        # Reading event data from the file.
        events = self.read_events_from_file()
        # If there are events in the file:
        if events:
            # Iterating through each event.
            for event in events:
                # Checking if the event ID matches the provided ID.
                if event.get('Event ID') == event_id:
                    # Updating the event's data with the provided data.
                    event.update(updated_data)
                    # Writing the updated list back to the file.
                    FileHandler.write_to_binary_file(events, 'events.pkl')
                    # Returning True indicating successful update.
                    return True
            # Returning False if the event ID was not found.
            return False
        # Returning False if there are no events in the file.
        else:
            return False
