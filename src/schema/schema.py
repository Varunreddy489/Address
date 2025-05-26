from pydantic import BaseModel


class ContactSchema(BaseModel):
    first_name: str
    last_name: str
    address: str
    city: str
    state: str
    zip_code: str
    phone_number: str
    email: str



