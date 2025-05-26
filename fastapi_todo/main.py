from fastapi.responses import JSONResponse
from sqlmodel import Fields, SQLModel, Session, create_engine,select
from cachetools import TTLCache
import logging

logging.basicConfig(level=logging.INFO)
app = FastAPI()



class Student(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    name: str
    age: int
    grade: str

sqlite_file_name = "students.db"
engine = create_engine("sqlite:///{sqlite_file_name}", echo=False)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

@app.on_event("startup")
def on_startup():
    create_db_and_tables()

cache = TITLcache(maxsize=100, ttl=30)

@app.get("/students")
async def get_students(version: str = Header(default="v1")):
    logging.info("Fetching student list")


    if 'students' in cache:
        logging.info("Serving from cache")
        return cache['students']






































    with Session(engine) as session:
        statement = select(Student)
        results = session.exec(statement).all()
        return results

@app.patch("/students/{student_id}")
def patch_student(student_id: int, student_data: dict = Body(...)):
    with Session(engine) as session:
        student = session.get(Student, student_id)
        if not student:
            raise HTTPException(status_code=404, detail="Student not found")
        for key, value in student_data.items():
            if hasattr(student, key):
                setattr(student, key, value)
        session.add(student)
        session.commit()
        session.refresh(student)
        return student

@app.put("/students/{student_id}")
def update_student(student_id: int, updated_student: Student):
    with Session(engine) as session:
        student = session.get(Student, student_id)
        if not student:
            raise HTTPException(status_code=404, detail="Student not found")
        updated_student.id = student_id
        session.merge(updated_student)
        session.commit()
        return updated_student

@app.delete("/students/{student_id}")
def delete_student(student_id: int):
    with Session(engine) as session:
        student = session.get(Student, student_id)
        if not student:
            raise HTTPException(status_code=404, detail="Student not found")
        session.delete(student)
        session.commit()
        return {"message": "Student deleted successfully"}

@app.head("/students")
def head_students():
    return Response(headers={"X-Data-Type": "Student-List"})

@app.options("/students")
def options_students():
    return Response(headers={"Allow": "GET, POST, PUT, PATCH, DELETE, OPTIONS, HEAD"})
