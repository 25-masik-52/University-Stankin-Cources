class InvalidDataError(Exception):
    pass

class PatientNotFoundError(Exception):
    pass

class DoctorNotFoundError(Exception):
    pass

class AppointmentConflictError(Exception):
    pass

class Patient:
    def __init__(self, patient_id, name, age, medical_history=None):
        self.patient_id = patient_id
        self.name = name
        self.age = age
        self.medical_history = medical_history if medical_history else []

    def add_to_medical_history(self, record):
        self.medical_history.append(record)

    def __str__(self):
        return f"Patient({self.patient_id}, {self.name}, {self.age})"

class Doctor:
    def __init__(self, doctor_id, name, specialization, schedule=None):
        self.doctor_id = doctor_id
        self.name = name
        self.specialization = specialization
        self.schedule = schedule if schedule else {}

    def add_schedule(self, date_time, available=True):
        if date_time in self.schedule:
            raise InvalidDataError(f"Schedule for {date_time} already exists.")
        self.schedule[date_time] = available

    def is_available(self, date_time):
        return self.schedule.get(date_time, False)

    def __str__(self):
        return f"Doctor({self.doctor_id}, {self.name}, {self.specialization})"

class Appointment:
    def __init__(self, appointment_id, patient, doctor, date_time):
        self.appointment_id = appointment_id
        self.patient = patient
        self.doctor = doctor
        self.date_time = date_time

    def __str__(self):
        return f"Appointment({self.appointment_id}, {self.patient.name}, {self.doctor.name}, {self.date_time})"

class Clinic:
    def __init__(self):
        self.patients = {}
        self.doctors = {}
        self.appointments = {}

    def add_patient(self, patient):
        if patient.patient_id in self.patients:
            raise InvalidDataError(f"Patient with ID {patient.patient_id} already exists.")
        self.patients[patient.patient_id] = patient

    def add_doctor(self, doctor):
        if doctor.doctor_id in self.doctors:
            raise InvalidDataError(f"Doctor with ID {doctor.doctor_id} already exists.")
        self.doctors[doctor.doctor_id] = doctor

    def book_appointment(self, appointment):
        doctor = self.doctors.get(appointment.doctor.doctor_id)
        if not doctor:
            raise DoctorNotFoundError(f"Doctor with ID {appointment.doctor.doctor_id} not found.")

        if not doctor.is_available(appointment.date_time):
            raise AppointmentConflictError(f"Doctor is not available at {appointment.date_time}.")

        doctor.schedule[appointment.date_time] = False
        self.appointments[appointment.appointment_id] = appointment

    def get_patient(self, patient_id):
        if patient_id not in self.patients:
            raise PatientNotFoundError(f"Patient with ID {patient_id} not found.")
        return self.patients[patient_id]

    def get_doctor(self, doctor_id):
        if doctor_id not in self.doctors:
            raise DoctorNotFoundError(f"Doctor with ID {doctor_id} not found.")
        return self.doctors[doctor_id]