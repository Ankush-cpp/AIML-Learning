CREATE DATABASE bank_db;

USE bank_db;

CREATE TABLE accounts (
    account_id INT PRIMARY KEY,
    account_holder VARCHAR(50),
    balance DECIMAL(10,2)
);

INSERT INTO accounts VALUES
(101, 'Ankush', 5000),
(102, 'Rahul', 3000);

-- Start Transaction
START TRANSACTION;

UPDATE accounts
SET balance = balance - 1000
WHERE account_id = 101;

UPDATE accounts
SET balance = balance + 1000
WHERE account_id = 102;

-- Permanently save the changes
COMMIT;

SELECT * FROM accounts;