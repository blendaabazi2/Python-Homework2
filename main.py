import argparse
import logging
import os
from gradebook.service import (
    add_student,
    add_course,
    enroll,
    add_grade,
    list_students,
    list_courses,
    list_enrollments,
    compute_average,
    compute_gpa,
    parse_grade,
)

os.makedirs("logs", exist_ok=True)

logging.basicConfig(
    filename="logs/app.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


def main():
    parser = argparse.ArgumentParser(description="Gradebook CLI")
    subparsers = parser.add_subparsers(dest="command")

    #add-student
    parser_add_student = subparsers.add_parser("add-student")
    parser_add_student.add_argument("--name", required=True)

    #add-course
    parser_add_course = subparsers.add_parser("add-course")
    parser_add_course.add_argument("--code", required=True)
    parser_add_course.add_argument("--title", required=True)

    #enroll
    parser_enroll = subparsers.add_parser("enroll")
    parser_enroll.add_argument("--student-id", type=int, required=True)
    parser_enroll.add_argument("--course", required=True)

    #add-grade
    parser_add_grade = subparsers.add_parser("add-grade")
    parser_add_grade.add_argument("--student-id", type=int, required=True)
    parser_add_grade.add_argument("--course", required=True)
    parser_add_grade.add_argument("--grade", required=True)

    #list
    parser_list = subparsers.add_parser("list")
    parser_list.add_argument("entity", choices=["students", "courses", "enrollments"])
    parser_list.add_argument("--sort", choices=["name", "code"], required=False)

    #avg
    parser_avg = subparsers.add_parser("avg")
    parser_avg.add_argument("--student-id", type=int, required=True)
    parser_avg.add_argument("--course", required=True)

    #gpa
    parser_gpa = subparsers.add_parser("gpa")
    parser_gpa.add_argument("--student-id", type=int, required=True)

    args = parser.parse_args()

    try:
        if args.command == "add-student":
            student_id = add_student(args.name)
            print(f"Student added with ID {student_id}")
            logging.info(f"Added student with ID {student_id}")

        elif args.command == "add-course":
            add_course(args.code, args.title)
            print("Course added successfully")
            logging.info(f"Course {args.code} added")

        elif args.command == "enroll":
            enroll(args.student_id, args.course)
            print("Enrollment added successfully")
            logging.info(f"Student {args.student_id} enrolled in {args.course}")

        elif args.command == "add-grade":
            grade = parse_grade(args.grade)
            add_grade(args.student_id, args.course, grade)
            print("Grade added succesfully")
            logging.info(f"Grade {grade} added for student {args.student_id}")

        elif args.command=="list":
            if args.entity == "students":
                students = list_students()
                for s in students:
                    print(s)
            elif args.entity == "courses":
                courses = list_courses()
                for c in courses:
                    print(c)
            elif args.entity == "enrollments":
                enrollments = list_enrollments()
                for e in enrollments:
                    print(e)
            
        elif args.command == "avg":
            avg = compute_average(args.student_id, args.course)
            print(f"Average: {avg:.2f}")
        
        elif args.command == "gpa":
            gpa = compute_gpa(args.student_id)
            print(f"GPA: {gpa:.2f}")
        else:
            parser.print_help()

    except ValueError as e:
        print(f"Error: {e}")
        logging.error(f"ValueError: {e}")
    
    except Exception as e:
        print(f"Unexpected error: {e}")
        logging.error(f"Unexpected error: {e}")


if __name__ == "__main__":
    main()


