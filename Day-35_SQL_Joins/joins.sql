-- INNER JOIN
SELECT e.name, d.department_name
FROM employees e
INNER JOIN departments d
ON e.department_id = d.department_id;


-- LEFT JOIN
SELECT e.name, d.department_name
FROM employees e
LEFT JOIN departments d
ON e.department_id = d.department_id;


-- RIGHT JOIN
SELECT e.name, d.department_name
FROM employees e
RIGHT JOIN departments d
ON e.department_id = d.department_id;


-- FULL OUTER JOIN
-- MySQL does not directly support FULL OUTER JOIN.
-- It can be achieved using UNION.

SELECT e.name, d.department_name
FROM employees e
LEFT JOIN departments d
ON e.department_id = d.department_id

UNION

SELECT e.name, d.department_name
FROM employees e
RIGHT JOIN departments d
ON e.department_id = d.department_id;


-- CROSS JOIN
SELECT e.name, d.department_name
FROM employees e
CROSS JOIN departments d;


-- SELF JOIN
SELECT e1.name AS employee,
       e2.name AS manager
FROM employees e1
JOIN employees e2
ON e1.manager_id = e2.emp_id;