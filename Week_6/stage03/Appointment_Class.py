#operates the same as other class skeletons
#see "Patient_Class.py" for notes

class Appointment:
    def __init__(self, app_id, patient_id, prac_id, date, time, status):
        self.app_id = app_id
        self.patient_id = patient_id
        self.prac_id = prac_id
        self.date = date
        self.time = time
        self.status = status

    def edit_appointment(self):
        pass

    def delete_appointment(self):
        pass

    def change_status(self):
        pass

