from pydantic import BaseModel


class AddressHouse(BaseModel):
    id: int | None = None
    student_id: int | None = None
    address: str
    subdistrict: str
    district: str
    province: str
    postal_code: str

    class Config:
        from_attributes = True


class AddressEZ(BaseModel):
    id: int | None = None
    student_id: int | None = None
    address: str
    subdistrict: str
    district: str
    province: str
    postal_code: str

    class Config:
        from_attributes = True


class AddressPartTime(BaseModel):
    id: int | None = None
    student_id: int | None = None
    address: str

    class Config:
        from_attributes = True


class Father(BaseModel):
    id: int | None = None
    student_id: int | None = None
    first_name: str
    last_name: str
    age: int
    life_status: str
    job: str
    position: str
    address_job: str
    salary: int
    tel: str

    class Config:
        from_attributes = True


class Mother(BaseModel):
    id: int | None = None
    student_id: int | None = None
    first_name: str
    last_name: str
    age: int
    life_status: str
    job: str
    position: str
    address_job: str
    salary: int
    tel: str

    class Config:
        from_attributes = True


class LivingWith(BaseModel):
    id: int | None = None
    student_id: int | None = None
    title: str
    first_name: str
    last_name: str
    relationship_living_with: str
    tel: str

    class Config:
        from_attributes = True


class Support(BaseModel):
    id: int | None = None
    student_id: int | None = None
    title: str
    first_name: str
    last_name: str
    relevant: str
    job: str
    position: str
    address_job: str
    salary: int
    tel: str

    class Config:
        from_attributes = True


class InformationHistory(BaseModel):
    id: int | None = None
    student_id: int | None = None
    marital_status_of_parents: str
    scholar_history: str
    sibling_study: str
    sibling_job: str

    class Config:
        from_attributes = True


class PartTimeJob(BaseModel):
    id: int | None = None
    student_id: int | None = None
    address: str
    type: str
    how_long: str
    salary: int

    class Config:
        from_attributes = True


class PaymentHistory(BaseModel):
    id: int | None = None
    student_id: int | None = None
    std_pay_month: int
    std_pay_year: int

    class Config:
        from_attributes = True


class Student(BaseModel):
    id: int | None = None
    title_name: str
    first_name: str
    last_name: str
    birthday: str
    ethnicity: str
    nationality: str
    religion: str
    tel: str
    gpa: float
    gpax: float
    term: str
    reason: str
    id_std_copy: str
    id_card_copy: str
    house_copy: str
    gpa_gpax_copy: str
    photo_house: str
    photo_family: str
    photo_std: str
    time_create: int | None = None
    address_house: AddressHouse
    address_ez: AddressEZ
    address_part_time: AddressPartTime
    father: Father
    mother: Mother
    living_with: LivingWith
    support: Support
    information_history: InformationHistory
    part_time_job: PartTimeJob
    payment_history: PaymentHistory

    class Config:
        from_attributes = True


class FormCreate(Student):
    pass


class TimeBetween(BaseModel):
    start:int
    end:int