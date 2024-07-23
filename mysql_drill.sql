-- MySQL Drill Exercise

-- 1. Create a database
CREATE DATABASE IF NOT EXISTS company_db;
USE company_db;

-- 2. Create a table
CREATE TABLE employees (
    id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    email VARCHAR(100),
    hire_date DATE,
    salary DECIMAL(10, 2),
    department VARCHAR(50)
);

-- 3. Insert data
INSERT INTO employees (first_name, last_name, email, hire_date, salary, department)
VALUES 
    ('John', 'Doe', 'john.doe@example.com', '2020-01-15', 55000.00, 'IT'),
    ('Jane', 'Smith', 'jane.smith@example.com', '2019-05-20', 62000.00, 'HR'),
    ('Mike', 'Johnson', 'mike.johnson@example.com', '2021-03-10', 48000.00, 'Sales'),
    ('Emily', 'Brown', 'emily.brown@example.com', '2018-11-01', 71000.00, 'IT');

-- 4. Basic SELECT query
SELECT * FROM employees;

-- 5. Filtering with WHERE clause
SELECT first_name, last_name, salary
FROM employees
WHERE salary > 60000;

-- 6. Ordering results
SELECT first_name, last_name, hire_date
FROM employees
ORDER BY hire_date DESC;

-- 7. Aggregate functions
SELECT department, AVG(salary) as avg_salary, COUNT(*) as employee_count
FROM employees
GROUP BY department;

-- 8. Updating data
UPDATE employees
SET salary = salary * 1.1
WHERE department = 'IT';

-- 9. Deleting data
DELETE FROM employees
WHERE hire_date < '2019-01-01';

-- 10. Join operation (first, create a new table)
CREATE TABLE departments (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50),
    manager VARCHAR(100)
);

INSERT INTO departments (name, manager)
VALUES 
    ('IT', 'Alice Cooper'),
    ('HR', 'Bob Marley'),
    ('Sales', 'Charlie Puth');

-- Now perform the JOIN
SELECT e.first_name, e.last_name, e.department, d.manager
FROM employees e
JOIN departments d ON e.department = d.name;

-- 11. Subquery
SELECT first_name, last_name, salary
FROM employees
WHERE salary > (SELECT AVG(salary) FROM employees);

-- 12. Create a view
CREATE VIEW high_paid_employees AS
SELECT first_name, last_name, salary, department
FROM employees
WHERE salary > 60000;

-- Use the view
SELECT * FROM high_paid_employees;
