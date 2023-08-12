# Authors: Olanrewaju Boyede, Chibueze Mgbemere, Adnan Khan
# Date: 11-Aug-2023


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
    
