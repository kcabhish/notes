# NOTES

What is Pydantic?

Pydantic is a popular Python library for data validation, parsing, and settings management that uses Python type hints to define how data should look—and then enforces it at runtime.

Core Concepts

You define a model by extending BaseModel:
```
from pydantic import BaseModel

class User(BaseModel):
    id: int
    name: str
    email: str
    is_active: bool = True

```

Example with nested data
```
from typing import List
from pydantic import BaseModel

class Item(BaseModel):
    name: str
    price: float

class Order(BaseModel):
    id: int
    items: List[Item]

```

Example with Custom validation
```
from pydantic import BaseModel, field_validator

class User(BaseModel):
    username: str

    @field_validator("username")
    def no_spaces(cls, v):
        if " " in v:
            raise ValueError("Username must not contain spaces")
        return v

```

