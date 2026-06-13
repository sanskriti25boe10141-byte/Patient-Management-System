from patient import Patient
from database import load_data, save_data

patients = load_data()

def add_patient():

    pid = input("Enter Patient ID: ")
    name = input("Enter Name: ")
    age = input("Enter Age: ")
    gender = input("Enter Gender: ")
    blood_group = input("Enter Blood Group: ")
    phone = input("Enter Phone Number: ")
    disease = input("Enter Disease: ")

    patient = Patient(
        pid,
        name,
        age,
        gender,
        blood_group,
        phone,
        disease
    )

    patients.append(patient.to_dict())
    save_data(patients)

    print("\nPatient Added Successfully!")

while True:

    print("\n===== Patient Management System =====")
    print("1. Add Patient")
    print("2. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_patient()

    elif choice == "2":
        print("Exiting...")
        break

    else:
        print("Invalid Choice")
