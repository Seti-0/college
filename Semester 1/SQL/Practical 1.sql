USE mydb;

/* 
The original command used to create the table
Note that this does not include the comments - I added them in later
with the GUI, but they could have been easily added here using the COMMENT keyword

CREATE TABLE StudentCourses (
	StudentID int NOT NULL,
    FirstName varchar(30) NOT NULL,
    LastName varchar(30) NOT NULL,
    Telephone varchar(20),
    Email varchar(20) UNIQUE,
    CourseCode varchar(20), 
    CourseName varchar(30),
    Duration int DEFAULT 10,
    CourseCost int DEFAULT 300,
    PRIMARY KEY(StudentID)
);
*/

/*
Populating the table with data

INSERT INTO StudentCourses (StudentID, FirstName, LastName, Telephone, Email, CourseCode, CourseName, Duration, CourseCost)
VALUES
(12345, 'Mary', 'Murphy', 2888888, 'MMurphy@ucd.ie', 'REL20', 'Relational databases', 10, 300),
(23456, 'Brian', 'Smith', 6498888, 'Bsmith@ucd.ie', 'REL20', 'Relational databases', 10, 300 ),
(34567, 'Cora', 'Williams', 1234567, 'Cwilliams@ucd.ie', 'REL20', 'Relational databases', 10, 300),
(12222, 'David', 'Honan',  2888888, 'Dhonan@ucd.ie', 'WEB20', 'Web design', 10, 200),
(11111, 'Frank', 'Murphy', 4568777, NULL, 'WEB20', 'Web design',10, 200),
(23000, 'Aoife' , 'Byrne', 987789, 'Abyrne@ucd.ie', 'EXL20', 'Excel', 9, 200);
*/

/* The second table was created and populated using the GUI */

/* Questions */

INSERT INTO StudentCourses 
VALUES (11111, 'Frank', 'Murphy', 45687777, 'Fmurphy@ucd.ie', 'REL20', 'Relational databases', 10, 300);
/*
Problem: duplicate key '11111' 
(a student with that number already exists, and since the number is the primary key for the table it must be unique)
*/

INSERT INTO StudentCourses 
VALUES (33333, 'Frank', 'Murphy', 45687777, 'Fmurphy@ucd.ie', 'REL20', 'Relational databases', 10, 300);
/*
This works (the first time it is run, it won't run anymore)
This is because the key '33333' was unique, in contrast to the first example
*/

/*
If a student must have a single, unique, student number, then no. Each entry must have a unique number, and so each number
may correspond to a single entry only. And each entry only has space for a single course reference. 
*/

/* 
I imagine it is the avoid those entering the information to have to enter the same information repeatedly - 
perhaps those defaults are the most common values. Or perhaps they the values the college will assume are true until
they recieve confirmation that they are not.
*/

/*
All information relating to the course is repeated unnecessarily I think - for example, the course name, duration and cost could
be moved to a "courses" table, which uses the course code as primary key. The course code could be kept here too as foreign key.
*/

/*
Before Frank Murphy was added, 3. Now, 4.
*/

/*
Deletion of Aoife would mean loss of information relating to the Excel course. We might want to save
information relating to the course separately.
*/

