import sys
from pathlib import Path

# Ensure project root is on sys.path so local imports work when running this file
# directly as a script (e.g. `python cli/main.py`).
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from patient import Patient
from doctor import Doctor
from hospital import HospitalManagement

def menu():
    hm = HospitalManagement()

    while True:
        print("\n--- Hospital Management Menu ---")
        print("1. Add Patient")
        print("2. Add Doctor")
        print("3. Assign Doctor to Patient")
        print("4. Search Patient")
        print("5. Search Doctor")
        print("6. View All Patients")
        print("7. View All Doctors")
        print("8. Discharge Patient")
        print("9. Exit")

        choice = input("Enter choice: ")

        try:
            if choice == "1":
                name = input("Enter patient name: ")
                age = int(input("Enter patient age: "))
                disease = input("Enter disease: ")
                hm.add_patient(Patient(name, age, disease))

            elif choice == "2":
                name = input("Enter doctor name: ")
                specialization = input("Enter specialization: ")
                hm.add_doctor(Doctor(name, specialization))

            elif choice == "3":
                pid = input("Enter patient ID: ")
                did = input("Enter doctor ID: ")
                hm.assign_doctor(pid, did)

            elif choice == "4":
                pid = input("Enter patient ID: ")
                patient = hm.search_patient_by_id(pid)
                print(patient if patient else "Not found")

            elif choice == "5":
                did = input("Enter doctor ID: ")
                doctor = hm.search_doctor_by_id(did)
                print(doctor if doctor else "Not found")

            elif choice == "6":
                print(hm.display_all_patients())

            elif choice == "7":
                print(hm.display_all_doctors())

            elif choice == "8":
                pid = input("Enter patient ID: ")
                patient = hm.search_patient_by_id(pid)
                if patient:
                    patient.discharge()
                    hm.save_data()
                    print("Patient discharged")
                else:
                    print("Patient not found")

            elif choice == "9":
                print("Exiting...")
                break

            else:
                print("Invalid choice, try again.")

        except ValueError:
            print("Invalid input type. Please enter correct values.")
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    menu()
