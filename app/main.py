from fastapi import FastAPI
from .utils import json_to_dict_list
import os
from typing import Optional
from app.students.models import SStudent

script_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(script_dir)
path_to_json = os.path.join(parent_dir, 'students.json')


app = FastAPI()
@app.get("/students")
def get_all_students():
    return json_to_dict_list(path_to_json)

@app.get("/")
def home_page():
    return {"message": "python"}

@app.get("/students/{course}")
def get_all_students_course(course: int):
    students = json_to_dict_list(path_to_json)
    return_list = []
    for student in students:
        if student["course"] == course:
            return_list.append(student)
    return return_list

@app.get("/students")
def get_all_student(course: Optional[int]=None):
    students = json_to_dict_list(path_to_json)
    if course in None:
        return students
    else:
        return_list = []
        for student in students:
            if student["course"] == course:
                return_list.append(student)
        return return_list
    
@app.get("/students/{course}")
def get_all_student_course(course: int, major: Optional[str]=None, enrollment_year: Optional[str]=2018):
    students = json_to_dict_list(path_to_json)
    filtered_students = []
    for student in students:
        if student["course"] == course:
            filtered_students.append(student)

    if major:
        filtered_students = [student for student in filtered_students if student['major'].lower()==major.lower()]

    if enrollment_year:
        filtered_students = [student for student in filtered_students if student['enrollments_year']==enrollment_year]

    return filtered_students

@app.get("/student")
def get_student_from_param_id(student_id: int) -> SStudent:
    students = json_to_dict_list(path_to_json)
    for student in students:
        if student["student_id"] == student_id:
            return student