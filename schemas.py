from pydantic import BaseModel
from typing import Optional


class SignUpModel(BaseModel):
    id: Optional[int] = None
    username : str
    email: str
    password: str
    is_active: Optional[bool]
    is_staff: Optional[bool]

    class Config:
        orm_mode = True
        schema_extra = {
            "example":{
                "username":"johndoe",
                "email":"johndoe@gmail.com",
                "password":"password",
                "is_active":True,
                "is_staff":False
            }
        }

class signUpResponse(BaseModel):
    id : int
    username: str
    email: str
    is_active: Optional[bool]
    is_staff : Optional[bool]

    class Config:
        orm_mode = True
        from_attributes = True