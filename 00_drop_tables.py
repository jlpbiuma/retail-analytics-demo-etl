from sqlalchemy import text
from database import engine

def drop_tables():
    tables = ["reviews", "orders", "users", "products"]
    with engine.connect() as connection:
        for table in tables:
            print(f"Dropping table {table}...")
            connection.execute(text(f"DROP TABLE IF EXISTS {table} CASCADE;"))
            connection.commit()
    print("All tables dropped.")

if __name__ == "__main__":
    drop_tables()
