# Importing the FileHandler module to handle binary file operations.
from binary_file_handler import FileHandler

# Defining a class called Guest to manage guest data.
class Guest:
    # Constructor method to initialize guest attributes.
    def __init__(self, guest_id, name, address, contact_details):
        # List to store guest data.
        self.guests = []
        # Assigning attributes with provided values.
        self.guest_id = guest_id
        self.name = name
        self.address = address
        self.contact_details = contact_details

    # Method to add a new guest to the list and save to file.
    def add_guest(self, guest_data):
        # Appending guest data to the list.
        self.guests.append(guest_data)
        # Writing the updated list to a binary file.
        FileHandler.write_to_binary_file(self.guests, 'guests.pkl')

    # Method to read guest data from file.
    def read_guests_from_file(self):
        # Returning guest data read from the binary file.
        return FileHandler.read_from_binary_file('guests.pkl')

    # Method to delete a guest by their ID.
    def delete_guest_by_id(self, guest_id):
        # Reading guest data from the file.
        guests = self.read_guests_from_file()
        # If there are guests in the file:
        if guests:
            # Iterating through each guest.
            for guest in guests:
                # Checking if the guest ID matches the provided ID.
                if guest.get('Guest ID') == guest_id:
                    # Removing the guest from the list.
                    guests.remove(guest)
                    # Writing the updated list back to the file.
                    FileHandler.write_to_binary_file(guests, 'guests.pkl')
                    # Returning True indicating successful deletion.
                    return True
            # Returning False if the guest ID was not found.
            return False
        # Returning False if there are no guests in the file.
        else:
            return False

    # Method to update a guest's data by their ID.
    def update_guest_by_id(self, guest_id, updated_data):
        # Reading guest data from the file.
        guests = self.read_guests_from_file()
        # If there are guests in the file:
        if guests:
            # Iterating through each guest.
            for guest in guests:
                # Checking if the guest ID matches the provided ID.
                if guest.get('Guest ID') == guest_id:
                    # Updating the guest's data with the provided data.
                    guest.update(updated_data)
                    # Writing the updated list back to the file.
                    FileHandler.write_to_binary_file(guests, 'guests.pkl')
                    # Returning True indicating successful update.
                    return True
            # Returning False if the guest ID was not found.
            return False
        # Returning False if there are no guests in the file.
        else:
            return False
