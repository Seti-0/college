USE mydb2;

/*
	TASK 1
*/

/*
# Apparently the constraint must be removed
# before the column can be dropped
ALTER TABLE students 
DROP CONSTRAINT FK_students_courses;

ALTER TABLE students 
DROP COLUMN Course;
*/

/*
	Task 2 and 3
*/

/*
CREATE TABLE student_courses (
	StudentID int,
    CourseCode varchar(20),
    PRIMARY KEY (StudentID, CourseCode),
    FOREIGN KEY (StudentID) REFERENCES students(StudentID),
    FOREIGN KEY (CourseCode) REFERENCES courses(CourseCode)
);
*/

/*
	Task 4
*/

/*
INSERT INTO student_courses(StudentID, CourseCode)
VALUES
(12345, 'REL20'),
(23456, 'REL20'),
(34567, 'REL20'),
(11111, 'REL20'),
(12222, 'WEB20'),
(11111, 'WEB20'),
(12345, 'WEB20'),
(23000, 'WEB20'),
(23456, 'WEB20'),
(23000, 'EXL20'),
(11111, 'EXL20'),
(12345, 'EXL20'),
(23456, 'EXL20');
*/

# As expected this fails due to the foreign key constraint.
# DELETE FROM courses WHERE courses.CourseCode = 'REL20'

/*
	Task 5
*/

CREATE TABLE mydb2.employee (
	EmployeeID INT PRIMARY KEY,
    FirstName VARCHAR(20) NOT NULL,
    Surname VARCHAR(20) NOT NULL,
    Salary int DEFAULT 0,
    City VARCHAR(20),
    UNIQUE(FirstName, Surname)
);

INSERT INTO employee(EmployeeID, FirstName, Surname, Salary, City)
VALUES
(1234, 'Killian', 'Carson', 23000, 'Dublin'),
(2345, 'Andy', 'Anderson', 45000, 'Cork'),
(3456, 'Fiona', 'Finnguala', 96000, 'Derry');  

INSERT INTO employee(EmployeeID, FirstName, Surname, Salary, City)
VALUES
(2462, 'Killian', 'Carson', 23000, 'Dublin');

INSERT INTO employee(EmployeeID, FirstName, Surname, Salary, City)
VALUES
(2462, NULL, 'Carson', 23000, 'Dublin');
