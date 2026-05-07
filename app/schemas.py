from pydantic import BaseModel, EmailStr
from typing import Optional
from enum import Enum
from datetime import datetime

class UserRole(str, Enum):
    seeker = "seeker"
    recruiter = "recruiter"

class ApplicationStatus(str, Enum):
    pending = "pending"
    accepted = "accepted"
    rejected = "rejected"

class JobType(str, Enum):
    full_time = "full_time"
    part_time = "part_time"
    remote = "remote"
    contract = "contract"

class JobStatus(str, Enum):
    open = "open"
    closed = "closed"

# --- Company Schemas ---
class CompanyBase(BaseModel):
    name: str
    industry: Optional[str] = None
    location: Optional[str] = None

class CompanyCreate(CompanyBase):
    pass

class CompanyResponse(CompanyBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True

# --- User Schemas ---
class UserBase(BaseModel):
    name: str
    email: EmailStr
    role: UserRole


class UserCreate(UserBase):
    password: str
    company_id: Optional[int] = None


class UserResponse(UserBase):
    id: int
    company_id: Optional[int] = None
    created_at: datetime

    class Config:
        from_attributes = True


# --- Job Schemas ---
class JobBase(BaseModel):
    title: str
    description: str
    location: Optional[str] = None
    salary_range: Optional[str] = None
    job_type: Optional[JobType] = None


class JobCreate(JobBase):
    company_id: int


class JobResponse(JobBase):
    id: int
    status: JobStatus
    company_id: int
    posted_at: datetime

    class Config:
        from_attributes = True


# --- Application Schemas ---
class ApplicationBase(BaseModel):
    job_id: int


class ApplicationCreate(ApplicationBase):
    pass




class ApplicationResponse(ApplicationBase):
    id: int
    user_id: int
    status: ApplicationStatus
    applied_at: datetime

    class Config:
        from_attributes = True

class ApplicationStatusUpdate(BaseModel):
    status: ApplicationStatus


# --- Auth Schemas ---
class LoginRequest(BaseModel):
    email: EmailStr
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str