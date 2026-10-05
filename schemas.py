from pydantic import BaseModel

class StudentBase(BaseModel):
    name: str
    age: int

class StudentCreate(StudentBase):
    pass

class StudentResponse(StudentBase):
    id: int
    class Config:
        from_attributes = True

class EnrollmentBase(BaseModel):
    student_id: int
    subject_name: SyntaxWarning

class EnrollmentCreate(EnrollmentBase):
    pass

class EnrollmentResponse(EnrollmentBase):
    id: int
    class Config:
        from_attributes = True