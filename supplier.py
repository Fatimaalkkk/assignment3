# Importing the FileHandler module to handle binary file operations.
from binary_file_handler import FileHandler

# Defining a class called Supplier to manage supplier data.
class Supplier:
    # Constructor method to initialize supplier attributes.
    def __init__(self, supplier_id, name, address, contact_details, menu, min_guests, max_guests):
        # List to store supplier data.
        self.suppliers = []
        # Assigning attributes with provided values.
        self.supplier_id = supplier_id
        self.name = name
        self.address = address
        self.contact_details = contact_details
        self.menu = menu
        self.min_guests = min_guests
        self.max_guests = max_guests

    # Method to add a new supplier to the list and save to file.
    def add_supplier(self, supplier_data):
        # Appending supplier data to the list.
        self.suppliers.append(supplier_data)
        # Writing the updated list to a binary file.
        FileHandler.write_to_binary_file(self.suppliers, 'suppliers.pkl')

    # Method to read supplier data from file.
    def read_suppliers_from_file(self):
        # Returning supplier data read from the binary file.
        return FileHandler.read_from_binary_file('suppliers.pkl')

    # Method to delete a supplier by their ID.
    def delete_supplier_by_id(self, supplier_id):
        # Reading supplier data from the file.
        suppliers = self.read_suppliers_from_file()
        # If there are suppliers in the file:
        if suppliers:
            # Iterating through each supplier.
            for supplier in suppliers:
                # Checking if the supplier ID matches the provided ID.
                if supplier.get('Supplier ID') == supplier_id:
                    # Removing the supplier from the list.
                    suppliers.remove(supplier)
                    # Writing the updated list back to the file.
                    FileHandler.write_to_binary_file(suppliers, 'suppliers.pkl')
                    # Returning True indicating successful deletion.
                    return True
            # Returning False if the supplier ID was not found.
            return False
        # Returning False if there are no suppliers in the file.
        else:
            return False

    # Method to update a supplier's data by their ID.
    def update_supplier_by_id(self, supplier_id, updated_data):
        # Reading supplier data from the file.
        suppliers = self.read_suppliers_from_file()
        # If there are suppliers in the file:
        if suppliers:
            # Iterating through each supplier.
            for supplier in suppliers:
                # Checking if the supplier ID matches the provided ID.
                if supplier.get('Supplier ID') == supplier_id:
                    # Updating the supplier's data with the provided data.
                    supplier.update(updated_data)
                    # Writing the updated list back to the file.
                    FileHandler.write_to_binary_file(suppliers, 'suppliers.pkl')
                    # Returning True indicating successful update.
                    return True
            # Returning False if the supplier ID was not found.
            return False
        # Returning False if there are no suppliers in the file.
        else:
            return False
