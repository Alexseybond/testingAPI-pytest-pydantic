from pydantic import BaseModel, validator
from src.enums.user_enums import Genders, Statuses, EserErrors


class User(BaseModel):
    id: int
    name: str
    email: str
    gender: Genders
    status: Statuses

    @validator('email')
    def check_that_dog_presented_in_email_address(cls, email):
        if '@' in email:
            return email
        else:
            raise ValueError(EserErrors.WRONG_EMAIL.value)

