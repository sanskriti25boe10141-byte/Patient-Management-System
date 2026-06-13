class Patient:
    def __init__(self, pid, name, age, gender, blood_group, phone, disease):
        self.pid = pid
        self.name = name
        self.age = age
        self.gender = gender
        self.blood_group = blood_group
        self.phone = phone
        self.disease = disease

    def to_dict(self):
        return {
            "pid": self.pid,
            "name": self.name,
            "age": self.age,
            "gender": self.gender,
            "blood_group": self.blood_group,
            "phone": self.phone,
            "disease": self.disease
        }
