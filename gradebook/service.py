# from gradebook.storage import  load_data, save_data
from .storage import load_data, save_data # relative import

def add_student(name):
    """Adds a new student and returns the generated ID."""

    data = load_data()
    if not name.strip():
        raise ValueError("Student name cannot be empty.")

    if data["students"]:
        new_id = max(student["id"] for student in data["students"]) +1
    else:
        new_id = 1
    student = {
        "id": new_id,
        "name": name
    }

    data["students"].append(student)
    save_data(data)

    return new_id

def add_course(code, title):
    """Adds a new course."""

    data = load_data()

    if not code.strip() or not title.strip():
        raise ValueError("Course code and title cannot be empty")
    
    for course in data["courses"]:
        if course["code"] == code:
            raise ValueError("Course code already exists")
        
    new_course = {
        "code": code,
        "title": title
    }
    data["courses"].append(new_course)
    save_data(data)


def enroll(student_id, course_code):
    """Enrolls a student in a course."""

    data = load_data()
    student_exists = any(student["id"]==student_id for student in data["students"])
    if not student_exists:
        raise ValueError("Student not found")
    course_exists = any(course["code"]==course_code for course in data["courses"])
    if not course_exists:   
        raise ValueError("Course not found")
    
    already_enrolled = any(
        enrollment["student_id"] == student_id and enrollment["course_code"] == course_code
        for enrollment in data["enrollments"]
    )
    if already_enrolled:
        raise ValueError("Student is already enrolled in this course.")
    
    new_enrollment = {
        "student_id": student_id,
        "course_code": course_code,
        "grades": []
    }

    data["enrollments"].append(new_enrollment)
    save_data(data)


def add_grade(student_id, course_code, grade):
    """Adds a grade to a student's enrollment."""

    data = load_data()

    if not isinstance(grade, (int, float)) or grade<0 or grade>100:
        raise ValueError("Grade must be between 0 and 100")
    
    for enrollment in data["enrollments"]:
        if enrollment["student_id"] == student_id and enrollment["course_code"] == course_code:
            enrollment["grades"].append(grade)
            save_data(data)
            return
        
    raise ValueError("Enrollment not found.")

def list_students():
    """Returns all students sorted by name."""

    data = load_data()
    # return sorted(data["students"], key=lambda student: student["name"])
    students = [{"id": s["id"], "name": s["name"]} for s in data["students"]]
    return sorted(students, key=lambda student: student["name"])

def list_courses():
    """Returns all courses sorted by code."""

    data = load_data()
    # return sorted(data["courses"], key=lambda course: course["code"])
    courses = [{"code": c["code"], "title": c["title"]} for c in data["courses"]]
    return sorted(courses, key=lambda course:course["code"])

def list_enrollments():
    """Returns all enrollments sorted by student ID and course code."""

    data = load_data()
    # return sorted(data["enrollments"], key=lambda enrollment: (enrollment["student_id"], enrollment["course_id"]))
    enrollments = [
        {
            "student_id": e["student_id"],
            "course_code": e["course_code"],
            "grades": e["grades"]
        }
        for e in data["enrollments"]
    ]
    return sorted(enrollments, key=lambda enrollment: (enrollment["student_id"], enrollment["course_code"]))


def compute_average(student_id, course_code):
    """Computes average grade for a course."""

    data = load_data()

    for enrollment in data["enrollments"]:
        if enrollment["student_id"] == student_id and enrollment["course_code"] == course_code:
            grades = enrollment["grades"]

            if not grades:
                raise ValueError("No grades found for this enrollment.")
            
            return sum(grades) / len(grades)
        
    raise ValueError("Enrollment not found")

   
def compute_gpa(student_id):
    """Computes GPA for a student."""
    data = load_data()
    averages = []

    for enrollment in data["enrollments"]:
        if enrollment["student_id"] == student_id:
            if enrollment["grades"]:
                avg = sum(enrollment["grades"]) / len(enrollment["grades"])
                averages.append(avg)

    if not averages:
        raise ValueError("No grades found for this student")

    return sum(averages) / len(averages)      

def parse_grade(value):
    """Parses and validates a grade value."""

    try:
        grade = float(value)
    except:
        raise ValueError("Grade must be a number.")
    
    if grade<0 or grade>100:
        raise ValueError("Grade must be between 0 and 100")
    
    return grade