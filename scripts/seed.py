from gradebook.service import (
    add_student,
    add_course,
    add_grade,
    enroll
)

def seed():
    print("Seeding data...")

    s1 = add_student("Blenda")
    s2 = add_student("Belita")
    s3 = add_student("Diar")

    #courses
    add_course("CS101","Intro to CS")
    add_course("ALGO101", "Algorithm")

    #enrollments
    enroll(s1, "CS101"),
    enroll(s1, "ALGO101"),
    enroll(s2, "CS101"),
    enroll(s3, "ALGO101"),

    #grades
    add_grade(s1, "CS101", 90)
    add_grade(s1, "CS101", 80)
    add_grade(s1, "ALGO101", 85)

    add_grade(s2, "CS101", 70)
    add_grade(s2, "CS101", 75)

    add_grade(s3, "ALGO101", 95)

    print("Data seeded successfully")

if __name__ == "__main__":
    seed() 



    


