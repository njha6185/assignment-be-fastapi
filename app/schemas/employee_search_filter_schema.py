# app/schemas/search.py
from pydantic import BaseModel, Field
from typing import List, Optional
from enum import Enum

class StatusEnum(str, Enum):
    active = "Active"
    terminated = "Terminated"
    not_started = "Not started"

class EmployeeSearchFilters(BaseModel):
    org_id: Optional[str] = Field(None, description="Organization ID to filter employees")
    status: Optional[List[StatusEnum]] = Field(None, description="Filter by employee status")
    location: Optional[str] = Field(None, description="Filter by location")
    company: Optional[str] = Field(None, description="Filter by company")
    department: Optional[str] = Field(None, description="Filter by department")
    position: Optional[str] = Field(None, description="Filter by position")
    limit: int = Field(le=100,ge=0, default=10, description="Maximum number of results to return")
    offset: int = 0
    