import os
from database import execute_sql_file

if __name__ == "__main__":
    data_path = os.path.join(os.path.dirname(__file__), "data", "reviews.sql")
    execute_sql_file(data_path)
