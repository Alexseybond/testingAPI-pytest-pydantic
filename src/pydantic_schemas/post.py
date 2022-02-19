from pydantic import BaseModel, validator, Field


class Post(BaseModel):
    id: int #= Field(le=0)
    title: str

    @validator("id")
    def check_that_id_is_less_than_two(cls, var):
        """
        Метод как пример.
        Это равноценно '= Field(le=0)'
        """
        if var <= 0:
            raise ValueError('ID is not less than 0')
        else:
            return var


