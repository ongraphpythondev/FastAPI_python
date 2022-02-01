from fastapi import FastAPI , Path
from typing import Optional
from pydantic import BaseModel

""" 
Operations in Data Communitcation : 
GET : Get information
POST : Create something
PUT : Udate existing information/data
DELETE : Deleting data/info
PATCH : Partial Update

TO run fastapi via Command Prompt : 
uvicorn appname:FastAPIvariablename
for this fastapi file command is :
    uvicorn myapi:app
this will run uvicorn server
"""

app = FastAPI()

students = {
    1 : {
        "name" : "John",
        "age" : 17,
        "class" : "Year 12"
    }
}

class Student(BaseModel):
    name : str 
    age : int 
    year : str

class UpdateStudent(BaseModel):
    name : Optional[str] = None 
    age:  Optional[int] = None
    year:  Optional[str] = None 
    

@app.get("/")
def index():
    return {"name":"First Data"}


# gt = greater than and lt = lesser than
@app.get("/get-student/{student_id}")
def get_student(student_id:int = Path(None , description="The Id Of student you want to view.", gt=0)):
    return students[student_id]



# URL =  google.com?search=maxwelltheory
# in above url '?' is for query
@app.get("/get-by-name/{student_id}")
def get_student(*, student_id:int, name: Optional[str] = None, test: int):
    for student_id in students :
        if students[student_id]["name"] == name:
            return students[student_id]
    
    return {"Data" : "Not Found"}

            
@app.post("/create-student/{student_id}")
def create_student(student_id : int , student : Student):
    if student_id in students : 
        return {"Error" : "Student Exists"}
    students[student_id] = student
    return students[student_id]


@app.put("/update-student/{student_id}")
def update_student(student_id: int, student: UpdateStudent):
    if student_id not in students :
        return {"Error" : "Student does not exist."}
    
    if student.name != None:
        students[student_id].name = student.name

    if student.age != None:
        students[student_id].age = student.age

    if student.year != None:
        students[student_id].year = student.year
    return students[student_id]
    

@app.delete("/delete-student/{student_id}")
def delete_student(student_id:int):
    if not students[student_id] :
        return {"Error" : "Student does not exist."}   
    del students[student_id]
    return {"Message" : "Student deleted successfully"}
    

