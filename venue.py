# Importing the FileHandler module to handle binary file operations.
from binary_file_handler import FileHandler

# Defining a class called Venue to manage venue data.
class Venue:
    # Constructor method to initialize venue attributes.
    def __init__(self, venue_id, name, address, contact, min_guests, max_guests):
        # List to store venue data.
        self.venues = []
        # Assigning attributes with provided values.
        self.venue_id = venue_id
        self.name = name
        self.address = address
        self.contact = contact
        self.min_guests = min_guests
        self.max_guests = max_guests

    # Method to add a new venue to the list and save to file.
    def add_venue(self, venue_data):
        # Appending venue data to the list.
        self.venues.append(venue_data)
        # Writing the updated list to a binary file.
        FileHandler.write_to_binary_file(self.venues, 'venues.pkl')

    # Method to read venue data from file.
    def read_venues_from_file(self):
        # Returning venue data read from the binary file.
        return FileHandler.read_from_binary_file('venues.pkl')

    # Method to delete a venue by its ID.
    def delete_venue_by_id(self, venue_id):
        # Reading venue data from the file.
        venues = self.read_venues_from_file()
        # If there are venues in the file:
        if venues:
            # Iterating through each venue.
            for venue in venues:
                # Checking if the venue ID matches the provided ID.
                if venue.get('Venue ID') == venue_id:
                    # Removing the venue from the list.
                    venues.remove(venue)
                    # Writing the updated list back to the file.
                    FileHandler.write_to_binary_file(venues, 'venues.pkl')
                    # Returning True indicating successful deletion.
                    return True
            # Returning False if the venue ID was not found.
            return False
        # Returning False if there are no venues in the file.
        else:
            return False

    # Method to update a venue's data by its ID.
    def update_venue_by_id(self, venue_id, updated_data):
        # Reading venue data from the file.
        venues = self.read_venues_from_file()
        # If there are venues in the file:
        if venues:
            # Iterating through each venue.
            for venue in venues:
                # Checking if the venue ID matches the provided ID.
                if venue.get('Venue ID') == venue_id:
                    # Updating the venue's data with the provided data.
                    venue.update(updated_data)
                    # Writing the updated list back to the file.
                    FileHandler.write_to_binary_file(venues, 'venues.pkl')
                    # Returning True indicating successful update.
                    return True
            # Returning False if the venue ID was not found.
            return False
        # Returning False if there are no venues in the file.
        else:
            return False
