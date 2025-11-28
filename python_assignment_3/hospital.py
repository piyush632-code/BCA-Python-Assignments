import json
import logging
from pathlib import Path
from patient import Patient
from doctor import Doctor

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

class HospitalManagement:
    def __init__(self, data_file="data/records.json"):
        self.patients = []
        self.doctors = []
        self.data_file = Path(data_file)
        self.load_data()

    def add_patient(self, patient):
        self.patients.append(patient)
        logging.info(f"Patient added: {patient.name}")
        self.save_data()

    def add_doctor(self, doctor):
        self.doctors.append(doctor)
        logging.info(f"Doctor added: {doctor.name}")
        self.save_data()

    def assign_doctor(self, patient_id, doctor_id):
        patient = self.search_patient_by_id(patient_id)
        doctor = self.search_doctor_by_id(doctor_id)
        if patient and doctor:
            patient.doctor_id = doctor_id
            logging.info(f"Doctor {doctor.name} assigned to Patient {patient.name}")
            self.save_data()
        else:
            logging.warning("Invalid patient or doctor ID")

    def search_patient_by_id(self, patient_id):
        return next((p for p in self.patients if p.patient_id == patient_id), None)

    def search_doctor_by_id(self, doctor_id):
        return next((d for d in self.doctors if d.doctor_id == doctor_id), None)

    def display_all_patients(self):
        return [p.to_dict() for p in self.patients]

    def display_all_doctors(self):
        return [d.to_dict() for d in self.doctors]

    def save_data(self):
        try:
            data = {
                "patients": [p.to_dict() for p in self.patients],
                "doctors": [d.to_dict() for d in self.doctors]
            }
            self.data_file.parent.mkdir(parents=True, exist_ok=True)
            with open(self.data_file, "w") as f:
                json.dump(data, f, indent=4)
        except PermissionError:
            logging.error("Permission denied while saving data")
        except Exception as e:
            logging.error(f"Error saving data: {e}")

    def load_data(self):
        if self.data_file.exists():
            try:
                with open(self.data_file, "r") as f:
                    data = json.load(f)
                    self.patients = [Patient(**p) for p in data.get("patients", [])]
                    self.doctors = [Doctor(**d) for d in data.get("doctors", [])]
            except json.JSONDecodeError:
                logging.error("Corrupted data file")
            except Exception as e:
                logging.error(f"Error loading data: {e}")
