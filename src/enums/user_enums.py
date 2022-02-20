from enum import Enum


class Genders(Enum):
    female = 'female'
    male = 'male'


class Statuses(Enum):
    inactive = 'INACTIVE'
    active = 'ACTIVE'


class EserErrors(Enum):
    WRONG_EMAIL = "Email dosnt't contein @"