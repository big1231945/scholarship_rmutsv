from sqlalchemy import Column, Integer, String, Double, ForeignKey, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class Student(Base):
    __tablename__ = 'student'
    id = Column(Integer, primary_key=True)
    title_name = Column(String(20),nullable=False)
    first_name = Column(String(100),nullable=False)
    last_name = Column(String(100),nullable=False)
    birthday = Column(String(200),nullable=False)
    ethnicity = Column(String(100),nullable=False)
    nationality = Column(String(100),nullable=False)
    religion = Column(String(100),nullable=False)
    tel = Column(String(10),nullable=False)
    gpa = Column(Double,nullable=False)
    gpax = Column(Double,nullable=False)
    term = Column(String(100),nullable=False)
    reason = Column(Text,nullable=False)
    id_std_copy = Column(String(255),nullable=False)
    id_card_copy = Column(String(255),nullable=False)
    house_copy = Column(String(255),nullable=False)
    gpa_gpax_copy = Column(String(255),nullable=False)
    photo_house = Column(String(255),nullable=False)
    photo_family = Column(String(255),nullable=False)
    photo_std = Column(String(255),nullable=False)
    address_hose = relationship("AddressHose", back_populates="student")
    address_ez = relationship("AddressEZ", back_populates="student")
    address_part_time = relationship(
        "AddressPartTime", back_populates="student")
    father = relationship("Father", back_populates="student")
    mother = relationship("Mother", back_populates="student")
    living_with = relationship("LivingWith", back_populates="student")
    support = relationship("Support", back_populates="student")
    information_history = relationship(
        "InformationHistory", back_populates="student")
    part_time_job = relationship("PartTimeJob", back_populates="student")
    payment_history = relationship("PaymentHistory", back_populates="student")


class AddressHouse(Base):
    __tablename__ = 'address_house'
    id = Column(Integer, primary_key=True)
    student_id = Column(Integer, ForeignKey('student.id'),nullable=False)
    address = Column(String(500),nullable=False)
    subdistrict = Column(String(100),nullable=False)
    district = Column(String(100),nullable=False)
    province = Column(String(100),nullable=False)
    postal_code = Column(String(20),nullable=False)
    student = relationship("Student", back_populates="address_house")


class AddressEZ(Base):
    __tablename__ = 'address_ez'
    id = Column(Integer, primary_key=True)
    student_id = Column(Integer, ForeignKey('student.id'),nullable=False)
    address = Column(String(500),nullable=False)
    subdistrict = Column(String(100),nullable=False)
    district = Column(String(100),nullable=False)
    province = Column(String(100),nullable=False)
    postal_code = Column(String(20),nullable=False)
    student = relationship("Student", back_populates="address_ez")


class AddressPartTime(Base):
    __tablename__ = 'address_part_time'
    id = Column(Integer, primary_key=True)
    student_id = Column(Integer, ForeignKey('student.id'),nullable=False)
    address = Column(String(1000),nullable=False)
    student = relationship("Student", back_populates="address_part_time")


class Father(Base):
    __tablename__ = 'father'
    id = Column(Integer, primary_key=True)
    student_id = Column(Integer, ForeignKey('student.id'),nullable=False)
    first_name = Column(String(100),nullable=False)
    last_name = Column(String(100),nullable=False)
    age = Column(Integer,nullable=False)
    life_status = Column(String(30),nullable=False)
    job = Column(String(255),nullable=False)
    position = Column(String(255),nullable=False)
    address_job = Column(String(1000),nullable=False)
    salary = Column(Integer,nullable=False)
    tel = Column(String(10),nullable=False)
    student = relationship("Student", back_populates="father")


class Mother(Base):
    __tablename__ = 'mother'
    id = Column(Integer, primary_key=True)
    student_id = Column(Integer, ForeignKey('student.id'))
    first_name = Column(String(100),nullable=False)
    last_name = Column(String(100),nullable=False)
    age = Column(Integer,nullable=False)
    life_status = Column(String(30),nullable=False)
    job = Column(String(255),nullable=False)
    position = Column(String(255),nullable=False)
    address_job = Column(String(1000),nullable=False)
    salary = Column(Integer,nullable=False)
    tel = Column(String(10),nullable=False)
    student = relationship("Student", back_populates="mother")


class LivingWith(Base):
    __tablename__ = 'living_with'
    id = Column(Integer, primary_key=True)
    student_id = Column(Integer, ForeignKey('student.id'),nullable=False)
    title = Column(String(20),nullable=False)
    first_name = Column(String(100),nullable=False)
    last_name = Column(String(100),nullable=False)
    relationship_living_with = Column(String(255),nullable=False)
    tel = Column(String(10),nullable=False)
    student = relationship("Student", back_populates="living_with")


class Support(Base):
    __tablename__ = 'support'
    id = Column(Integer, primary_key=True)
    student_id = Column(Integer, ForeignKey('student.id'),nullable=False)
    title = Column(String(10),nullable=False)
    first_name = Column(String(100),nullable=False)
    last_name = Column(String(100),nullable=False)
    relevant = Column(String(255),nullable=False)
    job = Column(String(255),nullable=False)
    position = Column(String(255),nullable=False)
    address_job = Column(String(1000),nullable=False)
    salary = Column(Integer,nullable=False)
    tel = Column(String(10),nullable=False)
    student = relationship("Student", back_populates="support")


class InformationHistory(Base):
    __tablename__ = 'information_history'
    id = Column(Integer, primary_key=True)
    student_id = Column(Integer, ForeignKey('student.id'),nullable=False)
    marital_status_of_parents = Column(String(255),nullable=False)
    scholar_history = Column(String(2000),nullable=False)
    sibling_study = Column(String(2000),nullable=False)
    sibling_job = Column(String(2000),nullable=False)
    student = relationship("Student", back_populates="information_history")


class PartTimeJob(Base):
    __tablename__ = 'part_time_job'
    id = Column(Integer, primary_key=True)
    student_id = Column(Integer, ForeignKey('student.id'),nullable=False)
    address = Column(String(500),nullable=False)
    type = Column(String(255),nullable=False)
    how_long = Column(String(255),nullable=False)
    salary = Column(Integer,nullable=False)
    student = relationship("Student", back_populates="part_time_job")


class PaymentHistory(Base):
    __tablename__ = 'payment_history'
    id = Column(Integer, primary_key=True)
    student_id = Column(Integer, ForeignKey('student.id'),nullable=False)
    std_pay_month = Column(Integer,nullable=False)
    std_pay_year = Column(Integer,nullable=False)
    student = relationship("Student", back_populates="payment_history")
