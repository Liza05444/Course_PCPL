import unittest
import main


class TestTeacherCourse(unittest.TestCase):
    # Учебные курсы
    courses = [
        main.Course(1, 'математический анализ'),
        main.Course(2, 'физика'),
        main.Course(3, 'модели данных')
    ]
    # Преподаватели
    teachers = [
        main.Teacher(1, 'Акимов', 75_000, 1),
        main.Teacher(2, 'Бурова', 85_000, 2),
        main.Teacher(3, 'Александрова', 80_000, 2),
        main.Teacher(4, 'Корчагин', 70_000, 2),
        main.Teacher(5, 'Бычков', 90_000, 3),
    ]
    teachers_courses = [
        main.TeacherCourse(1, 1),
        main.TeacherCourse(2, 2),
        main.TeacherCourse(2, 3),
        main.TeacherCourse(2, 4),
        main.TeacherCourse(3, 5)
    ]
    one_to_many = main.make_one_to_many(courses, teachers)
    many_to_many = main.make_many_to_many(courses, teachers, teachers_courses)

    def test_do_task_one(self):
        result_1 = main.do_task_one(self.one_to_many)
        result_2 = [('Акимов', 'математический анализ'), ('Александрова', 'физика')]
        self.assertEqual(result_1, result_2)

    def test_do_task_two(self):
        result_1 = main.do_task_two(self.one_to_many, self.courses)
        result_2 = [('физика', 70000), ('математический анализ', 75000), ('модели данных', 90000)]
        self.assertEqual(result_1, result_2)

    def test_do_task_three(self):
        result_1 = main.do_task_three(self.many_to_many)
        result_2 = [('Акимов', 'математический анализ'), ('Александрова', 'физика'), ('Бурова', 'физика'),
                    ('Бычков', 'модели данных'), ('Корчагин', 'физика')]
        self.assertEqual(result_1, result_2)


if __name__ == '__main__':
    unittest.main()