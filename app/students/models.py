from enum import Enum
from pydantic import BaseModel, EmailStr, Field, field_validator, ValidationError
from datetime import date, datetime
from typing import Optional
import re

class Major(str, Enum):
    programming = "Информатика"

class SStudent(BaseModel):
    student_id: int
    phone_number: str = Field(default=..., description="Номер телефона")
    first_name: str = Field(default=..., min_length=1, max_length=50, description="Имя студента")
    last_name: str = Field(default=..., min_length=1, max_length=50, description="Фамилия студента")
    date_of_birth: date = Field(default=..., description="Дата рождения студента в формате гггг-мм-дд")
    email: EmailStr = Field(default=..., description="Электронная почта студента")
    address: str = Field(default=..., description="Адресс студента")
    enrollment_year: int = Field(default=..., ge=2002, description="Год поступления должен быть не меньше 2002")
    major: Major = Field(default=..., description="Специальность студента")
    course: int = Field(default=..., ge=1, le=5, description="Курс должен быть в диапазоне от 1 до 5")
    special_notes: Optional[str] = Field(default=None, max_length=500, description="Дополнительное заметки, не более 500 символов")
    
    @field_validator("phone_number")
    @staticmethod
    def validate_phone_number(cls, values: str) -> str:
        if not re.match(r'^\+\d{1,15}$', values):
            raise ValueError('Номер телефона должен начинатся с "+" и содержать от 1 до 15 цифр.')
        return values
    @field_validator("date_of_birth")
    @classmethod
    def validate_date_of_birth(cls, values: date):
        if values and values >= datetime.now().date():
            raise ValueError('Дата рождения должна быть в прошлом')
        return values
    
    