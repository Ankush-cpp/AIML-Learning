-- Subquery with WHERE

SELECT name, salary
FROM employees
WHERE salary > (
    SELECT AVG(salary)
    FROM employees
);


-- Subquery with IN

SELECT name, department
FROM employees
WHERE department IN (
    SELECT department
    FROM employees
    WHERE salary > 50000
);


-- Subquery with MAX

SELECT name, salary
FROM employees
WHERE salary = (
    SELECT MAX(salary)
    FROM employees
);


-- Subquery with MIN

SELECT name, salary
FROM employees
WHERE salary = (
    SELECT MIN(salary)
    FROM employees
);


-- Subquery with COUNT

SELECT name, salary
FROM employees
WHERE salary > (
    SELECT salary
    FROM employees
    WHERE name = 'Rahul'
);


-- Subquery in FROM

SELECT department, avg_salary
FROM (
    SELECT department, AVG(salary) AS avg_salary
    FROM employees
    GROUP BY department
) AS dept_salary
WHERE avg_salary > 45000;