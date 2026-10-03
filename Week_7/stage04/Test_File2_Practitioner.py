class Practitioner:
    def __init__(self, practitioner_id: int, name: str, specialty: str):
        if practitioner_id <= 0:
            raise ValueError("Practitioner ID must be positive")

        if not name.strip():
            raise ValueError("Name cannot be empty")

        if not specialty.strip():
            raise ValueError("Specialty cannot be empty")

        self.__practitioner_id = practitioner_id
        self.__name = name
        self.__specialty = specialty

    def get_practitioner_id(self):
        return self.__practitioner_id

    def get_name(self):
        return self.__name

    def get_specialty(self):
        return self.__specialty

from Practitioner_Implementation import Practitioner

practitioner = Practitioner(
    1,
    "Sarah Jones",
    "Cardiology"
)

print("Valid practitioner created")

try:
    practitioner = Practitioner(
        -1,
        "Sarah Jones",
        "Cardiology"
    )
except ValueError:
    print("Invalid practitioner ID detected")