from .new_student import Student
import unittest


class TestStudent(unittest.TestCase):

    def test_main(self):
        # obj.__str__() handled by dataclass
        student = Student(name="Edward", surname="agle")
        print(student)

        student = Student("Pnamnil", '42Bangkok')
        print(student)

        student = Student("Pnamnil", '42Bangkok', False)
        print(student)

        # test error when insert an id cause dataclass mark init false
        with self.assertRaises(TypeError) as e:
            student = Student(name="Edward", surname="agle", id='slkj')
        print(e.exception)
