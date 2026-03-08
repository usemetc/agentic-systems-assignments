from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, CheckConstraint, select, insert, update, delete

# Configuration: Update with your MySQL credentials
DB_URL = "mysql+pymysql://root:password@localhost/school_db"

engine = create_engine(DB_URL)
metadata = MetaData()

# Define table
students = Table(
    'students', metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String(50), nullable=False),
    Column('age', Integer),
    Column('city', String(50), nullable=True),
    CheckConstraint('age >= 18', name='age_check')
)

# Create table in DB
metadata.create_all(engine)

# CRUD Operations
with engine.connect() as conn:
    # Insert
    conn.execute(insert(students), [
        {"name": "Rahul", "age": 21, "city": "Mumbai"},
        {"name": "Anjali", "age": 19, "city": "Delhi"},
        {"name": "Vikram", "age": 17, "city": "Pune"} # Note: CheckConstraint may fail if < 18
    ])
    conn.commit()

    # Fetch
    print("Students list:", conn.execute(select(students)).fetchall())

    # Update
    conn.execute(update(students).where(students.c.name == "Rahul").values(city="Bangalore"))
    conn.commit()

    # Delete
    conn.execute(delete(students).where(students.c.age < 20))
    conn.commit()