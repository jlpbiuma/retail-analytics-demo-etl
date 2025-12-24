# ⚙️ Retail Analytics ETL (Python)

The **Retail Analytics ETL** (Extract, Transform, Load) service is a specialized utility designed to manage the database lifecycle of the platform. It ensures that the PostgreSQL environment is correctly structured, populated with high-quality data, and synchronized for production use.

---

## ✨ Key Features

### 📜 Schema & Integrity
- **Automated Schema Creation**: Generates the full database structure (Users, Products, Orders, Reviews, Favorites) from optimized SQL DDL.
- **Sequence Synchronization**: Fixes a common PostgreSQL issue by syncing Primary Key sequences with the maximum IDs from imported data, preventing registration errors.

### 📥 Data Ingestion Pipeline
- **Smart Loading**: Sequential loading of datasets to maintain foreign key integrity (Users -> Products -> Orders -> Reviews).
- **Large Dataset Support**: Efficiently handles thousands of records using SQLAlchemy and raw SQL execution.
- **Favorites Initialization**: Ensures the wishlist system is ready for use upon first launch.

### 🧹 Maintenance Tools
- **Environment Reset**: Quick commands to drop and recreate the entire schema for testing.
- **Database Utilities**: Shared library for robust database connections and engine management.

---

## 🛠️ Tech Stack
- **Language**: Python 3.10+
- **Package Manager**: [uv](https://github.com/astral-sh/uv)
- **Database Library**: [SQLAlchemy](https://www.sqlalchemy.org/)
- **Driver**: `psycopg2-binary`

---

## 📦 Installation & Setup

### 1. Requirements
Install the `uv` tool for the best experience.

### 2. Configure Environment
```bash
cp .env.example .env
# Set your DATABASE_URL (localhost:5432 for local development)
```

### 3. Run the Full Pipeline
```bash
uv sync
uv run python main.py
```

---

## 📂 Data Inventory

| Dataset | Scope | Purpose |
| :--- | :--- | :--- |
| `users.sql` | 2000+ Records | Initial user accounts and demographic data. |
| `products.sql` | 200+ Records | Rich product catalog with categories and vendors. |
| `reviews.sql` | 1000+ Records | Customer feedback loop and rating data. |
| `schema.sql` | Full DDL | The blueprint of the entire platform. |
