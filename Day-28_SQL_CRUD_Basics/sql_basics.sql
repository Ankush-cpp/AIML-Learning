-- Create Database
CREATE DATABASE company_db;

-- Use Database
USE company_db;

-- Create Table
CREATE TABLE employees (
    emp_id INT PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    age INT,
    department VARCHAR(30),
    salary DECIMAL(10,2)
);

-- Show Databases
SHOW DATABASES;

-- Show Tables
SHOW TABLES;

-- Describe Table
DESCRIBE employees;

-- Insert Records
INSERT INTO employees
(emp_id, name, age, department, salary)
VALUES
(101, 'Ankush', 21, 'IT', 50000);

INSERT INTO employees
VALUES
(102, 'Rahul', 22, 'HR', 42000);

INSERT INTO employees
VALUES
(103, 'Priya', 20, 'IT', 55000);

INSERT INTO employees
VALUES
(104, 'Neha', 23, 'Sales', 47000);

-- Select All
SELECT * FROM employees;

-- Select Specific Columns
SELECT name, salary
FROM employees;

-- WHERE Clause
SELECT *
FROM employees
WHERE department = 'IT';

SELECT *
FROM employees
WHERE salary > 45000;

SELECT *
FROM employees
WHERE age >= 21;

-- Frequently Used Operators

SELECT *
FROM employees
WHERE salary BETWEEN 40000 AND 55000;

SELECT *
FROM employees
WHERE department IN ('IT', 'HR');

SELECT *
FROM employees
WHERE name LIKE 'A%';

SELECT *
FROM employees
WHERE salary <> 42000;

SELECT *
FROM employees
WHERE age IS NOT NULL;