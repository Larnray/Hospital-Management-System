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

    def search_patient_by_id(self, id):
        for patient in self.patients:
            if patient.id == id:
                return patient
        return None

    def edit_patient_info(self, id, new_name, new_disease, new_gender, new_age):
        patient = self.search_patient_by_id(id)
        if patient:
            patient.name = new_name
            patient.disease = new_disease
            patient.gender = new_gender
            patient.age = new_age

class Management:
    def __init__(self):
        self.doctor_manager = DoctorManager()
        self.patient_manager = PatientManager()

    def main_menu(self):
        while True:
            print("Welcome to Alberta Hospital (AH) Managment system")
            print("Select from the following options, or select 3 to stop:")
            print("1 - \tDoctors")
            print("2 - \tPatients")
            print("3 -\tExit Program")
            choice = input(">>> ")
            if choice == "1":
                self.doctors_menu()
            elif choice == "2":
                self.patients_menu()
            elif choice == "3":
                print("Thanks for using the program. Bye!")
                break
                    
    def doctors_menu(self):
        while True:
            print("\nDoctors Menu:")
            print("1 - Display Doctors list")
            print("2 - Search for doctor by ID")
            print("3 - Search for doctor by name")
            print("4 - Add doctor")
            print("5 - Edit doctor info")
            print("6 - Back to the Main Menu")
            choice = input(">>> ")
            if choice == "1":
                self.doctor_manager.display_doctors_list()
            elif choice == "2":
                id = int(input("\nEnter the doctor Id: "))
                doctor = self.doctor_manager.search_doctor_by_id(id)
                if doctor:
                    print("\nId   Name                   Speciality      Timing          Qualification   Room Number\n")
                    print(doctor)
                else:
                    print("\nCan't find the doctor with the same ID on the system")
            elif choice == "3":
                name = input("\nEnter the doctor name: ")
                doctor = self.doctor_manager.search_doctor_by_name(name)
                if doctor:
                    print("\nId   Name                   Speciality      Timing          Qualification   Room Number\n")
                    print(doctor)
                else:
                    print("\nCan't find the doctor with the same name on the system")
            elif choice == "4":
                id = int(input("\nEnter the doctor’s ID: "))
                name = input("Enter the doctor’s name: ")
                speciality = input("Enter the doctor’s specility: ")
                timing = input("Enter the doctor’s timing (e.g., 7am-10pm): ")
                qualification = input("Enter the doctor’s qualification: ")
                room_number = int(input("Enter the doctor’s room number: "))
                new_doctor = Doctor(id, name, speciality, timing, qualification, room_number)
                self.doctor_manager.add_doctor(new_doctor)
                print(f"\nDoctor whose ID is {id} has been added")
            elif choice == "5":
                id = int(input("\nPlease enter the id of the doctor that you want to edit their information: "))
                new_name = input("Enter new Name: ")
                new_speciality = input("Enter new Specilist in: ")
                new_timing = input("Enter new Timing: ")
                new_qualification = input("Enter new Qualification: ")
                new_room_number = int(input("Enter new Room number: "))
                self.doctor_manager.edit_doctor_info(id, new_name, new_speciality, new_timing, new_qualification, new_room_number)
                print(f"\nDoctor whose ID is {id} has been edited")
            elif choice == "6":
                break
    
