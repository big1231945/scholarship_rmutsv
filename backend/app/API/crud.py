from sqlalchemy.orm import Session
from .schemas import schemas
from ..Database import Models
from fastapi import  HTTPException
import time


def create_from(db: Session, form: schemas.FormCreate):
    # db_form = Models.Student(**form)
    time_now = time.time()
    db_form = Models.Student(
        title_name=form.title_name,
        first_name=form.first_name,
        last_name=form.last_name,
        birthday=form.birthday,
        ethnicity=form.ethnicity,
        nationality=form.nationality,
        religion=form.religion,
        tel=form.tel,
        gpa=form.gpa,
        gpax=form.gpax,
        term=form.term,
        reason=form.reason,
        id_std_copy=form.id_std_copy,
        id_card_copy=form.id_card_copy,
        house_copy=form.house_copy,
        gpa_gpax_copy=form.gpa_gpax_copy,
        photo_house=form.photo_house,
        photo_family=form.photo_family,
        photo_std=form.photo_std,
        time_create = time_now

    )
    db_form.address_house = Models.AddressHouse(
        student_id=form.id,
        address=form.address_house.address,
        subdistrict=form.address_house.subdistrict,
        district=form.address_house.district,
        province=form.address_house.province,
        postal_code=form.address_house.postal_code)
    db_form.address_ez = Models.AddressEZ(
        student_id=form.id,
        address=form.address_house.address,
        subdistrict=form.address_house.subdistrict,
        district=form.address_house.district,
        province=form.address_house.province,
        postal_code=form.address_house.postal_code)
    db_form.address_part_time = Models.AddressPartTime(
        student_id=form.id,
        address=form.address_part_time.address,
    )
    db_form.father = Models.Father(
        student_id=form.id,
        first_name=form.father.first_name,
        last_name=form.father.last_name,
        age=form.father.age,
        life_status=form.father.life_status,
        job=form.father.job,
        position=form.father.position,
        address_job=form.father.address_job,
        salary=form.father.salary,
        tel=form.father.tel
    )
    db_form.mother = Models.Mother(
        student_id=form.id,
        first_name=form.mother.first_name,
        last_name=form.mother.last_name,
        age=form.mother.age,
        life_status=form.mother.life_status,
        job=form.mother.job,
        position=form.mother.position,
        address_job=form.mother.address_job,
        salary=form.mother.salary,
        tel=form.mother.tel
    )
    db_form.living_with = Models.LivingWith(
        student_id=form.id,
        title=form.living_with.title,
        first_name=form.living_with.first_name,
        last_name=form.living_with.last_name,
        relationship_living_with=form.living_with.relationship_living_with,
        tel=form.living_with.tel
    )
    db_form.support = Models.Support(
        student_id=form.id,
        title=form.support.title,
        first_name=form.support.first_name,
        last_name=form.support.last_name,
        relevant=form.support.relevant,
        job=form.support.job,
        position=form.support.position,
        address_job=form.support.address_job,
        salary=form.support.salary,
        tel=form.support.tel
    )
    db_form.information_history = Models.InformationHistory(
        student_id=form.id,
        marital_status_of_parents=form.information_history.marital_status_of_parents,
        scholar_history=form.information_history.scholar_history,
        sibling_study=form.information_history.sibling_study,
        sibling_job=form.information_history.sibling_job
    )
    db_form.part_time_job = Models.PartTimeJob(
        student_id=form.id,
        address=form.part_time_job.address,
        type=form.part_time_job.type,
        how_long=form.part_time_job.how_long,
        salary=form.part_time_job.salary
    )
    db_form.payment_history = Models.PaymentHistory(
        student_id=form.id,
        std_pay_month=form.payment_history.std_pay_month,
        std_pay_year=form.payment_history.std_pay_year
    )
    db.add(db_form)
    db.commit()
    # return db_form


def delete_form(id:int,db: Session): 
    check = db.query(Models.Student).filter(Models.Student.id == id).first()
    if check:
        try:
            db.query(Models.AddressHouse).filter(Models.AddressHouse.student_id == id).delete()
            db.query(Models.AddressEZ).filter(Models.AddressEZ.student_id == id).delete()
            db.query(Models.AddressPartTime).filter(Models.AddressPartTime.student_id == id).delete()
            db.query(Models.Father).filter(Models.Father.student_id == id).delete()
            db.query(Models.Mother).filter(Models.Mother.student_id == id).delete()
            db.query(Models.LivingWith).filter(Models.LivingWith.student_id == id).delete()
            db.query(Models.Support).filter(Models.Support.student_id == id).delete()
            db.query(Models.InformationHistory).filter(Models.InformationHistory.student_id == id).delete()
            db.query(Models.PartTimeJob).filter(Models.PartTimeJob.student_id == id).delete()
            db.query(Models.PaymentHistory).filter(Models.PaymentHistory.student_id == id).delete()
            db.query(Models.Student).filter(Models.Student.id == id).delete()
            db.commit()
        except Exception as e:
            db.rollback()
            raise HTTPException(status_code=500)
    else:
        raise HTTPException(status_code=404)

    
def get_all(db:Session):
    data = db.query(Models.Student).all()
    return data

def update(id:int,db:Session,data:dict):
    form = db.query(Models.Student).filter(Models.Student.id == id).first()
    if form :
        try:
            for key,val in data.items():
                if key not in ["address_house","address_ez","address_part_time","father","mother","living_with","support","information_history","part_time_job","payment_history"]:
                    setattr(form, key, val)
            for key,val in data["address_house"].items():
                setattr(form.address_house, key, val)
            for key,val in data["address_ez"].items():
                setattr(form.address_ez, key, val)
            for key,val in data["address_part_time"].items():
                setattr(form.address_part_time, key, val)
            for key,val in data["father"].items():
                setattr(form.father, key, val)
            for key,val in data["mother"].items():
                setattr(form.mother, key, val)
            for key,val in data["living_with"].items():
                setattr(form.living_with, key, val)
            for key,val in data["support"].items():
                setattr(form.support, key, val)
            for key,val in data["information_history"].items():
                setattr(form.information_history, key, val)
            for key,val in data["part_time_job"].items():
                setattr(form.part_time_job, key, val)
            for key,val in data["payment_history"].items():
                setattr(form.payment_history, key, val)
            db.commit()
        except Exception as e:
            db.rollback()
            raise HTTPException(status_code=500)
    else:
        raise HTTPException(status_code=404)


def filter_time(db:Session,start:int,end:int):
    try:   
        data = db.query(Models.Student).filter(Models.Student.time_create.between(start,end)).all()
        if len(data) > 0 :
            return data
        else:
            raise HTTPException(status_code=404)
    except:
        raise HTTPException(status_code=404)
        