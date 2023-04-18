from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# 1 Add models for student, subject and student_subject from previous lessons in SQLAlchemy.
Base = declarative_base()

class Student(Base):
    __tablename__ = 'student'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)
    subjects = relationship('Subject', secondary='student_subject')

class Subject(Base):
    __tablename__ = 'subject'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    students = relationship('Student', secondary='student_subject')

class StudentSubject(Base):
    __tablename__ = 'student_subject'

    student_id = Column(Integer, ForeignKey('student.id'), primary_key=True)
    subject_id = Column(Integer, ForeignKey('subject.id'), primary_key=True)

# 2 Find all students` name that visited 'English' classes.

engine = create_engine('sqlite:///example.db')
Session = sessionmaker(bind=engine)
session = Session()

students = session.query(Student).join(StudentSubject).join(Subject).filter(Subject.name == 'English').all()

for student in students:
    print(student.name)
