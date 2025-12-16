from pydantic import BaseModel, field_validator, Field

class UserCreate(BaseModel):
    name: str = Field(..., min_length=2, description="User's name")
    email: str = Field(..., description="User's email address")

    @field_validator('name')
    @classmethod
    def name_must_not_be_empty(cls, v):
        # Trim and remove extra spaces
        v = ' '.join(v.split())
        if not v:
            raise ValueError('Name must not be empty')
        return v

    @field_validator('email')
    @classmethod
    def email_must_contain_at(cls, v):
        # Trim whitespace and remove all spaces from email
        v = v.strip().replace(' ', '')
        if not v or '@' not in v:
            raise ValueError('Email must contain @ symbol')
        # Additional basic validation
        if v.count('@') != 1:
            raise ValueError('Email must contain exactly one @ symbol')
        local, domain = v.split('@')
        if not local or not domain:
            raise ValueError('Email must have text before and after @ symbol')
        # Check for dot in domain
        if '.' not in domain:
            raise ValueError('Email domain must contain at least one dot (.)')
        # Check domain has text before and after the dot
        domain_parts = domain.split('.')
        if any(not part for part in domain_parts):
            raise ValueError('Email domain must have text before and after dot')
        return v.lower()

class UserResponse(BaseModel):
    id: int
    name: str
    email: str

    class Config:
        from_attributes = True

class UserCreateResponse(BaseModel):
    message: str
    user: dict