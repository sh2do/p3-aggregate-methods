
from lib.enrollment import Student, Course, Enrollment
from datetime import datetime, timedelta
from unittest.mock import patch

class TestCodegrade:
    '''Codegrade placeholder'''

    def test_codegrade_placeholder(self):
        assert(True)

    def test_student_course_count(self):
        student = Student("Alice")
        course1 = Course("Math")
        course2 = Course("Science")

        assert student.course_count() == 0

        student.enroll(course1)
        assert student.course_count() == 1

        student.enroll(course2)
        assert student.course_count() == 2

    @patch('lib.enrollment.datetime')
    def test_aggregate_enrollments_per_day(self, mock_datetime):
        # Clear previous enrollments for clean testing
        Enrollment.all = []

        student1 = Student("Alice")
        student2 = Student("Bob")
        course1 = Course("History")
        course2 = Course("Physics")

        # Mock datetime for consistent testing
        mock_datetime.now.return_value = datetime(2023, 1, 10, 10, 0, 0)
        Enrollment(student1, course1)
        Enrollment(student2, course1)
        
        mock_datetime.now.return_value = datetime(2023, 1, 11, 11, 0, 0)
        Enrollment(student1, course2)
        
        mock_datetime.now.return_value = datetime(2023, 1, 10, 12, 0, 0)
        Enrollment(student2, course2)

        expected_counts = {
            datetime(2023, 1, 10).date(): 3,
            datetime(2023, 1, 11).date(): 1
        }
        
        result = Enrollment.aggregate_enrollments_per_day()
        assert result == expected_counts

