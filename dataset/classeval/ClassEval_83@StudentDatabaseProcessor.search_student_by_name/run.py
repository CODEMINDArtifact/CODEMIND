import os
import unittest
import sqlite3


class StudentDatabaseProcessor:

    def __init__(self, database_name):
        self.database_name = database_name

    def create_student_table(self):
        conn = sqlite3.connect(self.database_name)
        cursor = conn.cursor()

        create_table_query = """
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY,
            name TEXT,
            age INTEGER,
            gender TEXT,
            grade INTEGER
        )
        """
        cursor.execute(create_table_query)

        conn.commit()
        conn.close()

    def insert_student(self, student_data):
        conn = sqlite3.connect(self.database_name)
        cursor = conn.cursor()

        insert_query = """
        INSERT INTO students (name, age, gender, grade)
        VALUES (?, ?, ?, ?)
        """
        cursor.execute(insert_query,
                       (student_data['name'], student_data['age'], student_data['gender'], student_data['grade']))

        conn.commit()
        conn.close()

    def search_student_by_name(self, name):
        conn = sqlite3.connect(self.database_name)
        cursor = conn.cursor()

        select_query = "SELECT * FROM students WHERE name = ?"
        cursor.execute(select_query, (name,))
        result = cursor.fetchall()

        conn.close()

        return result

    def delete_student_by_name(self, name):
        conn = sqlite3.connect(self.database_name)
        cursor = conn.cursor()

        delete_query = "DELETE FROM students WHERE name = ?"
        cursor.execute(delete_query, (name,))

        conn.commit()
        conn.close()
class Test(unittest.TestCase):
    def test(self):
            self.processor = StudentDatabaseProcessor("test_database.db")
            self.processor.create_student_table()
            student_data = {
                'name': 'ddd',
                'age': 18,
                'gender': 'male',
                'grade': 95
            }
            self.processor.insert_student(student_data)
            self.processor.delete_student_by_name('ddd')
            conn = sqlite3.connect("test_database.db")
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM students WHERE name=?", ('ddd',))
            result = cursor.fetchall()
            conn.close()
            return len(result)
t=Test()
a=t.test()
with open('/home/changshu/CODEMIND/dataset/classeval/ClassEval_83@StudentDatabaseProcessor.search_student_by_name/output.txt', 'w') as wr:
    wr.write(str(a))
        