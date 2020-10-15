USE mydb2;

/* 

############
## TASK 1 ##
############

# First create the tables

/*
CREATE TABLE students (
	StudentID int NOT NULL,
    FirstName varchar(30) NOT NULL,
    LastName varchar(30) NOT NULL,
    Telephone varchar(20),
    Email varchar(20) UNIQUE,
    PRIMARY KEY(StudentID)
);
    
CREATE TABLE courses (
	CourseCode int NOT NULL,
    CourseName varchar(30) NOT NULL,
    Duration int NOT NULL,
    CourseCost int NOT NULL,
    PRIMARY KEY(CourseCode)
);
*/

# I made a mistake in the previous statement - the course code should
# be a varchar.

/*
ALTER TABLE courses
MODIFY COLUMN CourseCode varchar(20) NOT NULL;
*/

# Now for data 

/*
INSERT INTO students(StudentID, FirstName, LastName, Telephone, Email)
VALUES
(12345, 'Mary', 'Murphy', '2888888', 'MMurphy@ucd.ie'),
(23456, 'Brian', 'Smith', '6498888', 'Bsmith@ucd.ie'),
(34567, 'Cora', 'Williams', '1234567', 'Cwilliams@ucd.ie'),
(12222, 'David', 'Honan', '2888888', 'Dhonan@ucd.ie'),
(11111, 'Frank', 'Murphy', '456777', NULL),
(23000, 'Aoife', 'Byrne', '987789', 'Abyrne@ucd.ie');

INSERT INTO courses(CourseCode, CourseName, Duration, CourseCost)
VALUES
('REL20', 'Relational Databases', 10, 300),
('WEB20', 'Web Design', 10, 200),
('EXL20', 'Excel', 9, 200);
*/

############
## Task 2 ##
############

/*
ALTER TABLE students
ADD COLUMN Course varchar(20);

ALTER TABLE students
ADD CONSTRAINT FK_students_courses
FOREIGN KEY (Course) REFERENCES courses(CourseCode)
*/

/*
Fill in the new column. I know, there are much easier ways
to do this but one thing at a time.

UPDATE students
SET Course = 'REL20'
WHERE StudentID = 12345 OR StudentID = 23456 OR StudentID = 34567;

UPDATE students
SET Course = 'WEB20'
WHERE StudentID = '12222' OR StudentID = '11111';

UPDATE students
SET Course = 'EXL20'
WHERE StudentID = '23000'
*/

############
## Task 3 ##
############

/*
CREATE TABLE tutors (
	TutorID int NOT NULL AUTO_INCREMENT,
	FirstName varchar(30) NOT NULL,
    LastName varchar(30) NOT NULL,
    TelephoneNumber varchar(20),
    Email varchar(30),
    Course varchar(20),
    PRIMARY KEY (TutorID),
    FOREIGN KEY (Course) REFERENCES courses(CourseCode)
);

INSERT INTO tutors(FirstName, LastName, TelephoneNumber, Email, Course)
VALUES
('Kelly', 'Rynhart', '1123456', 'kelly.rynhart@ucd.ie', 'REL20'),
('Barry', 'Moore', '2123456', 'barry.moore@ucd.ie', 'REL20'),
('Caleb', 'Altman', '3123456', 'caleb.altman@ucd.ie', 'WEB20'),
('Casey', 'Millikan', '4123456', 'casey.millikan@ucd.ie', 'EXL20');
*/

############
## TASK 4 ##
############

/* Part 1: Select student id of all students */
SELECT StudentID FROM students;

/* Part 2: Select last name of all students */
SELECT LastName FROM students;

/* Part 3: Select first name of all students*/
SELECT FirstName FROM students;

/* Part 4: Select first and last names for student with id = 11111 */
SELECT FirstName, LastName FROM students
WHERE StudentID = 11111;

/* Part 5: Find the name of the courses taken by students with 
last name 'Murphy' */
SELECT CourseName FROM students
INNER JOIN courses ON students.Course = courses.CourseCode
WHERE LastName = 'Murphy';
