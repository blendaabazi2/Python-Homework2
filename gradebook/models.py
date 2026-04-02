class Student:
    def __init__(self, id, name):
        if not isinstance(name,str) or not name.strip():
            raise ValueError("Name must not be empty")
        self.id=id
        self.name=name


class Course:
     def __init__(self,code,title):
        if not isinstance(code, str) or not code.strip():
            raise ValueError("Course code must not be empty")
        if not isinstance(title, str) or not title.strip():
            raise ValueError("Course title must not be empty")
        self.code=code
        self.title=title

class Entrollment():
    def __init__(self, student_id, course_code, grades=None):
        self.student_id=student_id
        self.course_code=course_code
        
        if grades is None:
            self.grades = []
        else:
            for g in grades:
                if not isinstance(g, (int, float)) or g<0 or g>100:
                    raise ValueError("Grades must be between 0 and 100")
                self.grades = grades
        
