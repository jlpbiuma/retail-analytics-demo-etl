from database import engine
from sqlalchemy import text

def sync_sequences():
    tables = ['users', 'products', 'orders', 'reviews', 'favorites']
    with engine.begin() as conn:
        for table in tables:
            try:
                # Find the max ID and set the sequence to it
                conn.execute(text(f"SELECT setval('{table}_id_seq', (SELECT MAX(id) FROM {table}))"))
                print(f"Synced sequence for {table}")
            except Exception as e:
                print(f"Could not sync sequence for {table}: {e}")

if __name__ == "__main__":
    sync_sequences()
