DROP TABLE IF EXISTS students;
CREATE TABLE students (
    id serial PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    age INT NOT NULL,
    grade VARCHAR(1)
);

SELECT * FROM students;