from enum import Enum


class AppointmentStatus(Enum):
    SCHEDULED = "Scheduled"
    CANCELLED = "Cancelled"


class InvalidAppointmentStateError(Exception):
    pass


class Appointment:
    def __init__(self, appointment_id, patient, practitioner):
        self.__appointment_id = appointment_id
        self.__patient = patient
        self.__practitioner = practitioner
        self.__status = AppointmentStatus.SCHEDULED

    @property
    def status(self):
        return self.__status

    def cancel(self):
        if self.__status == AppointmentStatus.CANCELLED:
            raise InvalidAppointmentStateError(
                "Appointment is already cancelled"
            )

        self.__status = AppointmentStatus.CANCELLED

