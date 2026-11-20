class Supplier:
    def __init__(self, supplier_id, name, email):
        self.supplier_id = supplier_id
        self.name = name
        self.contact_email = email

    def display_information(self):
        print("====================")
        print("SUPPLIER INFORMATION")
        print("====================")
        print(f"ID: {self.supplier_id}")
        print(f"Name: {self.name}")
        print(f"Contact Email: {self.contact_email}\n")
