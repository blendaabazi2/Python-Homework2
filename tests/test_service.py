import unittest 
from unittest.mock import patch
from gradebook.service import add_student , add_grade , compute_average

class TestService(unittest.TestCase):
    @patch("gradebook.service.save_data")
    @patch("gradebook.service.load_data")

    def test_add_student_happy_path(self,mock_load_data,mock_save_data):
        mock_load_data.return_value = {
            "students":[],
            "courses":[],
            "enrollments":[]
        }

        student_id = add_student("Blenda")
        self.assertEqual(student_id,1)
        mock_save_data.assert_called_once()

    @patch("gradebook.service.save_data")
    @patch("gradebook.service.load_data")
    def test_add_grade_happy_path(self,mock_load_data, mock_save_data):
        mock_load_data.return_value = {
            "students" : [{"id" : 1, "name" : "Blenda"}],
            "courses": [{"code" : "CS101", "title" : "Intro to CS"}],
            "enrollments": [
                { "student_id" : 1 , "course_code" : "CS101", "grades" : [] }
            ]
        }

        add_grade(1 , "CS101" , 95)

        self.assertEqual(
            mock_load_data.return_value["enrollments"][0]["grades"],
            [95]
        )
        mock_save_data.assert_called_once()

    
    @patch("gradebook.service.load_data")
    def test_compute_average_happy_path(self,mock_load_data):
        mock_load_data.return_value = {
            "students": [{"id" : 1 , "name" : "Blenda"}],
            "courses" : [{"code" : "CS101" , "title" : "Intro to CS"}],
            "enrollments" : [
                {"student_id" : 1 , "course_code" : "CS101" , "grades" : [80,90,100]}
            ]
        }
        average = compute_average(1 , "CS101")
        self.assertEqual(average , 90)

    @patch("gradebook.service.load_data")
    def test_compute_average_no_grades_edge_case(self,mock_load_data):
        mock_load_data.return_value = {
            "students" : [{"id" : 1 , "name" : "Blenda"}],
            "courses" : [{"code" : "CS101" , "title" : "Intro to CS"}],
            "enrollments" : [{"student_id" : 1 , "course_code" : "CS101" , "grades" : []}]
        }
        with self.assertRaises(ValueError):
            compute_average(1,"CS101")



if __name__ == "__main__":
    unittest.main()
