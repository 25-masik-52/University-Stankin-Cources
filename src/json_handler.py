import json

from objs import Clinic, Patient, Doctor, Appointment

def save_to_json(clinic, filename):
    data = {
        "Clinic": {
            "Patients": [
                {
                    "id": pid,
                    "name": p.name,
                    "age": p.age,
                    "medical_history": p.medical_history
                } for pid, p in clinic.patients.items()
            ],
            "Doctors": [
                {
                    "id": did,
                    "name": d.name,
                    "specialization": d.specialization,
                    "schedule": d.schedule
                } for did, d in clinic.doctors.items()
            ],
            "Appointments": [
                {
                    "id": aid,
                    "patient_id": a.patient.patient_id,
                    "doctor_id": a.doctor.doctor_id,
                    "date_time": a.date_time
                } for aid, a in clinic.appointments.items()
            ]
        }
    }

    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)

def load_from_json(filename):
    with open(filename, 'r') as f:
        data = json.load(f)

    clinic = Clinic()

    for patient_data in data["Clinic"]["Patients"]:
        patient = Patient(patient_data["id"], patient_data["name"], patient_data["age"], patient_data["medical_history"])
        clinic.add_patient(patient)

    for doctor_data in data["Clinic"]["Doctors"]:
        doctor = Doctor(doctor_data["id"], doctor_data["name"], doctor_data["specialization"], doctor_data["schedule"])
        clinic.add_doctor(doctor)

    for appointment_data in data["Clinic"]["Appointments"]:
        patient = clinic.get_patient(appointment_data["patient_id"])
        doctor = clinic.get_doctor(appointment_data["doctor_id"])
        appointment = Appointment(appointment_data["id"], patient, doctor, appointment_data["date_time"])
        clinic.book_appointment(appointment)

    return clinic