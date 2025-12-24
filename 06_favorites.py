from database import engine
from sqlalchemy import text

def create_favorites():
    with engine.begin() as conn:
        conn.execute(text("""
            CREATE TABLE IF NOT EXISTS favorites(
                id bigserial PRIMARY KEY,
                created_at timestamp DEFAULT NOW(),
                user_id bigint,
                product_id bigint,
                UNIQUE(user_id, product_id)
            )
        """))
    print("Favorites table checked/created successfully.")

if __name__ == "__main__":
    create_favorites()
