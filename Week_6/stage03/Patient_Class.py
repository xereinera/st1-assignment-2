#basic script for a Patient class
class Patient:
    #the --init--() runs the program whenever a new record is created
    def __init__(self, patient_id, name, phone, email):
        self.patient_id = patient_id
        self.name = name
        self.phone = phone
        self.email = email

    def edit_record(self):
        pass
    #pass = do this later
    def view_history(self):
        pass
