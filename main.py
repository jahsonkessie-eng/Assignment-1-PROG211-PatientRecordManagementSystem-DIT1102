# PATIENT RECORD MANAGEMENT SYSTEM
# OOP1 Individual Assignment


# CLASS 1: PATIENT
class Patient:

    def __init__(self, patient_id, name, age, gender, condition):
        self.patient_id = patient_id
        self.name = name
        self.age = age
        self.gender = gender
        self.condition = condition

    def display_info(self):
        print("Patient ID:", self.patient_id)
        print("Name:", self.name)
        print("Age:", self.age)
        print("Gender:", self.gender)
        print("Condition:", self.condition)
        print("-----------------------------------")

    def update_condition(self, new_condition):
        self.condition = new_condition
        print("Patient condition updated successfully!")


# CLASS 2: PATIENT MANAGEMENT SYSTEM
class PatientManagementSystem:

    def __init__(self):
        self.patients = []

    # REGISTER PATIENT
    def add_patient(self, patient):

        for existing_patient in self.patients:
            if existing_patient.patient_id == patient.patient_id:
                print("Patient ID already exists!")
                return

        self.patients.append(patient)

        print("\nPatient registered successfully!")
        print("Total patients now:", len(self.patients))

    # DISPLAY ALL PATIENTS
    def display_all_patients(self):

        print("\n========== ALL REGISTERED PATIENTS ==========")

        if len(self.patients) == 0:
            print("No patients have been registered.")
            return

        for patient in self.patients:
            patient.display_info()

        print("TOTAL PATIENTS DISPLAYED:", len(self.patients))

    # SEARCH FOR A PATIENT
    def search_patient(self, patient_id):

        for patient in self.patients:
            if patient.patient_id.lower() == patient_id.lower():
                print("\nPATIENT FOUND")
                patient.display_info()
                return

        print("Patient not found.")

    # UPDATE PATIENT CONDITION
    def update_patient_condition(self, patient_id, new_condition):

        for patient in self.patients:
            if patient.patient_id.lower() == patient_id.lower():
                patient.update_condition(new_condition)
                return

        print("Patient not found.")

    # COUNT ALL PATIENTS
    def count_patients(self):
        total = len(self.patients)

        print("\n========== PATIENT STATISTICS ==========")
        print("TOTAL REGISTERED PATIENTS:", total)
        print("========================================")


# MAIN PROGRAM
def main():

    system = PatientManagementSystem()

    while True:

        print("\n======================================")
        print("   PATIENT RECORD MANAGEMENT SYSTEM")
        print("======================================")
        print("1. Register Patient")
        print("2. Display All Patients")
        print("3. Search Patient")
        print("4. Update Patient Condition")
        print("5. Count All Patients")
        print("6. Exit")
        print("======================================")

        choice = input("Enter your choice: ").strip()

        # OPTION 1
        if choice == "1":

            patient_id = input("Enter Patient ID: ").strip()
            name = input("Enter Patient Name: ").strip()

            try:
                age = int(input("Enter Patient Age: "))

                if age < 0 or age > 130:
                    print("Enter a valid age between 0 and 130.")
                    continue

            except ValueError:
                print("Age must be a number.")
                continue

            gender = input("Enter Gender: ").strip()
            condition = input("Enter Patient Condition: ").strip()

            if not patient_id or not name or not gender or not condition:
                print("All fields are required!")
                continue

            patient = Patient(
                patient_id,
                name,
                age,
                gender,
                condition
            )

            system.add_patient(patient)

        # OPTION 2
        elif choice == "2":

            system.display_all_patients()

        # OPTION 3
        elif choice == "3":

            patient_id = input("Enter Patient ID to search: ").strip()

            system.search_patient(patient_id)

        # OPTION 4
        elif choice == "4":

            patient_id = input("Enter Patient ID: ").strip()
            new_condition = input("Enter New Condition: ").strip()

            if not patient_id or not new_condition:
                print("Both fields are required!")
                continue

            system.update_patient_condition(
                patient_id,
                new_condition
            )

        # OPTION 5
        elif choice == "5":

            system.count_patients()

        # OPTION 6
        elif choice == "6":

            print("Thank you for using the Patient Record Management System!")
            break

        else:
            print("Invalid choice. Please enter a number from 1 to 6.")


if __name__ == "__main__":
    main()