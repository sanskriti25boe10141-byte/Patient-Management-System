#  Patient Management System

##  Project Overview

The Patient Management System is a Python-based application developed to simplify the management of patient records in healthcare environments. This project provides an organized way to store, retrieve, update, and delete patient information while demonstrating fundamental software development concepts.

The system is designed as a beginner-friendly project that helps students learn Python programming, Object-Oriented Programming (OOP), file handling, and CRUD operations.

---

##  Project Objectives

- Maintain patient records in a structured manner.
- Reduce manual record-keeping efforts.
- Provide quick access to patient information.
- Practice software development using Python.
- Learn data storage and retrieval techniques.

---

##  Features

###  Add Patient
- Register a new patient into the system.
- Store patient details securely.
- Assign a unique Patient ID.

###  View Patients
- Display all patient records.
- Show important patient information in an organized format.

###  Search Patient
- Search for a patient using their Patient ID.
- Retrieve complete patient details instantly.

### Update Patient Information
- Modify existing patient records.
- Keep patient information accurate and up to date.

###  Delete Patient
- Remove patient records when no longer required.
- Prevent unnecessary data accumulation.

###  Data Persistence
- Store patient records in a JSON file.
- Ensure data remains available after the program is closed.

---

## Patient Information Stored

Each patient record contains:

- Patient ID
- Full Name
- Age
- Gender
- Blood Group
- Phone Number
- Disease / Diagnosis

Example:

```json
{
  "pid": "P101",
  "name": "John Doe",
  "age": 25,
  "gender": "Male",
  "blood_group": "O+",
  "phone": "9876543210",
  "disease": "Fever"
}
```

---

## Technologies Used

### Python
- Core programming language used for development.

### Object-Oriented Programming (OOP)
- Used to represent patient data through classes and objects.

### JSON
- Used for storing patient records permanently.

### Git & GitHub
- Used for version control and project management.

---

##  Project Structure

```text
Patient-Management-System/
│
├── main.py
├── patient.py
├── database.py
├── patients.json
├── README.md
├── LICENSE
└── .gitignore
```

### File Descriptions

#### main.py
- Main application file.
- Contains menu-driven interface.
- Handles user interaction.

#### patient.py
- Contains the Patient class.
- Defines patient attributes and methods.

#### database.py
- Handles data loading and saving.
- Manages JSON file operations.

#### patients.json
- Stores all patient records.
- Acts as the project's database.

#### README.md
- Contains project documentation.

---

##  How to Run the Project

### Step 1: Clone Repository

```bash
git clone https://github.com/your-username/Patient-Management-System.git
```

### Step 2: Open Project Folder

```bash
cd Patient-Management-System
```

### Step 3: Run Program

```bash
python main.py
```

---

##  System Workflow

1. User launches the application.
2. Main menu is displayed.
3. User selects an operation:
   - Add Patient
   - View Patients
   - Search Patient
   - Update Patient
   - Delete Patient
4. Data is processed.
5. Records are saved automatically.
6. Updated information becomes available for future use.

---

##  Concepts Learned Through This Project

- Python Programming
- Variables and Data Types
- Functions
- Conditional Statements
- Loops
- Classes and Objects
- File Handling
- JSON Data Storage
- CRUD Operations
- GitHub Project Management

---

##  Future Improvements

### Database Integration
- Replace JSON with SQLite or MySQL.

### Graphical User Interface (GUI)
- Build a GUI using Tkinter.

### User Authentication
- Add login and registration system.

### Appointment Management
- Schedule patient appointments.

### Doctor Management
- Assign doctors to patients.

### Web Application
- Convert project into a Flask-based web application.

### Data Visualization
- Generate reports and patient statistics.

---

##  Real-World Applications

This system can be adapted for:

- Hospitals
- Clinics
- Diagnostic Centers
- Medical Laboratories
- Healthcare Startups
- Educational Demonstrations

---

##  Author

**Sanskriti Kumari**

- B.Tech Bioengineering Student
- Python Developer (Learning)
- Interested in Healthcare Technology, Bioinformatics, and Software Development

---

##  License

This project is licensed under the MIT License.

---

⭐ If you found this project useful, consider giving it a star on GitHub.
