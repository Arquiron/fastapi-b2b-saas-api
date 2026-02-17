from pydantic import BaseModel, Field

class CustomerCreate(BaseModel):
    name: str = Field(min_length=2, max_length=120)
    email: str = Field(min_length=5, max_length=255)

class CustomerOut(BaseModel):
    id: int
    name: str
    email: str

