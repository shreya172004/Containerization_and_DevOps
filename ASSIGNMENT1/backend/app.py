from fastapi import FastAPI
from pydantic import BaseModel
import psycopg2
import os
import time

app = FastAPI(title="Containerized Web App", version="1.0.0")

DB_HOST = os.getenv("DB_HOST", "db")
DB_PORT = os.getenv("DB_PORT", "5432")
DB_NAME = os.getenv("DB_NAME", "appdb")
DB_USER = os.getenv("DB_USER", "shreya")
DB_PASS = os.getenv("DB_PASS", "shreya123")

def get_connection():
    retries = 5
    while retries > 0:
        try:
            conn = psycopg2.connect(
                host=DB_HOST, port=DB_PORT,
                dbname=DB_NAME, user=DB_USER, password=DB_PASS
            )
            return conn
        except psycopg2.OperationalError:
            retries -= 1
            time.sleep(2)
    raise Exception("Could not connect to database.")

def init_db():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS records (
            id SERIAL PRIMARY KEY,
            data TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    conn.commit()
    cur.close()
    conn.close()

@app.on_event("startup")
def startup_event():
    init_db()

class RecordIn(BaseModel):
    data: str

@app.get("/health")
def health_check():
    return {"status": "healthy", "service": "fastapi-backend"}

@app.post("/api/records")
def insert_record(record: RecordIn):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("INSERT INTO records (data) VALUES (%s) RETURNING id", (record.data,))
    new_id = cur.fetchone()[0]
    conn.commit()
    cur.close()
    conn.close()
    return {"message": "Record inserted successfully", "id": new_id}

@app.get("/api/records")
def fetch_records():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT id, data, created_at FROM records ORDER BY id")
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return [{"id": r[0], "data": r[1], "created_at": str(r[2])} for r in rows]
```

---

### File 3
**Name:** `backend/requirements.txt`
**Path:** `ASSIGNMENT1/backend/requirements.txt`
```
fastapi==0.110.0
uvicorn==0.29.0
psycopg2-binary==2.9.9
pydantic==2.6.4
