-- Create Database
CREATE DATABASE bank_db;

USE bank_db;

-- Create Table
CREATE TABLE accounts (
    account_id INT PRIMARY KEY,
    account_holder VARCHAR(50),
    balance DECIMAL(10,2)
);

-- Insert Sample Data
INSERT INTO accounts VALUES
(101, 'Ankush', 5000),
(102, 'Rahul', 3000);

-- Start Transaction
START TRANSACTION;

-- Transfer Money
UPDATE accounts
SET balance = balance - 1000
WHERE account_id = 101;

UPDATE accounts
SET balance = balance + 1000
WHERE account_id = 102;

-- Save Changes
COMMIT;

-- Example Rollback
START TRANSACTION;

UPDATE accounts
SET balance = balance - 500
WHERE account_id = 101;

-- Undo Changes
ROLLBACK;

-- Check Data
SELECT * FROM accounts;