-- VIEW

CREATE VIEW employee_details AS
SELECT name, department, salary
FROM employees;

SELECT *
FROM employee_details;


-- INDEX

CREATE INDEX idx_employee_name
ON employees(name);


-- COMPOSITE INDEX

CREATE INDEX idx_department_salary
ON employees(department, salary);


-- STORED PROCEDURE

DELIMITER //

CREATE PROCEDURE GetEmployees()
BEGIN
    SELECT *
    FROM employees;
END //

DELIMITER ;


-- CALL PROCEDURE

CALL GetEmployees();


-- DROP PROCEDURE

DROP PROCEDURE GetEmployees;