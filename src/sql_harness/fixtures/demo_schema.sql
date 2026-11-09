-- Demo schema for local SQLite (loaded by adapter later)
DROP TABLE IF EXISTS orders;
DROP TABLE IF EXISTS customers;

CREATE TABLE customers (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    city TEXT NOT NULL,
    created_at TEXT NOT NULL
);

CREATE TABLE orders (
    id INTEGER PRIMARY KEY,
    customer_id INTEGER NOT NULL REFERENCES customers(id),
    amount REAL NOT NULL,
    status TEXT NOT NULL,
    created_at TEXT NOT NULL
);

INSERT INTO customers (id, name, city, created_at) VALUES
    (1, 'Alice', 'Shanghai', '2024-01-10'),
    (2, 'Bob', 'Beijing', '2024-02-01'),
    (3, 'Carol', 'Shenzhen', '2024-03-15');

INSERT INTO orders (id, customer_id, amount, status, created_at) VALUES
    (101, 1, 120.50, 'paid', '2024-04-01'),
    (102, 1, 80.00, 'refunded', '2024-04-05'),
    (103, 2, 220.00, 'paid', '2024-04-08'),
    (104, 3, 45.25, 'pending', '2024-04-10');
