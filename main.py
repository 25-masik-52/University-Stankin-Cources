from src import objs, xml_handler, json_handler

clinic = objs.Clinic()
# Добавление данных
clinic.add_patient(objs.Patient("1", "John Doe", 30))
clinic.add_doctor(objs.Doctor("101", "Dr. Smith", "Cardiologist"))
# clinic.book_appointment(objs.Appointment("A1", clinic.get_patient("1"), clinic.get_doctor("101"), "2023-04-05T10:00:00"))

# Сохранение в файлы
xml_handler.save_to_xml(clinic, "files/clinic.xml")
json_handler.save_to_json(clinic, "files/clinic.json")

# Загрузка из файлов
loaded_clinic = xml_handler.load_from_xml("files/clinic.xml")
loaded_clinic_json = json_handler.load_from_json("files/clinic.json")
