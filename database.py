import os
from sqlalchemy import create_engine, text
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str = "postgresql://user:password@localhost:5432/retail_db"

settings = Settings()

engine = create_engine(settings.DATABASE_URL)

def execute_sql_file(file_path):
    print(f"Executing {file_path}...")
    with open(file_path, 'r') as f:
        sql = f.read()
    
    with engine.connect() as connection:
        # Split by semicolon to execute one by one if it's multiple commands
        # Simple split might fail with semicolons in strings, but for these data files it should be fine
        commands = sql.split(';')
        for command in commands:
            if command.strip():
                connection.execute(text(command))
                connection.commit()
    print(f"Finished executing {file_path}")
