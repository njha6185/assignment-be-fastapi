import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from app.models.Employee import Employee
from app.models.db.database import SessionLocal

def seed_data():
    db = SessionLocal()
    if not db.query(Employee).first():
        employees = [
            Employee(
                org_id="org1",
                first_name="John",
                last_name="Doe",
                department="Engineering",
                location="New York",
                position="Engineer",
                email="john@example.com",
                phone="1234567890",
                status="active",
                company="ACME Corp"
            ),
            Employee(
                org_id="org1",
                first_name="Jane",
                last_name="Smith",
                department="HR",
                location="London",
                position="HR Manager",
                email="jane@example.com",
                phone="9876543210",
                status="terminated",
                company="ACME Corp"
            ), 
            Employee(
                org_id="org2",
                first_name="Alice",
                last_name="Johnson",
                department="Marketing",
                location="San Francisco",
                position="Marketing Specialist",
                email="alice@example.com",
                phone="5551234567",
                status="active",
                company="Tech Innovations"
            ),
            Employee(
                org_id="org2",
                first_name="Bob",
                last_name="Brown",
                department="Sales",
                location="Chicago",
                position="Sales Executive",
                email="bob.brown@example,com",
                phone="5559876543",
                status="not_started",
                company="Tech Innovations"
            ),
            Employee(
                org_id="org3",
                first_name="Charlie",
                last_name="White",
                department="Finance",
                location="Los Angeles",
                position="Financial Analyst",
                email="charlie@example.com",
                phone="5554567890",
                status="active",
                company="Global Finance"
            ),
            Employee(
                org_id="org3",
                first_name="Diana",
                last_name="Green",
                department="Legal",
                location="Miami",
                position="Legal Advisor",
                email="green@example.com",
                phone="5553216549",
                status="terminated",
                company="Global Finance"
            ),
        ]
    
        db.add_all(employees)
        db.commit()
        print("Seed data inserted.")
    else:
        print("Seed data already exists.")
    db.close()

if __name__ == "__main__":
    seed_data()
