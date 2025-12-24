import os
from database import execute_sql_file

if __name__ == "__main__":
    schema_path = os.path.join(os.path.dirname(__file__), "data", "schema.sql")
    execute_sql_file(schema_path)
