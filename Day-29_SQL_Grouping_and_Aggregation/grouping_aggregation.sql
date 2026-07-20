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
(103,'Priya','IT',20,55000),
(104,'Neha','Sales',23,47000),
(105,'Aman','HR',24,45000);

-- Frequently Used Operators

SELECT * FROM employees
WHERE salary BETWEEN 42000 AND 55000;

SELECT * FROM employees
WHERE department IN ('IT','HR');

SELECT * FROM employees
WHERE name LIKE 'A%';

SELECT * FROM employees
WHERE salary <> 45000;

-- LIMIT

SELECT *
FROM employees
LIMIT 3;

-- ORDER BY

SELECT *
FROM employees
ORDER BY salary DESC;

SELECT *
FROM employees
ORDER BY age ASC;

-- Aggregate Functions

SELECT COUNT(*) AS Total_Employees
FROM employees;

SELECT SUM(salary) AS Total_Salary
FROM employees;

SELECT AVG(salary) AS Average_Salary
FROM employees;

SELECT MAX(salary) AS Highest_Salary
FROM employees;

SELECT MIN(salary) AS Lowest_Salary
FROM employees;

-- GROUP BY

SELECT department,
AVG(salary) AS Average_Salary
FROM employees
GROUP BY department;

SELECT department,
COUNT(*) AS Total_Employees
FROM employees
GROUP BY department;

-- HAVING

SELECT department,
AVG(salary) AS Average_Salary
FROM employees
GROUP BY department
HAVING AVG(salary) > 45000;