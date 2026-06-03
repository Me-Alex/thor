CREATE TABLE IF NOT EXISTS listings (
  id SERIAL PRIMARY KEY,
  title TEXT NOT NULL,
  city TEXT,
  price INTEGER,
  rooms INTEGER,
  area REAL,
  source TEXT,
  url TEXT UNIQUE
);
