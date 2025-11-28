import uuid

class Doctor:
    def __init__(self, name, specialization):
        self.name = name
        self.specialization = specialization
        self.doctor_id = str(uuid.uuid4())[:8]

    def to_dict(self):
        return {
            "doctor_id": self.doctor_id,
            "name": self.name,
            "specialization": self.specialization
        }

    def __str__(self):
        return f"Doctor({self.name}, {self.specialization})"

    def __repr__(self):
        return self.__str__()
