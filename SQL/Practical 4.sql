USE mydb2;

/*
	TASK 1
*/

# 1)
SELECT students.FirstName FROM students
JOIN student_courses ON students.StudentID = student_courses.StudentID
WHERE student_courses.CourseCode = 'WEB20';

# 2)
SELECT FirstName, LastName FROM students;

# 3)
SELECT * FROM students
WHERE StudentID = 11111;

# 4)
SELECT FirstName FROM students
WHERE LastName = 'Murphy';

# 5)
SELECT CourseCode FROM courses
WHERE CourseName = 'Relational Databases';

# Yes, there could be more than one course with
# with that name - the name is not constrained to be unique

# 6)
SELECT CourseCode, CourseName FROM courses
WHERE CourseCost < 250;

# 7)
SELECT * FROM students
WHERE Email IS NULL;

# 8)
SELECT LastName FROM students
JOIN student_courses ON students.StudentID = student_courses.StudentID
WHERE student_courses.CourseCode = 'REL20';

# 9)
SELECT CourseCode FROM students
JOIN student_courses ON students.StudentID = student_courses.StudentID
WHERE students.StudentID = 11111;

# 10)
SELECT DISTINCT StudentID FROM student_courses
JOIN courses ON student_courses.CourseCode = courses.CourseCode
WHERE CourseCost < 250;

# 11)
SELECT DISTINCT LastName, students.StudentID FROM student_courses
JOIN courses ON student_courses.CourseCode = courses.CourseCode
JOIN students ON student_courses.StudentID = students.StudentID
WHERE CourseCost < 250;

# 12)
SELECT DISTINCT CourseName, courses.CourseCode FROM courses
JOIN student_courses ON courses.CourseCode = student_courses.CourseCode
JOIN students ON students.StudentID = student_courses.StudentID
WHERE students.LastName = 'Murphy';

/*
	Task 2
*/

# Dropping the current constraints so that they can be replaced
# Remember the tutors foreign key!

ALTER TABLE student_courses
DROP CONSTRAINT FK_studentcourses_students;

ALTER TABLE student_courses
DROP CONSTRAINT FK_studentcourses_courses;

ALTER TABLE tutors
DROP CONSTRAINT tutors_ibfk_1;

# New constraints set to cascade

ALTER TABLE student_courses
ADD CONSTRAINT FK_studentcourses_students
FOREIGN KEY (StudentID) REFERENCES students(StudentID)
ON UPDATE CASCADE;

ALTER TABLE student_courses
ADD CONSTRAINT FK_studentcourses_courses
FOREIGN KEY (CourseCode) REFERENCES courses(CourseCode)
ON UPDATE CASCADE;

ALTER TABLE tutors
ADD CONSTRAINT FK_tutors_courses
FOREIGN KEY (Course) REFERENCES courses(CourseCode)
ON UPDATE CASCADE;

# Experiment: does it cascade?

UPDATE courses
SET CourseCode = 'WEB21'
WHERE CourseCode = 'WEB20';

# (It did)

# Experiment: after setting foreign key constraints on
# deleting from courses to NO ACTION, is the row deleted?

DELETE FROM courses
WHERE CourseCode = 'EXL20';

# (It did not)

/*
	Task 3
*/

/*
  
  (Relational Algebra)
  
#1
students nat join student_courses on CourseCode
-> select where CourseCode = 'WEB20'
-> project on FirstName

#2
students -> project on FirstName, LastName

#3
students -> select where StudentID = 11111

#4
students -> select where LastName = 'Murphy'
-> project on FirstName

#5
courses -> select where CourseName = 'Relational Databases'

#6
courses -> select where CourseCode < 250
-> project on CourseName, CourseCode

#7
students -> select where Email is null

#8
students nat join student_courses on StudentID
-> select where CourseCode = 'REL20'

#9
courses nat join student_courses on CourseID
-> select where studentID = 11111

#10
courses nat join student_courses on CourseID
-> select where CourseCost < 250
-> project on StudentID

## FOR 11 AND 12 ##
A = students nat join student_courses on StudentID
B = courses nat join A on CourseID

#11
B -> select where CourseCost < 250 
-> select LastName, StudentID

#12
B -> select where LastName = 'Murphy'
-> project on CourseName, CourseCode

*/