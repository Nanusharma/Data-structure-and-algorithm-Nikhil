from typing import Optional
from pydantic import BaseModel

class User(BaseModel):
    id: int
    name: str
    email: str
    age: Optional[int] = None  # Default value is None

user = User(id=1, name="John Doe", email="john.doe@example.com")
print(user)