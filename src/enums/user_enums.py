from enum import Enum


class Genders(Enum):
    female = 'female'
    male = 'male'


class Statuses(Enum):
    inactive = 'inactive'
    active = 'active'


class EserErrors(Enum):
    WRONG_EMAIL = "Email dosnt't contein @"