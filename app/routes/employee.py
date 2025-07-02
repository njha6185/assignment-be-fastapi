from fastapi import APIRouter, Depends, Query, Path
from typing import Annotated, Optional
from app.schemas.employee_search_filter_schema import EmployeeSearchFilters
from app.handlers.employee import get_filtered_employees

router = APIRouter(
    prefix="/employee",
    tags=["search"],
    responses = {500: {"description": "Internal Server Error"}},
    )

@router.get("/search")
async def search_employee(filters:Annotated[EmployeeSearchFilters, Query()]):
    """
    Search for employees based on filters.
    """
    return get_filtered_employees(filters)