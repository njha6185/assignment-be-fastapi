import sys
import os

# Allow imports from root
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from app.models.db.database import engine, Base
from app.models.Employee import Employee

def create_tables():
    print("🔧 Creating tables if not exist...")
    Base.metadata.create_all(bind=engine)
    print("✅ Tables ready.")

if __name__ == "__main__":
    create_tables()