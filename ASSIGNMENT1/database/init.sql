DO $$ BEGIN
  CREATE USER shreya WITH PASSWORD 'shreya123';
EXCEPTION WHEN duplicate_object THEN
  RAISE NOTICE 'User already exists, skipping.';
END $$;

GRANT ALL PRIVILEGES ON DATABASE appdb TO shreya;

\connect appdb;

CREATE TABLE IF NOT EXISTS records (
    id SERIAL PRIMARY KEY,
    data TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public TO shreya;
GRANT ALL PRIVILEGES ON ALL SEQUENCES IN SCHEMA public TO shreya;
```

---

### File 8
**Name:** `index.html`
**Path:** `ASSIGNMENT1/index.html`

> This is the GitHub Pages site — download it from the files I shared earlier in this chat (the `index` file) and upload it directly. It's too long to paste here.

---

### Summary of structure:
```
ASSIGNMENT1/
├── index.html
├── docker-compose.yml
├── backend/
│   ├── app.py
│   ├── requirements.txt
│   ├── Dockerfile
│   └── .dockerignore
└── database/
    ├── Dockerfile
    └── init.sql
