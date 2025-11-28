import uuid

class Patient:
    def __init__(self, name, age, disease, status="Admitted"):
        self.name = name
        self.age = age
        self.disease = disease
        self.status = status
        self.patient_id = str(uuid.uuid4())[:8]  # unique ID

    def admit(self):
        self.status = "Admitted"

    def discharge(self):
        self.status = "Discharged"

    def is_admitted(self):
        return self.status == "Admitted"

    def to_dict(self):
        return {
            "patient_id": self.patient_id,
            "name": self.name,
            "age": self.age,
            "disease": self.disease,
            "status": self.status
        }

    def __str__(self):
        return f"Patient({self.name}, {self.age}, {self.disease}, {self.status})"

    def __repr__(self):
        return self.__str__()
