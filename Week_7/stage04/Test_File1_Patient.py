class Patient:
    def __init__(self, patient_id: int, name: str):
        if patient_id <= 0:
            raise ValueError("Patient ID must be positive")

        if not name.strip():
            raise ValueError("Name cannot be empty")

        self.__patient_id = patient_id
        self.__name = name

    def get_patient_id(self):
        return self.__patient_id

    def get_name(self):
        return self.__name

from Patient_Implementation import Patient

# Valid Patient

patient = Patient(1, "John Smith")
print("Valid patient created")

# Invalid ID

try:
    patient = Patient(-1, "John Smith")
except ValueError:
    print("Invalid ID detected")

# Empty Name

try:
    patient = Patient(1, "")
except ValueError:
    print("Empty name detected")