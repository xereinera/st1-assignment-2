def book_appointment(patient_name, practitioner_name, appointment_time):
    appointment = {
        "patient": patient_name,
        "practitioner": practitioner_name,
        "time": appointment_time
    }
    return appointment


# Get information from the user
patient_name = input("Enter patient name: ")
practitioner_name = input("Enter practitioner name: ")
appointment_time = input("Enter appointment time: ")

# Store the appointment
appointment = book_appointment(
    patient_name,
    practitioner_name,
    appointment_time
)

# Display the appointment
print("\nAppointment Booked:")
print(f"Patient: {appointment['patient']}")
print(f"Practitioner: {appointment['practitioner']}")
print(f"Time: {appointment['time']}")