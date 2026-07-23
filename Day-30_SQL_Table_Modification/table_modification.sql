-- Create Database
CREATE DATABASE company_db;

USE company_db;

-- Create Table
CREATE TABLE employees (
    emp_id INT PRIMARY KEY,
    name VARCHAR(50),
    department VARCHAR(30),
    age INT,
    salary DECIMAL(10,2)
);

-- Insert Records
INSERT INTO employees VALUES
(101,'Ankush','IT',21,50000),
(102,'Rahul','HR',22,42000),
(103,'Priya','IT',20,55000);

-- UPDATE
UPDATE employees
SET salary = 60000
WHERE emp_id = 101;

UPDATE employees
SET department = 'Finance'
WHERE name = 'Rahul';

-- DELETE
DELETE FROM employees
WHERE emp_id = 102;

-- ALTER TABLE
ALTER TABLE employees
ADD email VARCHAR(100);

ALTER TABLE employees
MODIFY age SMALLINT;

ALTER TABLE employees
DROP COLUMN email;

-- TRUNCATE TABLE
TRUNCATE TABLE employees;

-- Verify Table Structure
DESCRIBE employees;

-- View Data
SELECT * FROM employees;