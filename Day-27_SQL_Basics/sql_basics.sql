-- Create Database
CREATE DATABASE company_db;

-- Use Database
USE company_db;

-- Create Table
CREATE TABLE employees (
    emp_id INT PRIMARY KEY,
    name VARCHAR(50),
    age INT,
    department VARCHAR(30),
    salary DECIMAL(10,2)
);

-- View Table Structure
DESCRIBE employees;

-- Show Tables
SHOW TABLES;

-- Show Databases
SHOW DATABASES();