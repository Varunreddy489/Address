from pydantic import BaseModel


class ContactSchema(BaseModel):
    address_book_id: int
    first_name: str
    last_name: str
    email: str
    phone_number: str
    address: str
    city: str
    state: str
    zip_code: str
