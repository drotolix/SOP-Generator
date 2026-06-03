import sqlite3 

DB_PATH = "database/sop.db"


def get_connection():
    return sqlite3.connect(DB_PATH)


def create_database():

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS sops (

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        department TEXT NOT NULL,

        process_name TEXT NOT NULL,

        objective TEXT,

        roles TEXT,

        steps TEXT,

        kpis TEXT,

        risks TEXT,

        automation TEXT,

        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)

    conn.commit()
    conn.close()


if __name__ == "__main__":
    create_database()
    print("Database Created Successfully")