# Authors: Olanrewaju Boyede, Chibueze Mgbemere, Adnan Khan
# Date: 11-Aug-2023

    def patients_menu(self):
        while True:
            print("\nPatients Menu:")
            print("1 - Display patients list")
            print("2 - Search for patient by ID")
            print("3 - Add patient")
            print("4 - Edit patient info")
            print("5 - Back to the Main Menu")
            choice = input(">>> ")
            if choice == "1":
                self.patient_manager.display_patients_list()
            elif choice == "2":
                id = int(input("\nEnter the patient Id: "))
                patient = self.patient_manager.search_patient_by_id(id)
                if patient:
                    print("\nID   Name                   Disease         Gender          Age\n")
                    print(patient)
                else:
                    print("\nCan't find the patient with the same ID on the system")
            elif choice == "3":
                id = int(input("\nEnter the patient’s ID: "))
                name = input("Enter the patient’s name: ")
                disease = input("Enter the patient’s disease: ")
                gender = input("Enter the patient’s gender: ")
                age = int(input("Enter the patient’s age: "))
                new_patient = Patient(id, name, disease, gender, age)
                self.patient_manager.add_patient(new_patient)
                print(f"\nPatient whose ID is {id} has been added")
            elif choice == "4":
                id = int(input("\nPlease enter the id of the patient that you want to edit their information: "))
                new_name = input("Enter new Name: ")
                new_disease = input("Enter new Disease: ")
                new_gender = input("Enter new Gender: ")
                new_age = int(input("Enter new Age: "))
                self.patient_manager.edit_patient_info(id, new_name, new_disease, new_gender, new_age)
                print(f"\nPatient whose ID is {id} has been edited")
            elif choice == "5":
                break

management = Management()

doctors = [
    Doctor(21, "Dr.Gody", "ENT", "5am-11aM", "MBBS,MD", 17),
    Doctor(32, "Dr.Vikram", "Physician", "10pm-3am", "MBBS,MD", 45),
    Doctor(17, "Dr.Amy", "Surgeon", "8pm-2am", "BDM", 8),
    Doctor(33, "Dr.David", "Artho", "10am-4pm", "MBBS,MS", 40),
    Doctor(123, "Dr. Ross", "Headackes", "8pm-10am", "MST", 102),
    Doctor(66, "Dr. Mike", "Heart", "9am-5pm", "MS", 2)
]

for doctor in doctors:
    management.doctor_manager.add_doctor(doctor)

patients = [
    Patient(12, "Pankaj", "Cancer", "Male", 30),
    Patient(13, "Janina", "Cold", "Female", 23),
    Patient(14, "Alonna", "Malaria", "Female", 45),
    Patient(15, "Ravi", "Diabetes", "Male", 65)
]

for patient in patients:
    management.patient_manager.add_patient(patient)

management.main_menu()