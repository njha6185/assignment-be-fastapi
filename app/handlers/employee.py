from app.schemas.employee_search_filter_schema import EmployeeSearchFilters
from app.models.Employee import Employee
from app.models.db.database import SessionLocal
from app.config.org_config import get_org_visible_columns

def get_filtered_employees(filters: EmployeeSearchFilters):
    db = SessionLocal()
    try:
        employees = Employee.filter_employees(
            db=db,
            status=[s.value for s in filters.status] if filters.status else None,
            location=filters.location,
            company=filters.company,
            department=filters.department,
            position=filters.position,
            limit=filters.limit,
            offset=filters.offset,
            org_id=filters.org_id
        )

        org_id= filters.org_id

        if(org_id is None):
            return {
                "visible_columns": [],
                "results": employees
            }
        # Get org-specific visible columns
        visible_columns = get_org_visible_columns(org_id)

        # Filter fields per employee
        filtered_results = [
            {field: emp.get(field) for field in visible_columns if field in emp}
            for emp in employees
        ]

        return {
            "visible_columns": visible_columns,
            "results": filtered_results
        }
    finally:
        db.close()
