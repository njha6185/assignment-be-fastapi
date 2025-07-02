# app/db/models.py
from sqlalchemy import Column, String, Integer
from app.models.db.database import Base  # Import from a centralized database config
from sqlalchemy import func

class Employee(Base):
    __tablename__ = "employees"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    org_id = Column(String, index=True, nullable=False, index=True)
    company = Column(String, index=True, nullable=False, index=True)
    department = Column(String, index=True, nullable=True, index=True)
    location = Column(String, index=True, nullable=True, index=True)
    position = Column(String, index=True, nullable=True, index=True)
    email = Column(String, nullable=False, unique=True)
    phone = Column(String, nullable=True)
    status = Column(String, default="active", index=True)

    @classmethod
    def filter_employees(
        cls,
        db,
        status=None,
        location=None,
        company=None,
        department=None,
        position=None,
        org_id=None,
        limit=10,
        offset=0
    ):
        query = db.query(cls)

        if status:
            query = query.filter(func.lower(cls.status).in_([s.lower() for s in status]))
        if location:
            query = query.filter(func.lower(cls.location) == location.lower())
        if company:
            query = query.filter(func.lower(cls.company) == company.lower())
        if department:
            query = query.filter(func.lower(cls.department) == department.lower())
        if position:
            query = query.filter(func.lower(cls.position) == position.lower())
        if org_id:
            query = query.filter(func.lower(cls.org_id) == org_id.lower())


        results = query.offset(offset).limit(limit).all()
        return [emp.__dict__ for emp in results]
