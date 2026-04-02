# Python Mini-Project - Gradebook CLI

A command-line tool for managing students, courses, enrollments, and grades in a simple way.

---

## Setup

### 1. Clone the project
```bash
git clone https://github.com/blendaabazi2/Python-Homework2.git
cd Python-Homework2
```
### 2. Create a virtual environment
```bash
python -m venv venv
```
### 3. Activate virtual environment
```bash
venv\Scripts\activate
```

## Run the project

### Seed data
```bash
python -m scripts.seed
```

---

## CLI Examples

```bash
python main.py add-student --name "Blenda"
python main.py add-course --code CS101 --title "Intro to CS"
python main.py enroll --student-id 1 --course CS101
python main.py add-grade --student-id 1 --course CS101 --grade 95

python main.py list students
python main.py list courses
python main.py list enrollments
python main.py avg --student-id 1 --course CS101
python main.py gpa --student-id 1
```

---

## Example Output

```bash
Average: 85.00
GPA: 85.00
```

---

## Run Tests

```bash
python -m unittest tests.test_service
```

---

## Design Decisions & Limitations

### Design Decisions
- Data stored in JSON file
- The CLI is implemented using argparse
- Logic separated in service.py

### Limitations
- No database
- No UI
- Running the seed script multiple times can create duplicate entries
