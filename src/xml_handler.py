import xml.etree.ElementTree as ET

from objs import Clinic, Patient, Doctor, Appointment

def save_to_xml(clinic, filename):
    root = ET.Element("Clinic")

    patients_elem = ET.SubElement(root, "Patients")
    for patient_id, patient in clinic.patients.items():
        patient_elem = ET.SubElement(patients_elem, "Patient", attrib={"id": str(patient_id)})
        ET.SubElement(patient_elem, "Name").text = patient.name
        ET.SubElement(patient_elem, "Age").text = str(patient.age)
        history_elem = ET.SubElement(patient_elem, "MedicalHistory")
        for record in patient.medical_history:
            ET.SubElement(history_elem, "Record").text = record

    doctors_elem = ET.SubElement(root, "Doctors")
    for doctor_id, doctor in clinic.doctors.items():
        doctor_elem = ET.SubElement(doctors_elem, "Doctor", attrib={"id": str(doctor_id)})
        ET.SubElement(doctor_elem, "Name").text = doctor.name
        ET.SubElement(doctor_elem, "Specialization").text = doctor.specialization
        schedule_elem = ET.SubElement(doctor_elem, "Schedule")
        for dt, available in doctor.schedule.items():
            schedule_item = ET.SubElement(schedule_elem, "DateTime").text = dt
            ET.SubElement(schedule_elem, "Available").text = str(available).lower()

    appointments_elem = ET.SubElement(root, "Appointments")
    for app_id, appointment in clinic.appointments.items():
        app_elem = ET.SubElement(appointments_elem, "Appointment", attrib={"id": app_id})
        ET.SubElement(app_elem, "PatientId").text = str(appointment.patient.patient_id)
        ET.SubElement(app_elem, "DoctorId").text = str(appointment.doctor.doctor_id)
        ET.SubElement(app_elem, "DateTime").text = appointment.date_time

    tree = ET.ElementTree(root)
    tree.write(filename, encoding="utf-8", xml_declaration=True)

def load_from_xml(filename):
    tree = ET.parse(filename)
    root = tree.getroot()

    clinic = Clinic()

    for patient_elem in root.find("Patients"):
        patient_id = patient_elem.attrib["id"]
        name = patient_elem.find("Name").text
        age = int(patient_elem.find("Age").text)
        medical_history = [record.text for record in patient_elem.find("MedicalHistory")]
        clinic.add_patient(Patient(patient_id, name, age, medical_history))

    for doctor_elem in root.find("Doctors"):
        doctor_id = doctor_elem.attrib["id"]
        name = doctor_elem.find("Name").text
        specialization = doctor_elem.find("Specialization").text
        schedule = {dt.text: (avail.text == "true") for dt, avail in zip(doctor_elem.findall("Schedule/DateTime"), doctor_elem.findall("Schedule/Available"))}
        clinic.add_doctor(Doctor(doctor_id, name, specialization, schedule))

    for app_elem in root.find("Appointments"):
        app_id = app_elem.attrib["id"]
        patient_id = app_elem.find("PatientId").text
        doctor_id = app_elem.find("DoctorId").text
        date_time = app_elem.find("DateTime").text
        patient = clinic.get_patient(patient_id)
        doctor = clinic.get_doctor(doctor_id)
        clinic.book_appointment(Appointment(app_id, patient, doctor, date_time))

    return clinic