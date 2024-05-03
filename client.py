# Importing the FileHandler module to handle binary file operations.
from binary_file_handler import FileHandler

# Defining a class called Client to manage client data.
class Client:
    # Constructor method to initialize client attributes.
    def __init__(self, client_id, name, address, contact_details, budget):
        # List to store client data.
        self.clients = []
        # Assigning attributes with provided values.
        self.client_id = client_id
        self.name = name
        self.address = address
        self.contact_details = contact_details
        self.budget = budget

    # Method to add a new client to the list and save to file.
    def add_client(self, client_data):
        # Appending client data to the list.
        self.clients.append(client_data)
        # Writing the updated list to a binary file.
        FileHandler.write_to_binary_file(self.clients, 'clients.pkl')

    # Method to read client data from file.
    def read_clients_from_file(self):
        # Returning client data read from the binary file.
        return FileHandler.read_from_binary_file('clients.pkl')

    # Method to delete a client by their ID.
    def delete_client_by_id(self, client_id):
        # Reading client data from the file.
        clients = self.read_clients_from_file()
        # If there are clients in the file:
        if clients:
            # Iterating through each client.
            for client in clients:
                # Checking if the client ID matches the provided ID.
                if client.get('Client ID') == client_id:
                    # Removing the client from the list.
                    clients.remove(client)
                    # Writing the updated list back to the file.
                    FileHandler.write_to_binary_file(clients, 'clients.pkl')
                    # Returning True indicating successful deletion.
                    return True
            # Returning False if the client ID was not found.
            return False
        # Returning False if there are no clients in the file.
        else:
            return False

    # Method to update a client's data by their ID.
    def update_client_by_id(self, client_id, updated_data):
        # Reading client data from the file.
        clients = self.read_clients_from_file()
        # If there are clients in the file:
        if clients:
            # Iterating through each client.
            for client in clients:
                # Checking if the client ID matches the provided ID.
                if client.get('Client ID') == client_id:
                    # Updating the client's data with the provided data.
                    client.update(updated_data)
                    # Writing the updated list back to the file.
                    FileHandler.write_to_binary_file(clients, 'clients.pkl')
                    # Returning True indicating successful update.
                    return True
            # Returning False if the client ID was not found.
            return False
        # Returning False if there are no clients in the file.
        else:
            return False
