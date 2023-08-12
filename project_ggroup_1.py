# Authors: Olanrewaju Boyede, Chibueze Mgbemere, Adnan Khan
# Date: 11-Aug-2023

class Doctor:
    def __init__(self, id, name, speciality, timing, qualification, room_number):
        self.id = id
        self.name = name
        self.speciality = speciality
        self.timing = timing
        self.qualification = qualification
        self.room_number = room_number

    def __str__(self):
        return (f"{self.id:<5}{self.name:<23}{self.speciality:<15}{self.timing:<15}{self.qualification:<15}{self.room_number:<5}")

class DoctorManager:
    def __init__(self):
        self.doctors = []

    def add_doctor(self, doctor):
        self.doctors.append(doctor)

    def display_doctors_list(self):
        print("Id   Name                   Speciality      Timing          Qualification   Room Number\n")
        for doctor in self.doctors:
            print(doctor)

    def search_doctor_by_id(self, id):
        for doctor in self.doctors:
            if doctor.id == id:
                return doctor
        return None

    def search_doctor_by_name(self, name):
        for doctor in self.doctors:
            if doctor.name == name:
                return doctor
        return None

    def edit_doctor_info(self, id, new_name, new_speciality, new_timing, new_qualification, new_room_number):
        doctor = self.search_doctor_by_id(id)
        if doctor:
            doctor.name = new_name
            doctor.speciality = new_speciality
            doctor.timing = new_timing
            doctor.qualification = new_qualification
            doctor.room_number = new_room_number

class Patient:
    def __init__(self, id, name, disease, gender, age):
        self.id = id
        self.name = name
        self.disease = disease
        self.gender = gender
        self.age = age

    def __str__(self):
        return (f"{self.id:<5}{self.name:<23}{self.disease:<15}{self.gender:<15}{self.age:<5}")

class PatientManager:
    def __init__(self):
        self.patients = []

    def add_patient(self, patient):
        self.patients.append(patient)

    def display_patients_list(self):
        print("ID   Name                   Disease         Gender          Age\n")
        for patient in self.patients:
            print(patient)
